# Use an official Python runtime as a parent image (alpine version for minimal size)
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Install ffmpeg and necessary dependencies
RUN apk add --no-cache ffmpeg bash

# Install yt-dlp using pip
RUN pip install --no-cache-dir yt-dlp

# Copy the current directory contents into the container at /app
COPY script.py /app/

# Ensure the Python script has execution permissions
RUN chmod +x /app/script.py

# Set the output directory to /data
ENTRYPOINT ["python", "/app/script.py"]
