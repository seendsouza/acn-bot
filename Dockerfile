FROM python:3.6
WORKDIR /app
CMD cd /app
COPY ./src /app
RUN pip install discord
CMD ["python", "main.py"]
