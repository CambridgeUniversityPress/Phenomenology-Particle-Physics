#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:27:30 2022

@author: rubbiaa

Phenomenology of Particle Physics

Chapter 2

Figure 2.24 Stopping power (collision losses) as a function of momentum for different particles in iron.

This work is licensed under the Creative Commons Attribution 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or 
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""

import math

# energies in MeV
# MeV/mol cm2
K=0.31
me = 0.511
z=1


# incoming particle

def dedx(p,m, Z,A,I):
    E=math.sqrt(p**2+m**2)
    beta = p/E
    gamma=1/math.sqrt(1-beta**2)
    Wmax = (2*beta**2*gamma**2)/(1+2*gamma*(me/m)+(me/m)**2)*me
    p1 = 0.5*math.log(2*me*beta**2*gamma**2*Wmax/I**2)
    p2 = -beta**2
    dedx1 = K*Z/A/beta**2*(p1+p2)
    return (dedx1)

def plotcurve(partname, m, targetname, Z, A, I):
    print("% ", partname, " ",targetname)
    for ie in range(-20,30):
        expo = ie/10.0
        p=10**expo
        print("(",p,",",dedx(p*1e3,m, Z,A,I*1e-6),")")

# mass of particles in MeV
mmuon=105.7
mproton=938.3
mpion=139.570
mkaon=493.677
#
IFe=286.0
ZFe=26
AFe=55.845
plotcurve("muon",mmuon, "iron/Fe",ZFe,AFe,IFe)
plotcurve("pion",mpion, "pion/Fe",ZFe,AFe,IFe)
plotcurve("kaon",mkaon, "kaon/Fe",ZFe,AFe,IFe)
plotcurve("proton",mproton, "iron/Fe",ZFe,AFe,IFe)
