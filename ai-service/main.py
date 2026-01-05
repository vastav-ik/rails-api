from fastapi import FastAPI
from pydantic import BaseModel
import shopify
import os

app = FastAPI()

class QuestionRequest(BaseModel):
    store_id: str
    question: str
    access_token: str = None

from agent.core import agent_instance

def get_real_shopify_data(store_id, token, intent):
    session = shopify.Session(store_id, "2024-01", token)
    shopify.ShopifyResource.activate_session(session)
    
    data_summary = []
    chart_data = []

    try:
        if intent == "inventory_optimization":
            products = shopify.Product.find(limit=8)
            for p in products:
                qty = sum(int(v.inventory_quantity or 0) for v in p.variants)
                data_summary.append(f"{p.title}: {qty} units")
                chart_data.append({"name": p.title[:12], "value": qty})
        
        elif intent == "sales_analytics":
            orders = shopify.Order.find(limit=10, status="any")
            for o in orders:
                total = float(o.total_price)
                data_summary.append(f"Order {o.name}: ${total}")
                chart_data.append({"name": o.name, "value": total})
        
        else:
            data_summary = ["General store info retrieved"]

    finally:
        shopify.ShopifyResource.clear_session()
        
    return {"summary": data_summary, "chart": chart_data}

@app.post("/api/v1/analyze")
def analyze_question(request: QuestionRequest):
    plan = agent_instance.analyze(request.question)
    intent = plan.get("intent")
    
    if request.access_token:
        try:
            result = get_real_shopify_data(request.store_id, request.access_token, intent)
            data = result["summary"]
            chart_data = result["chart"]
        except Exception as e:
            data = {"error": f"API Error: {str(e)}"}
            chart_data = []
    else:
        data = ["No token provided"]
        chart_data = []

    answer = agent_instance.explain(request.question, data, plan)
    
    return {
        "answer": answer,
        "intent": intent,
        "chart_data": chart_data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)