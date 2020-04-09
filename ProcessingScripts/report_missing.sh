#!/bin/bash
#
# This script takes 2 argument:
#
# - $1 the file with SMILES strings and IDs
# - $2 an optional filename prefix
#
#. /software/anaconda3/etc/profile.d/conda.sh
#conda activate py3
#
# Conversion of SMILES string to MOL2:
#
# - Done one at a time as OpenBabel might crash attempting this
#   and if that happens only 1 molecule is lost this way
#
if [ $# -eq 2 ]
then
  prefix=$2
else
  prefix=""
fi
declare -a fields
num=-1
while IFS= read -r line
do
  ((num++))
  fields=($line)
  smiles=${fields[0]}
  id=${fields[1]}
  if [ -f $prefix$id.dlg ]
  then
    continue
  fi
  if [ -f $prefix$id.dlg.bz2 ]
  then
    continue
  fi
  echo $id
  echo $num > /dev/stderr
done < $1
