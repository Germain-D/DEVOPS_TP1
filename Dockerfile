FROM python:3.8-buster

WORKDIR /devops-tp2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

COPY config.py .

EXPOSE 5000

CMD ["python", "config.py"]

CMD ["python", "app.py"]
