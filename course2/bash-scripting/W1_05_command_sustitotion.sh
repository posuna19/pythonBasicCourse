#!/bin/bash

echo "Command substitution allows us to take the output of a command or program (what would normally be printed to the screen)" 
echo "and save it as the value of a variable"
echo 'You use the dollar sign and the parenthesis as follow: =$(ls)'
files=$(ls)
echo "Files: $files"

