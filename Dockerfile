# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
 && pip install streamlit pandas matplotlib

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
