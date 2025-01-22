# Use an official lightweight Python base image
FROM python:3.11-slim

# Create a working directory in the container
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt ./

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your code
COPY . .

# By default, run your tests
CMD ["pytest"]
