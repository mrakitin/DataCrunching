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

