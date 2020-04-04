# PLPro_monomer_pockets

The three main files are:

- PLPro_chainA_out.pdb: Contains the protein structure plus the positions of the
  `fpocket` spheres to identify the pocket locations
- PLPro_chainA_info.txt: Contains summary information on every pocket identified
  by `fpocket`
- PLPro_chainA_pockets.pqr: Contains the `fpocket` spheres for every pocket,
  giving both the position and radius of the spheres.

The information from `PLPro_chainA_info.txt` can be used to select promising
pockets to target. The information from `PLPro_chainA_pockets.pqr` for each
pocket can be used to define the box that contains the pocket. From 
`PLPro_chainA_out.pdb` we can extract the structure of just the protein.

- PLPro_chainA.pdb: was created from `PLPro_chainA_out.pdb` by just keeping
  the protein atoms.

Looking at `PLPro_chainA_info.txt` we can find that the following pockets
could be reasonable targets (by looking at the druggability scores):

- pocket 3
- pocket 4
- pocket 6  : Running by Dean Hidas  (04/04/2020)
- pocket 23 : Running By Martin Purschke (04/04/2020)

## Pocket 3

From the sphere positions and radii we given in `PLPro_chainA_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  -2.469 | 3.48   |   7.206 | 4.68   |
| y          |  47.235 | 4.68   |  55.998 | 3.47   |
| z          | -29.477 | 3.73   | -19.803 | 3.54   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  -5.949 |  11.886 |   2.968  | 17.835 | 48   |
| y          |  42.555 |  59.468 |  51.011  | 16.913 | 46   |
| z          | -33.207 | -16.263 | -24.735  | 16.944 | 46   |

Hence the gridcenter and npts parameters are
```
gridcenter="2.968,51.011,-24.735"
npts="48,46,46"
```

## Pocket 6

From the sphere positions and radii we given in `PLPro_chainA_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  -1.664 | 3.52   |   7.848 | 4.53   |
| y          |  37.287 | 4.12   |  45.300 | 3.54   |
| z          | -16.542 | 4.53   | -11.903 | 4.12   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  -5.184 | 12.378  |   3.597  | 17.562 | 48   |
| y          |  33.167 | 48.840  |  41.004  | 15.673 | 42   |
| z          | -21.072 | -7.783  | -14.428  | 13.289 | 36   |

Hence the gridcenter and npts parameters are
```
gridcenter="3.597,41.004,-14.428"
npts="48,42,36"
```

## Pocket 23

From the sphere positions and radii we given in `PLPro_chainA_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          | -20.852 | 3.53   |  -6.663 | 4.59   |
| y          |  39.813 | 4.16   |  50.585 | 4.44   |
| z          | -42.778 | 4.09   | -35.451 | 4.16   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          | -24.382 |  -2.073 | -13.228  | 22.309 | 60   |
| y          |  35.653 |  55.025 |  45.339  | 19.372 | 52   |
| z          | -46.868 | -31.291 | -39.080  | 15.577 | 42   |

Hence the gridcenter and npts parameters are
```
gridcenter="-13.228,45.339,-39.080"
npts="60,52,42"
```
