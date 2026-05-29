FROM python:3.11-slim

WORKDIR /app

COPY test.py /app

RUN pip install fastapi uvicorn

EXPOSE 9000

CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "9000"]

