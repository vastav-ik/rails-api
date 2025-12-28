# AI-Powered Shopify Analytics App

This project implements a mini operational intelligence application that connects to a Shopify store and uses a Python-based LLM agent to answer natural language questions about store data.

## Architecture

The system consists of two main components:

1.  **Rails API (`rails-api`)**:

    - Acts as the main entry point and "Shopify App".
    - Handles Shopify OAuth authentication (configured via `shopify_app` gem).
    - Exposes `POST /api/v1/questions` to receive user queries.
    - Forwards queries to the Python AI service.

2.  **Python AI Service (`ai-service`)**:
    - Built with FastAPI.
    - Receives questions + store context.
    - "Simulates" an LLM agent (mocked for this assignment, but structured for real LLM integration).
    - Determines user intent (Inventory, Sales, Customers).
    - Generates "ShopifyQL" (or GraphQL) queries.
    - Returns natural language explanations.

## Setup Instructions

### Prerequisites

- Ruby 3.x / Rails 7+
- Python 3.9+
- Shopify Partner Account (to create an app)

### 1. Rails API Setup

```bash
cd rails-api
bundle install
# Set environment variables for Shopify
# export SHOPIFY_API_KEY=your_key
# export SHOPIFY_API_SECRET=your_secret
rails s -p 3000
```

### 2. Python Service Setup

```bash
cd ai-service
pip install -r requirements.txt
python main.py
# Runs on http://0.0.0.0:8000
```

## Usage

Send a POST request to the Rails API:

```bash
curl -X POST http://localhost:3000/api/v1/questions \
  -H "Content-Type: application/json" \
  -d '{
    "store_id": "test-store.myshopify.com",
    "question": "How much inventory do I have?"
  }'
```

## Agent Flow

1.  **Input**: "How much inventory?"
2.  **Rails**: Validates request, calls Python `api/v1/analyze`.
3.  **Python Agent**:
    - Classifies intent: `inventory_optimization`
    - Generates Query: `FROM inventory_items SHOW ...`
    - (Mock) Executes Query against Shopify.
    - Generates Explanation: "Based on data..."
4.  **Rails**: Returns JSON to user.
