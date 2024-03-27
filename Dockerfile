# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the requirements first to leverage Docker cache
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Run server.py when the container launches
CMD ["python", "main.py"]
