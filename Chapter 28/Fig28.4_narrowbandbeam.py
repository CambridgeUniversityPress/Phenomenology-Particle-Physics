#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:00:17 2020

@author: rubbiaa

Phenomenology of Particle Physics

Chapter 28

A simple Python code to generate a neutrino beam.

This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""

import random
import math

# distances in meters
# energies in GeV

# mass of particles in GeV
mmuon=105.7e-3
mproton=938.3e-3
mpion=139.570e-3
mkaon=493.677e-3

# beam parameters
# distance to detector (m)
L=800
# momentum selection NBB (GeV)
p0 = 300
# radius of beam (sigma)
r0 = 0.3
# decay tunnel (m)
decaytunnellength = 300
decaytunnelradius = 1

f = open('narrowbandbeam.dat', 'w')

title = "ENU   R\n"
f.write(title)

for i in range(0,100000):

    pbeam = (1+random.gauss(0, 0.05))*p0
    x0 = random.gauss(0,r0)
    y0 = random.gauss(0,r0)
    rbeam = math.sqrt(x0**2+y0**2)
    if(abs(rbeam) > decaytunnelradius):
        continue

# assume 70% of pions in the beam
    if(random.random()<0.7):
        mmeson = mpion
        tau=26e-9
    else:
        mmeson = mkaon
        tau=12e-9

    ebeam = math.sqrt(pbeam**2+mmeson**2)
    beta = pbeam/ebeam
    gamma = ebeam/mmeson

    decaypoint = -gamma*3e8*tau*math.log(random.random())
    if(decaypoint>decaytunnellength):
        continue

    # maximum energy in meson CMS
    enustar = (mmeson**2 - mmuon**2)/(2*mmeson)

    # decay angle in the meson CMS
    costhetastar = random.uniform(-1,1)

    # lab quantities
    enu = gamma*enustar*(1+beta*costhetastar)
    costheta = (costhetastar+beta)/(1+beta*costhetastar)
    sintheta = math.sqrt(1-costheta**2)
    tantheta = sintheta/costheta
    phi = 2*math.pi*random.random()
    x = (L-decaypoint)*tantheta*math.cos(phi)+x0
    y = (L-decaypoint)*tantheta*math.sin(phi)+y0
    R = math.sqrt(x**2+y**2)

    if(R<3):
        out = "%f\t%f\n" % (enu,R)
        f.write(out)

f.close()
