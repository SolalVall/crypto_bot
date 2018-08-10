#!/bin/bash
pipExist=$(which pip)
packagesExists=$( pip list | grep 'Flask\|requests' )

#Check if pip is installed
if [ -z "$pipExist" ]
then
	echo "Pip is not installed\n"
	echo -e "Download get-pip script:"
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	python get-pip.py
else
	echo -e "Pip is already installed: \n"
	pip --version
fi

#Check if necessary packages are installed
if [ -z "$packagesExists" ]
then
	echo -e "\nPackages are not installed"
	pip install Flask, requests
else
	echo -e "\nPackages are already installed:\n"
	echo -e "$packagesExists \n"
fi

# Run app.py with flask command
flask run
