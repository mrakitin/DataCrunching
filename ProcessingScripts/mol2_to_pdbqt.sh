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
# We extract the identifiers to generate unique filenames to process.
#
if [[ ${#AUTODOCKTOOLS_UTIL} -eq 0 ]]
then
  echo "Set environment variable AUTODOCKTOOLS_UTIL to the absolute path of the Utilities24 directory"
  exit 1
fi
pythonsh=`which pythonsh`
if [[ ${#pythonsh} -eq 0 ]]
then
  echo "Make sure the pythonsh executable is in your PATH"
  exit 2
fi
declare -a fields
while IFS= read -r line
do
  fields=( $line )
  id=${fields[1]}
  # Note: prepare_ligand.py and prepare_ligand4.py produce different PDBQT formats.
  pythonsh $AUTODOCKTOOLS_UTIL/prepare_ligand4.py -l $id.mol2  -o $id.pdbqt
done < $1
