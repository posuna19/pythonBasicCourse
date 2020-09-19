#!/bin/bash

csv_name=$1
html_name=$2

echo "The CSV base name is: $csv_name"
echo "The HTML base name is $html_name"

./W7_count_error_types_report1.py $csv_name

csv_full_name="${csv_name}_error_types.csv"
html_full_name="${html_name}_errors_by_users.html"

if [ -e ./$csv_full_name ]; then
  echo "File exist! call python escript to generate files"
else
  echo "Error:  file $csv_full_name does not exist"
fi


