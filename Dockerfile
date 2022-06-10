
FROM python:3.8-buster

WORKDIR /devops-tp2

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]