#!/bin/bash
pipExist=$(which pip)
packagesExists=$( pip list | grep 'Flask\|requests' )

echo -e "\n------------------------CHECK NECESSARY PACKAGES--------------------------\n"

#Check if pip is installed
if [ -z "$pipExist" ]
then
	echo "Pip is not installed\n"
	echo -e "Download get-pip script:"
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python get-pip.py
	rm get-pip.py
else
	echo -e "Pip is already installed: \n"
	pip --version
fi

#Check if necessary packages are installed
if [ -z "$packagesExists" ]
then
	echo -e "\nPackages are not installed"
	sudo pip install Flask requests
else
	echo -e "\nPackages are already installed:\n"
	echo -e "$packagesExists \n"
fi

# Run app.py with flask command
echo -e "\n--------------------------------START APP---------------------------------\n"
flask run
