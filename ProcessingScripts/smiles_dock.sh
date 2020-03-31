#!/bin/bash
#
# This script takes 5 argument:
#
# - $1 the protein (in pdbqt format)
# - $2 the name of the file containing SMILES strings to process.
# - $3 the pocket center given as "xcoord,ycoord,zcoord"
# - $4 the number grid points given as "nptsx,nptsy,nptsz"
# - $5 the flexible residues (in pdb format) [optional]
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
  cp $1.pdbqt $id
  if [[ $# -eq 5 ]]
  then
    cp $5.pdb $id
  fi
  cd $id
  echo "$smiles" | obabel -h --gen3d -ismi -omol2 > $id.mol2
  pythonsh ../Utilities24/prepare_ligand4.py -l $id.mol2  -o $id.pdbqt
  if [[ $# -eq 4 ]]
  then
    pythonsh ../Utilities24/prepare_gpf4.py  -l $id.pdbqt -r $1.pdbqt -p npts="$4" -p gridcenter="$3" -o $id.gpf
    pythonsh ../Utilities24/prepare_dpf42.py -l $id.pdbqt -r $1.pdbqt -o $id.dpf
  elif [[ $# -eq 5 ]]
  then
    pythonsh ../Utilities24/prepare_gpf4.py  -l $id.pdbqt -r $1.pdbqt -x $5.pdb -p npts="$4" -p gridcenter="$3" -o $id.gpf
    pythonsh ../Utilities24/prepare_dpf42.py -l $id.pdbqt -r $1.pdbqt -x $5.pdb -o $id.dpf
  else
    echo "invalid number of arguments $#"
    echo "should be 4 or 5"
    exit 1
  fi
  autogrid4 -p $id.gpf -l $id.glg
  for it in `seq 1 3`
  do
    echo "autodock4.omp -p $id.dpf -l $id.$it.dlg"
    autodock4.omp -p $id.dpf -l $id.$it.dlg
  done 
  cd ..
done < $2
