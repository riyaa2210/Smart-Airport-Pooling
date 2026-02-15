✈️ Smart Airport Pooling – 

📌 Overview-

This project is a backend implementation of a ride pooling system for airport transfers. The system: Accepts ride requests , Matches rides to available cabs , Ensures safe concurrent seat allocation , Calculates dynamic fare , Prevents overbooking using database-level locking , Built as part of a Backend Engineer Internship Assignment.

🏗 System Design-
1)Core Components

Ride Service

Creates ride requests

Stores pickup/drop coordinates

Tracks seat & luggage requirements

Maintains ride status

Cab Service

Registers new cabs

Tracks seat availability

Stores current location

Pooling Engine

Groups pending rides

Matches with nearest available cabs

Uses distance-based filtering

Assigns seats safely

Concurrency Layer

Prevents double booking

Uses row-level locking

Atomic seat updates

Pricing Engine

Calculates fare dynamically

Based on distance

Passenger load factor

Demand multiplier

2) Pooling Algorithm
Strategy: Greedy Assignment

For each available cab:

Find nearby pending rides

Check seat + luggage capacity

Lock cab row

Deduct seats atomically

Assign ride

Distance Calculation

Uses Haversine Formula to calculate distance between cab and pickup location.

3) Concurrency Handling (Important)

To prevent race conditions:

SELECT ... FOR UPDATE is used

Cab rows are locked before seat deduction

Cancellation restores seats safely

No seat overbooking possible

This ensures correctness even under concurrent requests.

4) Pricing Logic

Fare is calculated as:

Fare = Base Fare + (Distance × Rate per km)
Adjusted by:
- Passenger count
- Demand multiplier


Time Complexity: O(1) per ride

5) Algorithm Complexity

Pooling:

O(N × M)
N = pending rides
M = available cabs


Optimized by:

Filtering in database

Async execution

Reduced in-memory iterations

6) Tech Stack

FastAPI (Async REST API)

PostgreSQL

SQLAlchemy 2.0 (Async)

Row-Level Locks

Python 3.11+

📂 Project Structure
app/
 ├── main.py
 ├── database.py
 ├── models.py
 ├── schemas.py
 ├── dependencies.py
 │
 ├── routers/
 │     ├── ride.py
 │     └── cab.py
 │
 ├── services/
 │     ├── pooling.py
 │     ├── pricing.py
 │     └── concurrency.py


🚀 Running the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Set environment variable

Create .env file:

DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname

3️⃣ Run server
uvicorn app.main:app --reload


Access:

API: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

=>Load Testing

A load testing script simulates 200 concurrent ride requests.

python load_test.py


Demonstrates system stability under concurrent traffic.

📈 Future Improvements

Redis caching for cab lookup

Background matcher worker

Docker deployment

Index optimization for geo queries

Horizontal scaling with multiple workers

🎯 Why This Implementation Stands Out-

Handles real-world concurrency issues

Clean modular architecture

Separation of concerns (routing / service / DB)

Async-first design

Production-oriented thinking

