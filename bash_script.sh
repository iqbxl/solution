#!/bin/bash

# Check if the number of arguments is not equal to the expected number
if [ $# -ne 1 ]; then
err_msg="Usage: ./bash_script.sh INPUT_FILE\nAcceptable usage example: ./bash_script.sh islands.txt"
  echo -e $err_msg
  exit 1
fi

# Get input file name from the first argument
input_file=$1

# Build Docker image
docker build -qt islands_image .

# Run Docker image
docker run -it \
-e FILE=$input_file \
--rm islands_image