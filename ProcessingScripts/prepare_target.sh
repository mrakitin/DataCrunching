#!/bin/bash
#
# This script takes 1 argument:
#
# - $1 the protein (in pdb format)
#
#. /software/anaconda3/etc/profile.d/conda.sh
#conda activate py3
#
pythonsh $AUTODOCKTOOLS_UTIL/prepare_receptor4.py -A checkhydrogens -r $1.pdb -o $1.pdbqt
