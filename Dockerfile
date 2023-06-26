# Base image
FROM adoptopenjdk:8-jdk-hotspot

# Set working directory
WORKDIR /

# Install Python and required dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

# Copy and install Python package requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the Python package code to the container
COPY . .

# Expose the port on which your application runs (adjust if needed)
EXPOSE 8000

# Command to start the application
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000", "--workers", "4"]
