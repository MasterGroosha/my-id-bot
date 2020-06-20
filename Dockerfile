FROM python:3.8-slim-buster
RUN apt update && apt install -y gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY bot.py /bot.py
COPY logs.py /logs.py
RUN mkdir /logs
CMD ["python", "bot.py"]
