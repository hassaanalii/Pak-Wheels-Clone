# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Add the rest of the code
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --no-input

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Start gunicorn with 0.0.0.0:8000
CMD ["gunicorn", "--config", "gunicorn_config.py", "pakwheelsclone.wsgi:application"]
