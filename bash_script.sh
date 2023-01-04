#!/bin/bash

# Build Docker image
docker build -t islands_image .

# Run Docker image
docker run -it --rm islands_image