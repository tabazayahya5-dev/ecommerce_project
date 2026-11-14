# E-Commerce Platform & REST API

A scalable, production-ready E-Commerce backend built with Python, Django, and Django REST Framework (DRF). Originally developed using server-rendered Django Templates, the architecture has been expanded into a hybrid system featuring a decoupled Headless RESTful API, asynchronous background tasks, Redis caching, and complete Docker containerization.

## Key Features
- **Hybrid Architecture:** Supports both traditional server-rendered views (Django Templates) and a full-featured RESTful API.
- **Authentication & Profiles:** Secure JWT-based authentication alongside custom user models and address management endpoints.
- **Cart & Atomic Checkout:** Modular Cart and CartItem APIs with automatic total calculation, stock validation, inventory deduction, and atomic database transactions.
- **Redis Caching:** Speeds up product responses and reduces database load with automated cache invalidation signals.
- **Celery Background Tasks:** Sends order confirmation emails via Gmail SMTP asynchronously without blocking client requests.
- **Interactive API Documentation:** Auto-generated OpenAPI documentation accessible via Swagger UI and ReDoc.
- **Docker Containerization:** Runs the entire multi-service environment easily with a single command.

## Tech Stack
- **Backend:** Python 3.13, Django, Django REST Framework (DRF)
- **Database:** MySQL
- **Cache & Broker:** Redis (`django-redis`)
- **Task Queue:** Celery
- **Dependency Management:** Pipenv
- **Documentation:** `drf-spectacular` (Swagger / ReDoc)
- **Containerization:** Docker, Docker Compose

## How to Run (Docker)
1. Clone the repository and navigate to the project folder.
2. Build and start the containers:
   ```bash
   docker compose up --build
   ```
3. Access the application and interactive documentation:
   - **Web App / API Root:** http://127.0.0.1:8000/
   - **Swagger Docs:** http://127.0.0.1:8000/api/schema/swagger-ui/
   - **ReDoc Docs:** http://127.0.0.1:8000/api/schema/redoc/

## Running Tests
To execute the unit and API test suite inside the container:
```bash
docker compose exec web python manage.py test
```