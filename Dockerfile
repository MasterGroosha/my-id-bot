FROM python:3.8-slim-buster
WORKDIR /app
RUN mkdir /logs
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY *.py /app/
CMD ["python", "bot.py"]
