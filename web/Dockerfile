# Use python 3.12 for base image
FROM python:3.12-slim

# For logging to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set working directory to /hobbysite
WORKDIR /hobbysite

# Copy all files to working directory
COPY . .

# install requirements for app
RUN python -m venv /opt/venv

# Initial setup for django app
RUN /opt/venv/bin/pip install -r requirements.txt
RUN chmod +x entrypoint.sh

# Run the Django development server
CMD ["/hobbysite/entrypoint.sh"]