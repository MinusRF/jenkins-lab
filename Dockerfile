# Start with a Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (we'll explain why in a moment)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Tell Docker the app listens on port 5000
EXPOSE 5000

# Command to run when container starts
CMD ["python3", "app.py"]
