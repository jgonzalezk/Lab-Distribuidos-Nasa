FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY productor.py .

CMD ["python", "productor.py"]
#docker build . -t producer
#docker run --network="host"  producer

