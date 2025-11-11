FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY dashboard.py .
COPY get_api.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["streamlit", "run", "dashboard.py", "--server.address=0.0.0.0", "--server.port=8501"]