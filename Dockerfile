FROM python:3-slim-buster

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY src .

CMD ["python", "main.py"]
