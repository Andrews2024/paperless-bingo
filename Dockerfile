# syntax=docker/dockerfile:1
# Python image
FROM python:3.12-alpine

# Destination for copy
WORKDIR /app

# Copy whole directory
COPY . ./

# Install flask and related dependencies
RUN pip3 install -r requirements.txt

# Run Flask app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]