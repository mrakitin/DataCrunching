#!/bin/bash
#
# This script takes 3 argument:
#
# - $1 the protein (in pdb format)
# - $2 the number of grid points as "nptsx,nptsy,nptsz"
# - $3 the gridcenter as "xcoord,ycoord,zcoord"
#
#. /software/anaconda3/etc/profile.d/conda.sh
#conda activate py3
#
# We are going to run through very large molecule sets. The best 
# approach is to assume that every atom type will show up somewhere
# (much better than trying to scan millions of files for all atom types).
#
lt="H,HD,HS,C,A,N,NA,NS,OA,OS,F,Mg,MG,P,SA,S,Cl,CL,Ca,CA,Mn,MN,Fe,FE,Zn,ZN,Br,BR,I,Z,G,GA,J,Q"
#
# Also prepare_gpf4.py expects a ligand and a receptor, but the grid
# parameter file will the same for all ligands. So we use the receptor
# as a fake ligand.
#
pythonsh $AUTODOCKTOOLS_UTIL/prepare_receptor4.py -A checkhydrogens -r $1.pdb -o $1.pdbqt
pythonsh $AUTODOCKTOOLS_UTIL/prepare_gpf4.py      -l $1.pdbqt -r $1.pdbqt -o $1.gpf \
                                                  -p npts="$npts" \
                                                  -p gridcenter="$gridcenter" \
                                                  -p ligand_types="$lt"
autogrid4 -p $1.gpf -l $id.glg
