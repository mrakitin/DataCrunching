# Nsp10_pockets

The three main files are:

- Nsp10_Nsp16_CX_inPDB_out.pdb: Contains the protein structure plus the 
  positions of the `fpocket` spheres to identify the pocket locations
- Nsp10_Nsp16_CX_inPDB_info.txt: Contains summary information on every pocket
  identified by `fpocket`
- Nsp10_Nsp16_CX_inPDB_pockets.pqr: Contains the `fpocket` spheres for every
  pocket, giving both the position and radius of the spheres.

Actually the main PDB file contains two protein structures that form a dimer.
Chain A is the Nsp10 protein, whereas chain B is Nsp16. The pockets listed
here are all close to the Nsp10 and hence we discard Nsp16.

The information from `Nsp10_Nsp16_CX_inPDB_info.txt` can be used to select
promising pockets to target. The information from 
`Nsp10_Nsp16_CX_inPDB_pockets.pqr` for each pocket can be used to define the
box that contains the pocket. From `Nsp10_Nsp16_CX_inPDB_out.pdb` we can
extract the structure of just the Nsp10 protein.

- Nsp10.pdb: was created from `Nsp10_Nsp16_CX_inPDB_out.pdb` by just keeping
  the protein atoms of chain A.

We have taken the following pockets from the priority list:

- pocket 1
- pocket 3
- pocket 26

## Pocket 1

From the sphere positions and radii given in `Nsp10_Nsp16_CX_inPDB_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  81.707 | 3.70   |  89.693 | 3.87   |
| y          |   9.280 | 3.48   |  17.793 | 3.70   |
| z          |  24.438 | 3.61   |  34.516 | 4.43   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  78.007 |  93.563 |  85.785  | 15.556 | 42   |
| y          |   5.800 |  21.493 |  13.646  | 15.693 | 42   |
| z          |  20.828 |  38.946 |  29.887  | 18.118 | 50   |

Hence the gridcenter and npts parameters are
```
gridcenter="85.785,13.646,29.887"
npts="42,42,50"

## Pocket 3

From the sphere positions and radii given in `Nsp10_Nsp16_CX_inPDB_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  76.515 | 4.23   |  98.219 | 4.31   |
| y          |  23.771 | 3.52   |  37.930 | 4.16   |
| z          |  36.411 | 3.68   |  49.728 | 4.63   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  72.285 | 102.529 |  87.407  | 30.244 | 82   |
| y          |  20.251 |  42.090 |  31.170  | 21.839 | 60   |
| z          |  32.731 |  54.358 |  43.544  | 21.627 | 58   |

Hence the gridcenter and npts parameters are
```
gridcenter="87.407,31.170,43.544"
npts="82,60,58"
```

## Pocket 26

From the sphere positions and radii given in `Nsp10_Nsp16_CX_inPDB_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  81.443 | 4.31   |  86.207 | 5.93   |
| y          |  35.443 | 3.41   |  41.699 | 5.93   |
| z          |  11.187 | 3.44   |  17.053 | 3.41   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  77.133 |  92.137 |  84.635  | 15.004 | 42   |
| y          |  32.033 |  47.629 |  39.831  | 15.596 | 42   |
| z          |   7.747 |  20.463 |  14.105  | 12.716 | 34   |

Hence the gridcenter and npts parameters are
```
gridcenter="84.635,39.831,14.105"
npts="42,42,34"
```

