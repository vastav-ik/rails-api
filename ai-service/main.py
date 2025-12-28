from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class QuestionRequest(BaseModel):
    store_id: str
    question: str

from agent.core import agent_instance

@app.get("/")
def read_root():
    return {"status": "ok", "service": "ai-service"}

@app.post("/api/v1/analyze")
def analyze_question(request: QuestionRequest):
    plan = agent_instance.analyze(request.question)
    
    data = {"mock_data": "sample results from shopify"}
    
    answer = agent_instance.explain(request.question, data, plan)
    
    return {
        "answer": answer,
        "confidence": "high (mock)",
        "meta": plan
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
