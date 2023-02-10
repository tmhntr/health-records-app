# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app /app

VOLUME ./app:/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--root-path", "/api/v1", "--reload"]