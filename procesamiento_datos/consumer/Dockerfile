FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY consumer.py .
COPY .env .

CMD ["python", "consumer.py"]
#docker build . -t consumer
#docker run --network="host"  consumer