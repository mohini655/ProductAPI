# ProductAPI

This is the Backend ProductAPI Project, built with FastAPI and SQLAlchemy, using PostgreSQL as the database.

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs with Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: Advanced open source relational database.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: ASGI web server implementation for Python.

## Prerequisites

- Python 3.7+
- PostgreSQL database
- Docker and Docker Compose (for database setup)

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
## Database Setup

1. Start the PostgreSQL database using Docker Compose

2. Create a ".env" file in the root directory with the following environment variables:
   ```
   POSTGRES_USER=your_postgres_user
   POSTGRES_PASSWORD=your_postgres_password
   POSTGRES_DB=your_postgres_db
   PGADMIN_DEFAULT_EMAIL=your_pgadmin_email
   PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password
   ```

3. Update the DATABASE_URL in config.py file if necessary to match your database credentials.

## Running the Application

1. Ensure the database is running:
   ```bash
   docker-compose up -d
   ```

2. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

3. The API will be available at `http://localhost:8000`

4. Interactive API documentation (Swagger UI) at `http://localhost:8000/docs`

## API Endpoints

### GET /
- **Description**: Greeting endpoint
- **Parameters**: `name` (optional, default: "User")
- **Response**: JSON object with greeting message

### GET /products
- **Description**: Retrieve all products
- **Response**: List of product objects

### GET /product/{product_id}
- **Description**: Retrieve a specific product by ID
- **Parameters**: `product_id` (integer)
- **Response**: Product object or error message

### POST /product
- **Description**: Add a new product
- **Body**: Product object (JSON)
- **Response**: Success message

### PUT /product/{product_id}
- **Description**: Update an existing product
- **Parameters**: `product_id` (integer)
- **Body**: Updated product object (JSON)
- **Response**: Success message or error message

### DELETE /product/{product_id}
- **Description**: Delete a product by ID
- **Parameters**: `product_id` (integer)
- **Response**: Success message or error message

