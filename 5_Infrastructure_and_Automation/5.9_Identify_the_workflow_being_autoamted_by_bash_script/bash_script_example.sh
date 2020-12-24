#! /bin/bash

# ECHO Commands
#echo Hello World!

# VARIABLES
# Upper case by convension
# Letters, numers and underscores
NAME="Brad"
# echo "My Name is ${NAME}"

# USER INPUT
# read -p "Enter you name: " NAME
# echo "Hello ${NAME}, nice to meet you!"

# IF-ELSE STATEMENT
if [ "${NAME}" == James ]
then
    echo "Your name is ${NAME}"
else
    echo " Your name is not James"
fi