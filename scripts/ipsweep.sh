#!/bin/bash

if [ "$1" == "" ] 
then
	echo "You Forget to put ip as arg"
	echo "Syntax: ./ipsweep.sh 10.0.2"
else
	for ip in `seq 1 254 `; do
		ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
	done
fi

#Comment for understanding
#$1 is input in command line (ie. ./ipsweep.sh <>.<>.<>)

