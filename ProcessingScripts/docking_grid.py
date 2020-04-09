#!/usr/bin/env python3
'''
Compute the grid box for a receptor pocket

In drug-screening Fpocket may be used to find a binding pocket in a protein.
A pocket is given by a collection of alpha-spheres. Each alpha-sphere is 
defined as a sphere that touches 4 atoms, demarcating the opening of 
the pocket. Each sphere is given by its position and radius in a
.pqr file.

The autogrid4 program builds a docking grid on which the potentials for
docking are expressed. The grid is defined in a rectangular box that
encompasses the binding pocket. The box is given by the position of its
center, and the number of grid points in each spatial dimension.
The number of grid points combined with the grid spacing determines
the lengths of each side of the box. This script uses the Autodock
default grid spacing.

This script takes a collection of alpha-spheres and computes the
specification of the grid box for autogrid4 as the box center
and the numbers of grid points. In essence it automates the calculation
done in DataCrunching/Data/TARGETS/3CLPro_pockets/README.md.
'''

def parse_line(line):
    '''
    Take a line from a PQR file and return a tuple containing
    (xcoord,ycoord,zcoord,radius) where the x, y, and z coordinates
    are the coordinates of the alpha-sphere (see fpocket), and
    the radius is the radius of the alpha-sphere.
    '''
    length=len(line)
    if length < 71:
      print("line too short: ",line)
      return None
    xcoord=float(line[31:39])
    ycoord=float(line[39:47])
    zcoord=float(line[47:55])
    radius=float(line[67:])
    return (xcoord,ycoord,zcoord,radius)

def min_and_max(tuple):
    '''
    Given a tuple (xcoord,ycoord,zcoord,radius) return another tuple
    with minimum and maximum coordinates (xmin,ymin,zmin,xmax,ymax,zmax).
    Xmin=xcoord-radius, xmax=xcoord+radius.
    '''
    (xcoord,ycoord,zcoord,radius)=tuple
    xmin=xcoord-radius
    xmax=xcoord+radius
    ymin=ycoord-radius
    ymax=ycoord+radius
    zmin=zcoord-radius
    zmax=zcoord+radius
    return (xmin,ymin,zmin,xmax,ymax,zmax)

def parse_file(lines):
    '''
    Go through all the lines in a file and return a list of 
    all 4-tuples.
    '''
    t4list=[]
    for line in lines:
        tuple=parse_line(line)
        if tuple:
            t4list.append(tuple)
    return t4list

def gen_minmax(t4list):
    '''
    Go through the 4-tuple list and for each element 
    add an element to the 6-tuple list.
    '''
    t6list=[]
    for t4 in t4list:
        t6=min_and_max(t4)
        t6list.append(t6)
    return t6list

def find_minmax(t6list):
    '''
    Go through the list of 6-tuples and find the index for 
    the minimum and maximum coordinates. Return the result
    as a 12-tuple
    (ixmin,iymin,izmin,ixmax,iymax,izmax,xmin,ymin,zmin,xmax,ymax,zmax).
    '''
    ixmin=0
    iymin=0
    izmin=0
    ixmax=0
    iymax=0
    izmax=0
    (xmin,ymin,zmin,xmax,ymax,zmax)=t6list[0]
    ielm=-1
    for t6 in t6list:
        ielm+=1
        (xmin1,ymin1,zmin1,xmax1,ymax1,zmax1)=t6
        if xmin1 < xmin:
            ixmin = ielm
            xmin  = xmin1
        if ymin1 < ymin:
            iymin = ielm
            ymin  = ymin1
        if zmin1 < zmin:
            izmin = ielm
            zmin  = zmin1
        if xmax1 > xmax:
            ixmax = ielm
            xmax  = xmax1
        if ymax1 > ymax:
            iymax = ielm
            ymax  = ymax1
        if zmax1 > zmax:
            izmax = ielm
            zmax  = zmax1
    return (ixmin,iymin,izmin,ixmax,iymax,izmax,xmin,ymin,zmin,xmax,ymax,zmax)

