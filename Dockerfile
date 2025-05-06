FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -e .

EXPOSE 80

# Default to running the web server
CMD ["python", "-m", "demo", "server", "--port", "80"]