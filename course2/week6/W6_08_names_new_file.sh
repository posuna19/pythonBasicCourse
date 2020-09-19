echo "Original file: "
cat W6_08_names.txt
echo  ""
echo "Sorted file:"
sort -o W6_08_names_sorted.txt W6_08_names.txt
if [ -e ./W6_08_names_sorted.txt ]; then
	cat W6_08_names_sorted.txt
	echo "*** New File created OK ***"
else
	echo "Error creating the sorted file"
fi
