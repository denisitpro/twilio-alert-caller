# Use Python base image
FROM python:3.12-slim

# Install necessary dependencies
RUN pip install flask twilio

# Copy the application code
COPY caller-twilio.py /app/caller-twilio.py

# Set working directory
WORKDIR /app

# Set environment variable for Flask app
ENV FLASK_APP=caller-twilio.py

# Expose the port (default is 5000)
EXPOSE 5000

# Command to run the application
CMD ["python", "caller-twilio.py"]