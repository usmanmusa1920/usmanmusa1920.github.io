#!/bin/sh

# Exit script if any command fails
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn server
echo "Starting Gunicorn..."
exec gunicorn --bind 0.0.0.0:8000 usmanmusa.wsgi:application
