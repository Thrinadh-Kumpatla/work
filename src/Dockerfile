# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY src/requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY src/print_timestamp.py .

# Expose the port on which the Flask app will run
EXPOSE 5001

# Define the command to run your Flask app
CMD ["python", "print_timestamp.py"]
