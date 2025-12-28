# Rails API

This is the main backend application for the Shopify Analytics App. It handles Shopify authentication and proxying requests to the AI Service.

## Setup

1.  **Install Dependencies**:

    ```bash
    bundle install
    ```

2.  **Database Setup**:

    - Ensure PostgreSQL is running.
    - Configure `config/database.yml` with your credentials.
    - Create and migrate the database:
      ```bash
      rails db:create
      rails db:migrate
      ```

3.  **Run the Server**:
    ```bash
    rails s -p 3000
    ```

## Endpoints

- `POST /api/v1/questions`: Main endpoint for user queries.
