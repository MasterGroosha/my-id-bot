FROM python:3.8-slim-buster
WORKDIR /app
RUN mkdir /app/logs
COPY start.sh /app/
RUN chmod +x /app/start.sh
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt
COPY *.py /app/
CMD ["/app/start.sh"]
