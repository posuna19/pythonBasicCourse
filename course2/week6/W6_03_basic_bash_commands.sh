#!/bin/bash
line="-------------------------------"
echo "*******************************"
echo "Starting at: $(date)"
echo

echo "UPTIME"; uptime; echo $line

echo "FREE"
free
echo $line

echo "WHO"
who
echo $line

echo "Finishing at: $(date)"
echo "*******************************"
