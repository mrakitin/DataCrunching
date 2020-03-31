#!/bin/bash
mkdir example01
cd example01
cp ../ena+db-small.can .
cp ../3CLPro_protein.pdb .
../prepare_target.sh 3CLPro_protein '54,52,60' '-10.520,-2.322,-20.631'
../smiles_to_mol2.sh ena+db-small.can
../mol2_to_pdbqt.sh  ena+db-small.can
../smiles_dock.sh    3CLPro_protein ena+db-small.can 
cd ..
./summarize.sh example01
