# Use a small official Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency list first (better Docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app.py .

# Expose the Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
