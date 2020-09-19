#!/bin/bash

if grep "127.0.0.1" ./etc/host/hosts.txt; then
	echo "Everything OK"
else
	echo "Error! 127.0.0.1 is not in /etc/host"
fi

