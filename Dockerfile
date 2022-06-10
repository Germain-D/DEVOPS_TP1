
FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV PYTHONPATH "${PYTHONPATH}:/app"

ENV PYTHONUNBUFFERED 1

CMD ["python", "app.py"]
