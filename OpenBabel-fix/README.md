# OpenBabel 3.0.0 Fix

OpenBabel can be used to transform SMILES strings to 3D structures stored in
MOL2 files. The algorithm to do so exploits rigid fragments to speed up the
conversion process. However, some of the rigid fragments stored in its tables
have invalid atomic coordinates (see
https://github.com/openbabel/openbabel/issues/2144 for details). Hence, we need
to replace the files:

- rigid-fragments.txt
- rigid-fragments-index.txt

to avoid generating bad structures, at least until this problem has been fixed.

Also note that a convenient way of installing OpenBabel is as a conda package:
```
conda install -c nsls2forge -c conda-forge openbabel
```
