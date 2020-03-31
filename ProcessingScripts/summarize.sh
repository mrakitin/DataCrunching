#!/bin/bash
#
# - $1 the file with SMILES strings to process
#
declare -a fields
while IFS= read -r line
do
  fields=($line)
  id=${fields[1]}
  pythonsh $AUTODOCKTOOLS_UTIL/summarize_results4.py -b -d $id -a -o summary.txt
done < $1
