# Dockerfile for core_service.py

# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the core application files to the container
COPY core_service.py requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the core application listens on
EXPOSE 8080

# Run the core application when the container starts
CMD ["python", "core_service.py"]
