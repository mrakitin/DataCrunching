#!/bin/bash

./prepare_target.sh 3CLPro_protein
./smiles_dock.sh    3CLPro_protein ena+db-small.can '-10.520,-2.322,-20.631' '54,52,60'
./summarize.sh      ena+db-small.can
