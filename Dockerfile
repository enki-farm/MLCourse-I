# Use an official Python image as the base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Jupyter Lab
RUN pip install --no-cache-dir jupyterlab

# Install additional Python packages
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
# Clean up
RUN rm /tmp/requirements.txt

# Expose the default Jupyter Lab port
EXPOSE 8888

# Set the working directory
WORKDIR /workspace

# Start Jupyter Lab without a password and allow access from any IP
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]