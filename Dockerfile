# Use an official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy files into the container
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
