# E-Commerce Platform & REST API

A backend e-commerce system built with **Python**, **Django**, and **Django REST Framework (DRF)**, featuring a RESTful API, asynchronous background tasks with **Celery**, caching with **Redis**, **MySQL** persistence, **Stripe** payments with Webhooks, and **Docker** deployment on **Render**[cite: 4, 10, 12, 15].

## Live Deployment & API Docs
- **Base URL:** `https://ecommerce-api-siw5.onrender.com`[cite: 4]
- **Swagger UI:** `https://ecommerce-api-siw5.onrender.com/api/docs/swagger/`[cite: 4]

## Key Features
- **Authentication & Role-Based Permissions:** JWT authentication (`access` and `refresh` tokens)[cite: 4], custom user & address models[cite: 1, 15], and admin-restricted write access (`403 Forbidden` for non-admin users) on products and categories[cite: 14].
- **Catalog & Filtering:** Category and product endpoints supporting filtering, search, ordering, and response caching[cite: 11].
- **Cart & Orders:** Cart and order management endpoints with Stripe payment session initiation (`/api/v1/orders/{order_id}/pay/`) and Webhook handling (`/api/v1/orders/webhook/`) to mark paid orders and update order status automatically[cite: 11, 12, 15].
- **Redis Caching & Celery Tasks:** Uses Redis for caching/broker alongside Celery workers for asynchronous background tasks (such as order confirmation notifications)[cite: 15].
- **Interactive API Documentation:** OpenAPI schema & Swagger UI exposed for testing endpoints[cite: 4, 11, 15].
- **Containerized & Deployed:** Dockerized application deployed on Render with external MySQL and Redis services[cite: 4, 15].

## Tech Stack
- **Backend:** Python, Django, Django REST Framework (DRF)[cite: 15]
- **Database:** MySQL[cite: 15]
- **Cache & Broker:** Redis[cite: 15]
- **Task Queue:** Celery[cite: 15]
- **Payments:** Stripe API & Webhooks[cite: 10]
- **Dependency Management:** Pipenv (`Pipfile` / `Pipfile.lock`)[cite: 15]
- **Documentation:** `drf-spectacular` (Swagger UI)[cite: 4, 15]
- **Containerization & Hosting:** Docker, Render[cite: 4, 15]

## Environment Variables
Configure the required environment variables in your local `.env` file and in your hosting platform (e.g., Render):
- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- MySQL database connection variables
- Redis / Celery broker & cache connection URLs
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`[cite: 7]
- `STRIPE_SUCCESS_URL` (e.g., `https://ecommerce-api-siw5.onrender.com/api/docs/swagger/`)[cite: 4, 6]
- `STRIPE_CANCEL_URL` (e.g., `https://ecommerce-api-siw5.onrender.com/api/docs/swagger/`)[cite: 4, 6]

## Running Locally
1. Clone the repository and install dependencies using `pipenv install --dev` (or run via Docker)[cite: 15].
2. Configure your `.env` file with database, Redis, and Stripe variables[cite: 7, 15].
3. Run migrations and start the development server / worker:
   ```bash
   python manage.py migrate
   python manage.py runserver