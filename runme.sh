#!/bin/bash


loc=/usr/bin/

if [ ! -e "$loc/base32" ] ; then
	echo "you are missing base32 from your $loc directory"
else
	echo 

fi
########################
if [ ! -e "$loc/base64" ] ; then
	echo "you are missing base64 from your $loc directory"
else
	echo 
fi
########################
if [ ! -e "$loc/perl" ] ; then
	echo "you are missing perl from your $loc directory"
else
	echo 
fi
########################
sudo chmod +x def 
sudo cp -i def /usr/bin 

