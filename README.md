# 🚖 Async Ride Pooling Backend System

A high-performance Ride Pooling Backend built using **FastAPI (Async)** and **PostgreSQL**, designed to handle concurrent ride allocation safely using row-level locking.

---

## 🚀 Tech Stack

| Layer        | Technology                     |
|-------------|--------------------------------|
| Backend      | FastAPI (Async REST API)       |
| Database     | PostgreSQL                     |
| ORM          | SQLAlchemy 2.0 (Async)         |
| Driver       | asyncpg                        |
| Concurrency  | Row-Level Locks                |
| Language     | Python 3.11+                   |

---

## 📂 Project Structure

```
app/
├── main.py              # Application entry point
├── database.py          # Async database configuration
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
│   └── pricing.py       # Pricing engine
│
└── concurrency.py       # Row-level locking logic
```

---

## ⚙️ Key Features

- Async database operations  
- Cab allocation system  
- Ride pooling logic  
- Pricing module  
- Row-level locking using `SELECT FOR UPDATE`  
- Clean layered architecture (Router → Service → Database)  
- Auto-generated API documentation  

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
```

Make sure:
- PostgreSQL is running  
- Database exists  
- `.env` is added to `.gitignore`  

---

## ▶️ Run the Server

```bash
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

### Swagger UI
```
http://127.0.0.1:8000/docs
```

### ReDoc
```
http://127.0.0.1:8000/redoc
```

---

## 🔒 Concurrency Handling

To prevent race conditions:

- Uses database transactions  
- Applies row-level locking  
- Ensures atomic cab allocation  
- Prevents double ride assignment  

---

## 👩‍💻 Author

Riya Ransing  
Computer Science Student | Backend Developer
