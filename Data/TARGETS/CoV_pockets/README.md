# CoV_pockets

- CoV.pdb: was created from `CoV_RBD_out.pdb` by just keeping
  the protein atoms.

We have taken the following pockets from the priority list:

- pocket 1
- pocket 2

## Pocket 1

From the sphere positions and radii given in `CoV_RBD_pockets.pqr`
we collect:

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          | -15.779 | 4.03   |  -4.230 | 4.65   |
| y          |  -2.696 | 4.03   |   8.211 | 3.44   |
| z          |   0.781 | 4.18   |  13.104 | 3.52   |

Compute from the results in the table above the lower and upper limits of 
the coordinates. The lower limits are calculated by taking the minimum value
of a coordinate and subtracting the sphere radius. The upper limits are 
calculated by taking the maximum value of a coordinate and adding the sphere
radius. The number of points are calculated from the length and using that the
default grid spacing is 0.375 Angstrom (note that the number of grid points
has to be even in every dimension). This way we get:

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          | -19.809 |   0.420 |  -9.694  | 20.229 | 54   |
| y          |  -6.726 |  11.651 |   2.462  | 18.377 | 50   |
| z          |  -3.399 |  16.624 |   6.612  | 20.023 | 54   |

Hence the gridcenter and npts parameters are
```
gridcenter="-9.694,2.462,6.612"
npts="54,50,54"
```

## Pocket 2

| coordinate | min     | radius | max     | radius |
| ---------- | ------- | ------ | ------- | ------ |
| x          | -24.019 | 3.56 | -8.713 | 4.12 |
| y          | 28.449 | 4.54 | 39.037 | 3.82 |
| z          | -0.778 | 3.51 | 9.089 | 3.64 |

| coordinate | min     | max     | middle   | length | npts |
| ---------- | ------- | ------- | -------- | ------ | ---- |
| x          | -27.579 | -4.593 | -16.0860 | 22.986 | 62 |
| y          | 23.909 | 42.857 | 33.3830 | 18.948 | 52 |
| y          | -4.288 | 12.729 | 4.2205 | 17.017 | 46 |

```
npts="62,52,46"
center="-16.0860,33.3830,4.2205"
```
