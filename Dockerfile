# Use python 3.12 for base image
FROM python:3.12

# For logging to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set working directory to /hobbysite
WORKDIR /hobbysite

# Copy all files to working directory
COPY . .

# install requirements for app
RUN pip install -r requirements.txt

# Initial setup for django app
RUN python manage.py migrate
RUN python manage.py collectstatic

# Create initial superuser with .env variables
RUN --mount=type=secret,id=env,target=./.env \ 
    python manage.py createsuperuser --username=admin --email=admin@example.com --no-input

# Expose port 8000 for the Django application
EXPOSE 8080

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]