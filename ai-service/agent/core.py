import json
import re

class Agent:
    def __init__(self):
        pass

    def analyze(self, question: str):
        question = question.lower()
        
        if "inventory" in question or "stock" in question or "reorder" in question:
            intent = "inventory_optimization"
            shopify_ql = "FROM inventory_items SHOW id, sku, inventory_levels LIMIT 5"
        elif "sales" in question or "selling" in question:
            intent = "sales_analytics"
            shopify_ql = "FROM orders SHOW id, total_price, line_items SINCE -30d"
        elif "customer" in question:
            intent = "customer_segmentation"
            shopify_ql = "FROM customers SHOW id, orders_count, total_spent"
        else:
            intent = "general_inquiry"
            shopify_ql = ""
            
        return {
            "intent": intent,
            "shopify_ql": shopify_ql,
            "explanation_prompt": f"Explain {intent} based on the data."
        }
    
    def explain(self, question: str, data: any, plan: dict):
        if not data:
            return "I couldn't find any relevant data."
            
        return f"Based on your request regarding {plan['intent']}, here is what I found. (Mock Data Summary: {len(str(data))} bytes)"

agent_instance = Agent()
