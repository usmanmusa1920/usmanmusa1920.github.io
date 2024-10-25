# Use the official Python image from DockerHub
FROM python:3.10-slim

# Add metadata using LABEL
LABEL name="Usman Site"
LABEL version="0.0.1"
LABEL description="Usman Musa decorized django website."
LABEL maintainer="Usman Musa"

# Set environment variables to prevent writing bytecode and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Create and activate a virtual environment in /opt/venv
RUN python -m venv /opt/venv

# Ensure the virtual environment's bin directory is in the PATH
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies into the virtual environment
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy the entire project into the container
COPY . /app/

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Set the entrypoint to the shell script
ENTRYPOINT ["/app/entrypoint.sh"]
