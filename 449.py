#!/usr/bin/env python

"""
Phil the confectioner is making a new batch of chocolate covered candy. Each candy centre is shaped like an ellipsoid of revolution defined by the equation: b2x2 + b2y2 + a2z2 = a2b2.

Phil wants to know how much chocolate is needed to cover one candy centre with a uniform coat of chocolate one millimeter thick.
If a=1 mm and b=1 mm, the amount of chocolate required is
28
3
	π mm3
If a=2 mm and b=1 mm, the amount of chocolate required is approximately 60.35475635 mm3.

Find the amount of chocolate in mm3 required if a=3 mm and b=1 mm. Give your answer as the number rounded to 8 decimal places behind the decimal point.
"""

import numpy as np
import matplotlib.pyplot as plt


#we use rotational symmetrie and reduce it to a radial problem
def radius(z, a, b):
    return a*np.sqrt(1-z**2/b**2)


def height(r, a, b):
    return b/a*np.sqrt(a**2-r**2)


def angle(r, a, b):
    return -np.arctan( (-b/a*r/np.sqrt(a**2-r**2))**(-1)  )


def r_z_new(r, a, b):
    z = height(r, a, b)
    phi = angle(r, a, b)
    r_n = r + np.sqrt(1/(1+np.tan(phi)**2))
    z_n = z + (r_n-r)*np.tan(phi)
    return [r_n, z_n]


def volume(r_z):
    sum = 0
    for i in range(0,len(r_z)-1):
        sum += ((r_z[i][0]+r_z[i+1][0])*0.5)**2*(r_z[i][1]-r_z[i+1][1])
    sum *= np.pi
    return sum

def solve(n, a, b):

    radii_1 = np.linspace(0,0.25*a,n//5)
    radii_2 = np.linspace(0.25*a,0.5*a,n//4)
    radii_3 = np.linspace(0.5*a,0.99*a,n//3)
    radii_4 = np.linspace(0.99*a,a,n)
    radii_1 = np.append(radii_1, radii_2)
    radii_2 = np.append(radii_3, radii_4)
    radii = np.append(radii_1, radii_2)
    z_arr = height(radii,a,b)
    
    r_z_in = [[radii[i],z_arr[i]] for i in range(0,len(radii)) ]

    
    r_z_out = [r_z_new(r, a, b) for r in radii]
    radii_2 = [x[0] for x in r_z_out]
    z_arr2 = [x[1] for x in r_z_out]
    # plt.plot(radii_2, z_arr2)
    # plt.show()

    return np.round(2*(volume(r_z_out)-volume(r_z_in)),8)

print(solve(600000, 3, 1))
