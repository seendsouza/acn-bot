FROM python:3.6
WORKDIR /app
CMD cd /app
COPY ./src /app
RUN pip3 install discord.py --user
CMD ["python", "main.py"]
