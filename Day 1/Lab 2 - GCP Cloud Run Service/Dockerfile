# Start with a base image that has Python 3.12 installed
# 'slim' version is smaller and contains only essential components
FROM python:3.12-slim

# Set the working directory inside the container to /app
# All subsequent commands will run from this directory
WORKDIR /app

# Copy the requirements file first (before copying code)
# This allows Docker to cache the dependency installation step
# If only code changes, dependencies don't need to be reinstalled
COPY requirements.txt .

# Install Python dependencies inside the container
# This ensures the same versions work everywhere
RUN pip install -r requirements.txt

# Copy the main application code into the container
# This is done after installing dependencies for better caching
COPY main.py .

# Define the command to run when the container starts
# gunicorn is a production-ready web server (better than Flask's built-in server)
# --bind :8080 means listen on port 8080
# --workers 1 means use 1 worker process
# --threads 2 means each worker can handle 2 requests simultaneously
# main:app refers to the 'app' variable in the 'main.py' file
CMD exec gunicorn --bind :8080 --workers 1 --threads 2 main:app