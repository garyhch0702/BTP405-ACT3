# Use Python 3.8 as the base image, adjust if you're using a different version
FROM python:3.8-slim

# Set the working directory in the Docker image
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install mysql-connector-python to allow your app to connect to MySQL
RUN pip install mysql-connector-python

# Expose the port the app runs on
EXPOSE 8080

# Run the Python server
CMD ["python", "my_api_server.py"]
