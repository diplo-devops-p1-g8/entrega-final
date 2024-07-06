FROM python:3.10-slim

WORKDIR /app

# Install Python dependencies
RUN pip3 install flask

# Copy the rest of the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]