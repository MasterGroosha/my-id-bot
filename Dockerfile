FROM python:3.8-slim-buster
COPY requirements.txt /requirements.txt
COPY bot.py /bot.py
RUN apt update && apt install -y gcc && rm -rf /var/lib/apt/lists/*
RUN pip install -r /requirements.txt
CMD ["python", "bot.py"]
