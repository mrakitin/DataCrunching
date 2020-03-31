#!/bin/bash
#
# This script takes 3 argument:
#
# - $1 the protein (in pdbqt format)
# - $2 the name of the file containing SMILES strings to process.
#
#. /software/anaconda3/etc/profile.d/conda.sh
#conda activate py3
#
# Conversion of SMILES string to MOL2:
#
# - Done one at a time as OpenBabel might crash attempting this
#   and if that happens only 1 molecule is lost this way
#
receptor=$1
declare -a fields
while IFS= read -r line
do
  fields=($line)
  smiles=${fields[0]}
  id=${fields[1]}
  if [ -f $id.dlg ]
  then
    continue
  fi
  pythonsh $AUTODOCKTOOLS_UTIL/prepare_dpf42.py -l $id.pdbqt -r $receptor.pdbqt -o $id.dpf
  autodock4 -p $id.dpf -l $id.dlg
done < $2
