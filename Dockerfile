FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

# Assumes your FastAPI instance is in a file named "main.py" and the app object is named "app".
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

