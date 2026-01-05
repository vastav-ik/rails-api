import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class Agent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze(self, question: str):
        question = question.lower()
        if any(word in question for word in ["inventory", "stock", "reorder", "product"]):
            intent = "inventory_optimization"
        elif any(word in question for word in ["sales", "selling", "revenue", "order"]):
            intent = "sales_analytics"
        else:
            intent = "general_inquiry"
        return {"intent": intent}
    
    def explain(self, question: str, data: any, plan: dict):
        if not data or (isinstance(data, dict) and "error" in data):
            return "I couldn't find any data to analyze."

        try:
            prompt = (
                f"As a Shopify business assistant, answer the user's question: '{question}' "
                f"using this data: {data}. Give a specific recommendation in 3 sentences."
            )
            
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                return response.text
            else:
                return "The AI retrieved the data but provided an empty response."
                
        except Exception as e:
            if "API key not valid" in str(e):
                return "Error: Your Gemini API Key is invalid. Please check your .env file."
            
            print(f"ERROR: {e}")
            return f"I have the data: {data}. (AI Insight unavailable: {str(e)})"

agent_instance = Agent()