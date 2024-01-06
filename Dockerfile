FROM python:3.11-slim
COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
CMD py app.py