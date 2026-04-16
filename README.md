# API Key & Rate Limiting Service

## Project Overview

This project is a backend service built using FastAPI that provides secure API access using API keys and enforces rate limiting on protected endpoints.

Each client is issued a unique API key, which must be used to access protected resources. The system tracks usage and restricts excessive requests based on defined limits.

---

## Features

* Unique API key generation
* Secure access using API key authentication
* Request tracking per API key
* Rate limiting (5 requests per minute)
* Protected API endpoint
* Automatic API documentation (Swagger UI)

---

## Tech Stack

* Framework: FastAPI
* Database: SQLite
* ORM: SQLAlchemy
* Language: Python

---

## Project Structure

```
API-KEY-SERVICE/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   ├── rate_limiter.py
│   ├── schemas.py
│   ├── auth.py
│
├── venv/
├── test.db
├── README.md
```

---

## Installation & Setup

### 1. Clone the Repository

```
git clone <your-repo-link>
cd api-key-service
```

### 2. Install Dependencies

```
pip install fastapi uvicorn sqlalchemy
```

### 3. Run the Application

```
python -m uvicorn app.main:app
```

---

## API Documentation

Once the server is running, open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. Generate API Key

* Method: POST
* Endpoint: `/generate-key`

#### Response Example

```
{
  "id": 1,
  "key": "abc123xyz...",
  "created_at": "2026-04-16T12:00:00"
}
```

---

### 2. Access Protected API

* Method: GET
* Endpoint: `/protected`

#### Required Header

```
x-api-key: YOUR_API_KEY
```

#### Success Response

```
{
  "message": "Access granted"
}
```

#### Error Responses

Invalid API Key:

```
{
  "detail": "Invalid API Key"
}
```

Rate Limit Exceeded:

```
{
  "detail": "Rate limit exceeded"
}
```

---

## Rate Limiting

* Limit: 5 requests per minute per API key
* Implemented using in-memory tracking

---

## Test Cases

### 1. Generate API Key

* Request: POST /generate-key
* Expected: New API key is created and returned

---

### 2. Access Protected API with Valid Key

* Request: GET /protected with valid `x-api-key`
* Expected: Access granted

---

### 3. Access Protected API without API Key

* Request: GET /protected without header
* Expected: 422 validation error (missing header)

---

### 4. Access Protected API with Invalid API Key

* Request: GET /protected with wrong key
* Expected: 403 Invalid API Key

---

### 5. Rate Limiting Test

* Request: Call `/protected` more than 5 times within a minute
* Expected: 429 Rate limit exceeded

---

### 6. Rate Limit Reset

* Wait for 60 seconds after hitting limit
* Call again
* Expected: Requests allowed again

---

## Testing with Postman

1. POST `/generate-key`
2. Copy API key
3. GET `/protected`
4. Add header:

```
x-api-key: YOUR_API_KEY
```

---

## Future Improvements

* Redis-based rate limiting
* API key expiration
* Logging and monitoring
* Docker support
