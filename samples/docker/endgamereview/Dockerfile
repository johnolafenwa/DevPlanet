FROM python:3.6-slim

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3","app.py"]
