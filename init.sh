#!/bin/bash

#Check if pip is installed
pipExist=$(which pip)
if [ -z "$pipExist" ]
then
	echo "Pip is not installed"
else
	echo -e "Pip is already installed: \n"
	pip --version
fi

packagesExists=$( pip list | grep 'Flask\|requests' )
if [ -z "$packagesExists" ]
then
	echo -e "\nPackages are not installed"
else
	echo -e "\nPackages are already installed:\n"
	echo -e "$packagesExists \n"
fi
# Check if request and flask already installed
#pip list | grep -F requests flask

# If not install
#sudo pip install request flask

# Run app.py qith flask command
#flask run
