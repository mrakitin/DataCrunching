# AutoDockTools Fix

In the Autodock Tools docking parameter file generator the writer
may actually add comments directly following the data. For example,
we have seen ligand type declarations such as
```
ligand_types  A C HD Mg N NA OA P SA W# atoms types in ligand
```
This input is invalid and causes Autodock4 to fail. This failure is
the result of a format error on line 1259 of `DockingParameters.py`
in the function `_make_string`. The format in that line should be
`"%s %s%s # %s\n"` instead of `"%s %s%s# %s\n"`.

To fix this problem, copy the `DockingParameters.py` file provided here
over the one in `MGLToolsPckgs/AutoDockTools/DockingParameters.py`.
