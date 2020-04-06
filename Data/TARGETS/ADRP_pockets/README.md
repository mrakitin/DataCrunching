# ADRP_pockets

The three main files are:

- ADRP_Apo_6vxs_out.pdb: Contains the protein structure plus the positions of
  the `fpocket` spheres to identify the pocket locations
- ADRP_Apo_6vxs_info.txt: Contains summary information on every pocket
  identified by `fpocket`
- ADRP_Apo_6vxs_pockets.pqr: Contains the `fpocket` spheres for every pocket,
  giving both the position and radius of the spheres.

The information from `ADRP_Apo_6vxs_pockets.pqr` for each pocket can be used
to define the box that contains the pocket. From 
`ADRP_Apo_6vxs_out.pdb` we can extract the structure of just the protein.

- ADRP.pdb: was created from `ADRP_Apo_6vxs_out.pdb` by just keeping
  the protein atoms.

We have taken the following pockets from the priority list:

- pocket 1
- pocket 12
- pocket 13

## Pocket 1

From the sphere positions and radii we given in `ADRP_Apo_6vxs_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          | -13.975 | 4.13   |  -6.080 | 3.43   |
| y          | -14.932 | 3.79   |  -3.146 | 4.26   |
| z          | -15.346 | 4.26   |  -2.575 | 4.05   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          | -18.105 |  -2.650 | -10.377  | 15.455 | 42   |
| y          | -18.722 |   1.114 |  -8.804  | 19.836 | 54   |
| z          | -19.606 |   1.475 |  -9.065  | 21.081 | 58   |

Hence the gridcenter and npts parameters are
```
gridcenter="-10.377,-8.804,-9.065"
npts="42,54,58"
```

## Pocket 12

From the sphere positions and radii we given in `ADRP_Apo_6vxs_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |   8.510 | 4.23   |  15.043 | 4.33   |
| y          |  -7.998 | 3.94   |   1.048 | 4.60   |
| z          |  -7.789 | 4.50   |   1.910 | 4.60   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          |   4.280 |  19.373 |  11.826  | 15.093 | 42   |
| y          | -11.938 |   5.648 |  -3.145  | 17.586 | 48   |
| z          | -12.289 |   6.510 |  -2.889  | 18.799 | 52   |

Hence the gridcenter and npts parameters are
```
gridcenter="11.826,-3.145,-2.889"
npts="42,48,52"
```


## Pocket 13

From the sphere positions and radii we given in `ADRP_Apo_6vxs_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          |  -7.460 | 3.50   |   0.675 | 4.09   |
| y          | -21.955 | 3.50   | -12.336 | 3.94   |
| z          | -31.907 | 4.43   | -20.196 | 4.22   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          | -10.960 |   4.765 |  -3.097  | 15.725 | 42   |
| y          | -25.455 |  -8.396 | -16.925  | 17.059 | 46   |
| z          | -36.337 | -15.976 | -26.156  | 20.361 | 56   |

Hence the gridcenter and npts parameters are
```
gridcenter="-3.097,-16.925,-26.156"
npts="42,46,56"
```

