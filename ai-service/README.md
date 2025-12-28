# AI Service

This is a FastAPI-based Python service that acts as the AI agent for the Shopify Analytics application.

## Setup

1.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    Create a `.env` file with the following keys:

    ```
    SHOPIFY_API_KEY=your_key
    SHOPIFY_API_SECRET=your_secret
    ```

3.  **Run the Service**:
    ```bash
    python main.py
    ```
    The service runs on `http://0.0.0.0:8000`.

## API Endpoints

- `GET /`: Health check. Returns `{"status": "ok", "service": "ai-service"}`.
- `POST /api/v1/analyze`: Analyzes a natural language question.
  - **Body**: `{"store_id": "...", "question": "..."}`
  - **Response**: `{"answer": "...", "confidence": "...", "meta": {...}}`
