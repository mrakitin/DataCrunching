#!/bin/bash
#
# This script takes 1 argument:
#
# - $1 the name of the file containing SMILES strings to process.
#
# The file of SMILES strings contains a number of lines each of which contains:
#
# - A SMILES string
# - An identifier
# - Other data fields
#
# We extract the SMILES string to process, and use the identifier to generate
# unique filenames.
#
declare -a fields
while IFS= read -r line
do
  fields=( $line )
  smiles=${fields[0]}
  id=${fields[1]}
  echo "$smiles" | obabel -h --gen3d -ismi -omol2 >> $id.mol2 2> /dev/null
done < $1
