FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:$PORT/health/ || exit 1

RUN mkdir -p staticfiles

RUN python manage.py collectstatic --noinput

EXPOSE $PORT

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 3 library_project.wsgi:application"]