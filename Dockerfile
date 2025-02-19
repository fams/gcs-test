# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app/requirements.txt
# Install any needed packages specified in requirements.txt
RUN pip config --user set global.progress_bar off
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY ./run.py /app/run.py
COPY ./gcs /app/gcs

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=run.py
# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
