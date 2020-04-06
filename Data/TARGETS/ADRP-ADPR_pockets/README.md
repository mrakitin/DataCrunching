# ADRP-ADPR_pockets

The three main files are:

- ADRP-ADPR_6w02_out.pdb: Contains the protein structure plus the positions of
  the `fpocket` spheres to identify the pocket locations
- ADRP-ADPR_6w02_info.txt: Contains summary information on every pocket
  identified by `fpocket`
- ADRP-ADPR_6w02_pockets.pqr: Contains the `fpocket` spheres for every pocket,
  giving both the position and radius of the spheres.

The information from `ADRP-ADPR_6w02_pockets.txt` can be used to select
promising pockets to target. The information from `ADRP-ADPR_6w02_pockets.pqr`
for each pocket can be used to define the box that contains the pocket. From 
`ADRP-ADPR_6w02_out.pdb` we can extract the structure of just the protein.

- ADRP-ADPR.pdb: was created from `ADRP-ADPR_6w02_out.pdb` by just keeping
  the protein atoms.

We have taken the following pockets from the priority list:

- pocket 1
- pocket 5

## Pocket 1

From the sphere positions and radii we given in `ADRP-ADPR_6w02_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  -0.575 | 3.42   |   8.131 | 3.60   |
| y          |  -9.821 | 3.42   |  -1.534 | 3.57   |
| z          | -29.073 | 3.63   | -16.820 | 3.60   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |  -3.995 |  11.731 |   3.868  | 15.726 | 42   |
| y          | -13.241 |   2.036 |  -5.602  | 15.277 | 42   |
| z          | -32.703 | -13.220 | -22.961  | 19.483 | 52   |

Hence the gridcenter and npts parameters are
```
gridcenter="3.868,-5.602,-22.961"
npts="42,42,52"
```

## Pocket 5

From the sphere positions and radii we given in `ADRP-ADPR_6w02_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |   4.968 | 3.53   |   9.379 | 4.64   |
| y          | -11.734 | 3.88   |  -5.284 | 5.54   |
| z          | -20.810 | 5.54   | -15.862 | 3.53   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |   1.438 |  14.019 |   7.728  | 12.581 | 34   |
| y          | -15.614 |   0.256 |  -7.679  | 15.870 | 44   |
| z          | -26.350 | -12.332 | -19.341  | 14.018 | 38   |

Hence the gridcenter and npts parameters are
```
gridcenter="7.728,-7.679,-19.341"
npts="34,44,38"
```

