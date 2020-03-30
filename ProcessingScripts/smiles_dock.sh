#!/bin/bash
#
# This script takes 3 argument:
#
# - $1 the protein (in pdbqt format)
# - $2 the name of the file containing SMILES strings to process.
# - $3 the flexible residues (in pdb format) [optional]
#
#. /software/anaconda3/etc/profile.d/conda.sh
#conda activate py3
#
# Conversion of SMILES string to MOL2:
#
# - Done one at a time as OpenBabel might crash attempting this
#   and if that happens only 1 molecule is lost this way
#
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
  mkdir $id
  cp $1 $id
  if [[ $# -eq 3 ]]
  then
    cp $3 $id
  fi
  cd $id
  echo "$smiles" | obabel -h --gen3d -ismi -omol2 > $id.mol2
  pythonsh ../Utilities24/prepare_ligand4.py -l $id.mol2  -o $id.pdbqt
  if [[ $# -eq 2 ]]
  then
    pythonsh ../Utilities24/prepare_gpf4.py  -l $id.pdbqt -r $1 -p npts="54,52,60" -p gridcenter="-10.520,-12.322,-20.631" -o $id.gpf
    pythonsh ../Utilities24/prepare_dpf42.py -l $id.pdbqt -r $1 -o $id.dpf
  elif [[ $# -eq 3 ]]
  then
    pythonsh ../Utilities24/prepare_gpf4.py  -l $id.pdbqt -r $1 -x $3 -p npts="54,52,60" -p gridcenter="-10.520,-12.322,-20.631" -o $id.gpf
    pythonsh ../Utilities24/prepare_dpf42.py -l $id.pdbqt -r $1 -x $3 -o $id.dpf
  else
    echo "invalid number of arguments $#"
    echo "should be 2 or 3"
    exit 1
  fi
  autogrid4 -p $id.gpf -l $id.glg
  autodock4.omp -p $id.dpf -l $id.dlg
  mv $id.dlg ..
  cd ..
  rm -rf $id
done < $2
