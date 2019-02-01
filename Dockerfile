# Our base image
FROM python:alpine
# Lets work out of /usr/src/app in the container
WORKDIR /usr/src/app
# Copy requirements first
COPY requirements.txt .
# Install Python modules needed by the Python app
RUN pip install --no-cache-dir -r requirements.txt
# The port number the container should expose
EXPOSE 80
# Run the application
CMD ["python", "./app.py"]
# Copy the the app
COPY app.py .
