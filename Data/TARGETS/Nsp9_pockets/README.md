# Nsp10_pockets

The three main files are:

- Nsp9_Refined_out.pdb: Contains the protein structure plus the 
  positions of the `fpocket` spheres to identify the pocket locations
- Nsp9_Refined_info.txt: Contains summary information on every pocket
  identified by `fpocket`
- Nsp9_Refined_pockets.pqr: Contains the `fpocket` spheres for every
  pocket, giving both the position and radius of the spheres.

The information from `Nsp9_Refined_info.txt` can be used to select
promising pockets to target. The information from 
`Nsp9_Refined_pockets.pqr` for each pocket can be used to define the
box that contains the pocket. From `Nsp9_Refined_out.pdb` we can
extract the structure of just the Nsp10 protein.

- Nsp9.pdb: was created from `Nsp9_Refined_out.pdb` by just keeping
  the protein atoms.

We have taken the following pockets from the priority list:

- pocket 2
- pocket 7

## Pocket 2

From the sphere positions and radii given in `Nsp9_Refined_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  28.615 | 3.69   |  41.882 | 3.49   |
| y          |  -7.800 | 3.51   |  -1.483 | 4.49   |
| z          |   8.878 | 3.57   |  19.066 | 3.96   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  24.925 |  45.372 |  35.148  | 20.447 | 56   |
| y          | -11.310 |   3.007 |  -4.151  | 14.317 | 40   |
| z          |   5.308 |  23.026 |  14.167  | 17.718 | 48   |

Hence the gridcenter and npts parameters are
```
gridcenter="35.148,-4.151,14.167"
npts="56,40,48"


## Pocket 7

From the sphere positions and radii given in `Nsp9_Refined_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  51.159 | 3.87   |  59.576 | 4.34   |
| y          |  -2.545 | 3.43   |   4.406 | 4.67   |
| z          |  13.888 | 4.21   |  25.927 | 3.48   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  47.289 |  63.916 |  55.602  | 16.627 | 46   |
| y          |  -5.975 |   9.076 |   1.550  | 15.051 | 42   |
| z          |   9.678 |  29.407 |  19.542  | 19.729 | 54   |

Hence the gridcenter and npts parameters are
```
gridcenter="55.602,1.550,19.542"
npts="46,42,54"

