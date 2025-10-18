# 1. Use official Python image
FROM python:3.10-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set work directory
WORKDIR /app

# 4. Install system dependencies (if needed for Pillow, psycopg2, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy requirements first (for caching)
COPY requirements.txt /app/

# 6. Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 7. Copy project files
COPY . /app/

# 8. Collect static files (important!)
RUN python manage.py collectstatic --noinput || true

# 9. Expose port
EXPOSE 8000

# 10. Run the app with Gunicorn (better than runserver in production)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "healthcare_management.wsgi:application"]

