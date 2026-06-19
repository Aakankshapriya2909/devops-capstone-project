# Use an official lightweight Python runtime
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy and install dependencies first (leverages Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080 for the Flask application
EXPOSE 8080

# Switch to a non-root user for security compliance
RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
USER appuser

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "service:app"]