def find_npts(t12,spacing,factor):
    '''
    Given the 12-tuple compute the number of points for each dimension.
    The number of points is computed from the length of a dimension
    and the grid spacing. The number of grid points must be a multiple of
    factor. Return the 3-tuple of numbers of points.
    '''
    (ixmin,iymin,izmin,ixmax,iymax,izmax,xmin,ymin,zmin,xmax,ymax,zmax)=t12
    xlen=(xmax-xmin)/spacing
    ylen=(ymax-ymin)/spacing
    zlen=(zmax-zmin)/spacing
    xnpts=int(xlen/float(factor)+1.0)*int(factor)
    ynpts=int(ylen/float(factor)+1.0)*int(factor)
    znpts=int(zlen/float(factor)+1.0)*int(factor)
    return (xnpts,ynpts,znpts)
    
def find_center(t12):
    '''
    Given the 12-tuple compute the center of the receptor.
    Return the 3-tuple of center coordinates.
    '''
    (ixmin,iymin,izmin,ixmax,iymax,izmax,xmin,ymin,zmin,xmax,ymax,zmax)=t12
    xcen=(xmax+xmin)/2.0
    ycen=(ymax+ymin)/2.0
    zcen=(zmax+zmin)/2.0
    return (xcen,ycen,zcen)
    
def find_lengths(t12):
    '''
    Given the 12-tuple compute the lengths of the receptor.
    Return the 3-tuple of lengths.
    '''
    (ixmin,iymin,izmin,ixmax,iymax,izmax,xmin,ymin,zmin,xmax,ymax,zmax)=t12
    xlen=(xmax-xmin)
    ylen=(ymax-ymin)
    zlen=(zmax-zmin)
    return (xlen,ylen,zlen)

def parse_arguments():
    '''
    Parse the arguments.
    '''
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("filename",help="PQR file to generate grid-box from")
    args=parser.parse_args()
    return args

if __name__ == "__main__":
    args=parse_arguments()
    fobj=open(args.filename,"rb")
    contents=fobj.readlines()
    fobj.close()
    t4list=parse_file(contents)
    t6list=gen_minmax(t4list)
    t12=find_minmax(t6list)
    npts=find_npts(t12,0.375,2)
    (xpts,ypts,zpts)=npts
    cent=find_center(t12)
    (xcen,ycen,zcen)=cent
    leng=find_lengths(t12)
    (xlen,ylen,zlen)=leng
    (ixmin,iymin,izmin,ixmax,iymax,izmax,xmin,ymin,zmin,xmax,ymax,zmax)=t12
    print(f"| coordinate | min     | radius | max     | radius |")
    print(f"| ---------- | ------- | ------ | ------- | ------ |")
    (xxmin,tmpy,tmpz,xxmnr)=t4list[ixmin]
    (xxmax,tmpy,tmpz,xxmxr)=t4list[ixmax]
    (tmpx,yymin,tmpz,yymnr)=t4list[iymin]
    (tmpx,yymax,tmpz,yymxr)=t4list[iymax]
    (tmpx,tmpy,zzmin,zzmnr)=t4list[izmin]
    (tmpx,tmpy,zzmax,zzmxr)=t4list[izmax]
    print(f"| x          | {xxmin:.3f} | {xxmnr:.2f} | {xxmax:.3f} | {xxmxr:.2f} |")
    print(f"| y          | {yymin:.3f} | {yymnr:.2f} | {yymax:.3f} | {yymxr:.2f} |")
    print(f"| z          | {zzmin:.3f} | {zzmnr:.2f} | {zzmax:.3f} | {zzmxr:.2f} |")
    print(f"")
    print(f"| coordinate | min     | max     | middle   | length | npts |")
    print(f"| ---------- | ------- | ------- | -------- | ------ | ---- |")
    print(f"| x          | {xmin:.3f} | {xmax:.3f} | {xcen:.4f} | {xlen:.3f} | {xpts} |")
    print(f"| y          | {ymin:.3f} | {ymax:.3f} | {ycen:.4f} | {ylen:.3f} | {ypts} |")
    print(f"| z          | {zmin:.3f} | {zmax:.3f} | {zcen:.4f} | {zlen:.3f} | {zpts} |")
    print(f"")
    print(f"```")
    print(f"npts=\"{xpts},{ypts},{zpts}\"")
    print(f"center=\"{xcen:.4f},{ycen:.4f},{zcen:.4f}\"")
    print(f"```")

