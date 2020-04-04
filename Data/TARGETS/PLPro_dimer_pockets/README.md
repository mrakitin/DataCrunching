# PLPro_dimer_pockets

The three main files are:

- PLPro_chainsAB_out.pdb: Contains the protein structure plus the positions of
  the `fpocket` spheres to identify the pocket locations
- PLPro_chainsAB_info.txt: Contains summary information on every pocket
  identified by `fpocket`
- PLPro_chainsAB_pockets.pqr: Contains the `fpocket` spheres for every pocket,
  giving both the position and radius of the spheres.

The information from `PLPro_chainsAB_info.txt` can be used to select promising
pockets to target. The information from `PLPro_chainsAB_pockets.pqr` for each
pocket can be used to define the box that contains the pocket. From 
`PLPro_chainsAB_out.pdb` we can extract the structure of just the protein.

- PLPro_chainsAB.pdb: was created from `PLPro_chainsAB_out.pdb` by just keeping
  the protein atoms.

Looking at `PLPro_chainsAB_info.txt` we can find that the following pockets
could be reasonable targets (by looking at the druggability scores):

- pocket 24 : double checking
- pocket 46 : double checking
- pocket 47 : double checking
- pocket 50

## Pocket 50

From the sphere positions and radii we given in `PLPro_chainsAB_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          | -25.119 | 3.45   |   1.422 | 3.45   |
| y          |  18.443 | 3.85   |  61.031 | 3.86   |
| z          | -50.702 | 4.27   | -28.274 | 3.57   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          | -28.569 |   4.872 | -11.849  | 33.441 |  90  |
| y          |  14.593 |  64.891 |  39.742  | 50.298 | 136  |
| z          | -54.972 | -24.704 | -39.838  | 30.268 |  82  |

Hence the gridcenter and npts parameters are
```
gridcenter="-11.849,39.742,-39.838"
npts="90,136,82"
```

