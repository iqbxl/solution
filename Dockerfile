# FROM arm64v8/python:3
FROM python:3

# Set the working directory to the app directory
WORKDIR /app

# Copy files from host system into Docker container
COPY . .

# Run the Python file when the container starts
CMD python ./Island.py $FILE