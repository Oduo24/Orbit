# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate a virtual environment
RUN python3 -m venv venv
RUN . venv/bin/activate

# Install the required packages within the virtual environment
RUN pip install -r requirements.txt

# Expose port 5001 for the Flask application
EXPOSE 5001

# Define the command to run your application
CMD ["venv/bin/python3", "./app.py"]

