FROM python:3.9


# Move file to working directory and start program
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main_handler.py .
COPY crawling.py .

COPY start.sh .

RUN chmod +x start.sh

# Start web crawling
CMD ["./start.sh"]
