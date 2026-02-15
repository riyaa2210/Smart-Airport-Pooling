🚖 Ride Pooling System – FastAPI (Async)

A high-performance Async Ride Pooling Backend System built using FastAPI, PostgreSQL, and SQLAlchemy 2.0 (Async) with support for concurrency control using row-level locking.

🚀 Tech Stack

Backend: FastAPI (Async REST API)

Database: PostgreSQL

ORM: SQLAlchemy 2.0 (Async)

Driver: asyncpg

Concurrency Control: Row-Level Locks

Python Version: 3.11+

📂 Project Structure
app/
│
├── main.py              # Entry point
├── database.py          # Database configuration
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── dependencies.py      # Dependency injection
│
├── routers/
│   ├── ride.py          # Ride endpoints
│   └── cab.py           # Cab endpoints
│
├── services/
│   ├── pooling.py       # Ride pooling logic
│   └── pricing.py       # Pricing logic
│
└── concurrency.py       # Row-level locking logic

⚙️ Features

✅ Create and manage rides

✅ Cab allocation system

✅ Ride pooling logic

✅ Dynamic pricing module

✅ Async database operations

✅ Row-level locking to prevent race conditions

✅ Clean layered architecture (Router → Service → DB)

🛠 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Configuration

Create a .env file in the root directory:

DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname


Replace:

user → PostgreSQL username

password → PostgreSQL password

dbname → Your database name

Make sure PostgreSQL is running.

▶️ Running the Server
uvicorn app.main:app --reload


Server will start at:

http://127.0.0.1:8000

📖 API Documentation

FastAPI automatically generates interactive API docs:

🔹 Swagger UI → http://127.0.0.1:8000/docs

🔹 ReDoc → http://127.0.0.1:8000/redoc

🧠 Architecture Overview

This project follows a clean separation of concerns:

Routers → Define API endpoints

Services → Business logic layer

Models → Database representation

Schemas → Request/Response validation

Concurrency Layer → Handles row-level locks for safe ride allocation

This ensures:

Scalability

Maintainability

Testability

🔒 Concurrency Handling

The system uses PostgreSQL row-level locks (SELECT FOR UPDATE) to:

Prevent double cab assignment

Avoid race conditions during ride allocation

Maintain consistency under high load

🧪 Future Improvements

Add JWT Authentication

Add Docker support

Add Alembic migrations

Add Redis caching

Add unit & integration tests

CI/CD pipeline
