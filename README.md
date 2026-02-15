🚖 Async Ride Pooling Backend System

A high-performance Ride Pooling Backend System built using FastAPI (Async) and PostgreSQL, designed to handle concurrent ride allocations safely using row-level locking.

This project demonstrates:

Async backend development

Database transaction management

Concurrency control

Clean architecture principles

🧠 Problem Statement

In ride-sharing systems, multiple users may request rides simultaneously.
Without proper concurrency control, the same cab can be assigned to multiple riders.

This system prevents:

❌ Double cab assignment

❌ Race conditions

❌ Data inconsistency

Using PostgreSQL row-level locks (SELECT FOR UPDATE).

🚀 Tech Stack
Layer	Technology
Backend	FastAPI (Async REST API)
Database	PostgreSQL
ORM	SQLAlchemy 2.0 (Async)
Driver	asyncpg
Concurrency	Row-Level Locks
Language	Python 3.11+
📂 Project Structure
app/
│
├── main.py              # Application entry point
├── database.py          # Async DB configuration
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic request/response schemas
├── dependencies.py      # Dependency injection
│
├── routers/
│   ├── ride.py          # Ride endpoints
│   └── cab.py           # Cab endpoints
│
├── services/
│   ├── pooling.py       # Ride pooling logic
│   └── pricing.py       # Pricing engine
│
└── concurrency.py       # Row-level locking logic

⚙️ Key Features

✅ Async database operations

✅ Cab allocation system

✅ Ride pooling algorithm

✅ Pricing module

✅ Row-level locking for safe transactions

✅ Clean layered architecture (Router → Service → DB)

✅ Auto-generated API documentation

🛠 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔐 Environment Configuration

Create a .env file:

DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname


⚠️ Make sure:

PostgreSQL is running

Database exists

.env is added to .gitignore

▶️ Running the Application
uvicorn app.main:app --reload


Server runs at:

http://127.0.0.1:8000

📖 API Documentation

FastAPI automatically generates interactive docs:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🔒 Concurrency Handling

To prevent race conditions during cab allocation:

Uses PostgreSQL transactions

Applies SELECT ... FOR UPDATE

Locks rows during ride assignment

Ensures atomic operations

This makes the system safe under high concurrent requests.

🏗 Architecture Overview
Client
   ↓
Router Layer (API)
   ↓
Service Layer (Business Logic)
   ↓
Database Layer (Async ORM)
   ↓
PostgreSQL (Row-level Locking)


This separation ensures:

Scalability

Maintainability

Testability

📈 Possible Improvements

JWT Authentication

Role-based access control

Redis caching

Docker support

Alembic migrations

Unit & integration tests

Load testing

