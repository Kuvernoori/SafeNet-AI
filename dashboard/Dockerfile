FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --default-timeout=100 streamlit==1.32.0 requests==2.31.0


EXPOSE 8501


CMD ["streamlit", "run", "Dashboard_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
