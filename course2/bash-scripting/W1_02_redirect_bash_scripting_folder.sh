#!/bin/bash

# In the '/bin' folder must be a file called 'polba' which stands for POL bash directory and it is just a bash script
# that executes this file with the following command:
# . /mnt/d/Projects/pythonBasicCourse/course2/bash-scripting/W1_02_redirect_bash_scripting_folder.sh
# and what it does is just to change the current directory to the 'bash-scripting' folder. 
# NOTE: it must starts with the '.' or 'source' command in order to actualy work

echo "This bash script can be called using the command '. polba' or 'source polba'"

cd /mnt/d/Projects/pythonBasicCourse/course2/bash-scripting

ls -la

pwd
