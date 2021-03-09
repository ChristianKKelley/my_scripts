#!/usr/bin/env python3

import numpy as np

scal = 10
low_val = 150
high_val = (scal*100) - 150


def levy_distance(poss,e):
#    x = pos[e]
#    de = min(x,abs((scal*100)-x))
#    if de < 75:
#        if de == x:
#            return 150
#        else:
#            return -150
#    done = 0
    for i in range(10000):
        bx = (np.random.randint(0,2)-0.5)*2
        t = (scal*50)*(1-np.random.power(3))
        nloc = poss[e]+(t*bx)
        if i == 9999:
            return 0
        if nloc < 950 and nloc > 50:
            disto = bx*t
            return disto
            
def levy_walk(poss):
    dx = levy_distance(poss,0)
    dy = levy_distance(poss,1)
    dz = levy_distance(poss,2)
    tot = (dx*dx + dy*dy + dz*dz)**(0.5)
    number = int(np.ceil(tot/(1.3*scal)))
    return number, dx, dy, dz
#BN = bead number
#Btot = total length of chromosome

def mc(po,de,re):
    te = int(de+re+po)
    if te > 999:
        return int(de+re+po-10)
    elif te < 0:
        return int(de+re+po+10)
    else:
        return te

def walker(pos,grid):
    stata = 0
    while stata == 0:
            rad = 0
            bx = 0
            bz = 0
            by = 0
            dim1 = np.random.randint(0,3)
            if dim1 == 0:
                dim2 = np.random.randint(0,2)
                bx = np.random.randint(-1,2)
                rad = rad + abs(bx)
                if dim2 == 0:
                    by = np.random.randint(-1,2)
                    rad = rad + abs(by)
                    if rad < 2:
                        bz = np.random.randint(-1,2)
                else:
                    bz = np.random.randint(-1,2)
                    rad = rad + abs(bz)
                    if rad < 2:
                        by = np.random.randint(-1,2)
            elif dim1 == 1:
                dim2 = np.random.randint(0,2)
                by = np.random.randint(-1,2)
                rad = rad + abs(by)
                if dim2 == 0:
                    bx = np.random.randint(-1,2)
                    rad = rad + abs(by)
                    if rad < 2:
                        bz = np.random.randint(-1,2)
                else:
                    bz = np.random.randint(-1,2)
                    rad = rad + abs(bz)
                    if rad < 2:
                        bx = np.random.randint(-1,2)
            else:
                dim2 = np.random.randint(0,2)
                bz = np.random.randint(-1,2)
                rad = rad + abs(bz)
                if dim2 == 0:
                    bx = np.random.randint(-1,2)
                    rad = rad + abs(bx)
                    if rad < 2:
                        by = np.random.randint(-1,2)
                else:
                    by = np.random.randint(-1,2)
                    rad = rad + abs(by)
                    if rad < 2:
                        bx = np.random.randint(-1,2)
#            bx = np.random.randint(-1,2)
#            by = np.random.randint(-1,2)
#            bz = np.random.randint(-1,2)
            bx = scal*bx
            by = scal*by
            bz = scal*bz
            ncx = pos[0]+bx
            if ncx < low_val:
                ncx = pos[0]+1
            elif ncx > high_val:
                ncx = pos[0]-1
            
            ncy = pos[1]+by
            if ncy < low_val:
                ncy = pos[1]+1
            elif ncy > high_val:
                ncy = pos[1]-1
            
            ncz = pos[2]+bz
            if ncz < low_val:
                ncz = pos[2]+1
            elif ncz > high_val:
                ncz = pos[2]-1
                
            coord = [ncx,ncy,ncz]
            occu = grid[ncx,ncy,ncz]
                
            if occu == 0:
                return coord
                stata = 1


def spot_finder(grid):
    stata = 0
    while stata == 0:
        bx = np.random.randint(low_val,high_val)
        by = np.random.randint(low_val,high_val)
        bz = np.random.randint(low_val,high_val)
        if grid[bx,by,bz] == 0:
            coord = [bx,by,bz]
            return coord
            stata = 1
