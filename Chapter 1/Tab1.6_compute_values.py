#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:18:38 2020

@author: rubbiaa

Phenomenology of Particle Physics

Chapter 1

Table 1.6 Units, derived units, and conversion for primary physical quantities.

This work is licensed under the Creative Commons Attribution 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or 
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""

import math

# charge in Coulomb (exact)
e=1.602176634e-19

# Planck h J.s (exact)
h=6.62607015e-34

# speed of light m/s (exact)
c= 299792458 

hbar = h/(2*math.pi)
hbar_MeVs = hbar/e/1e6
hbar_GeVs = hbar/e/1e9

print("hbar = ", hbar, " J*s")
print("hbar = ", hbar_MeVs, " MeV*s")

print ("-----------")

hbarc = hbar*c
print("hbar*c = ", hbarc, " J*m")
hbarc_MeVfm = hbar*c/e/1e6*1e15
print("hbar*c = ", hbarc_MeVfm, " MeV*fm")
hbarc_GeVfm = hbarc_MeVfm/1e3

print ("-----------")

onemeter_GeVinverse = 1e15/(hbarc_GeVfm)
print("1 meter = ", "{:.7e}".format(onemeter_GeVinverse), "GeV^-1")

onesecond_GeVinverse = 1/hbar_GeVs
print("1 second = ", "{:.7e}".format(onesecond_GeVinverse), "GeV^-1")

print ("------- TABLE 1.6 -------")
mass_oneGeV_in_kg = 1e9*e/(c**2)
length_oneGeVexpominusone_in_m = hbarc_GeVfm*1e-15
time_oneGeVexpominusone_in_s = hbar_GeVs
energy_oneGeV_in_J = e*1e9
momentum_oneGeV_in_kgms = e*1e9/c
force_oneGeV_in_N = (e*1e9)**2/hbar/c
area_oneGeV_in_m2 = (hbarc_MeVfm/1e3/1e15)**2
area_oneGeV_in_mb = area_oneGeV_in_m2*1e3/1e-28

print("Mass: 1 GeV = ", "{:.7e}".format(mass_oneGeV_in_kg), "kg")
print("Length: 1 GeV^-1 = ", "{:.7e}".format(length_oneGeVexpominusone_in_m), "m")
print("Time: 1 GeV^-1 = ", "{:.7e}".format(time_oneGeVexpominusone_in_s), "s")
print("Momentum 1 GeV = ", "{:.7e}".format(momentum_oneGeV_in_kgms), "kg m/s")
print("Force: 1 GeV^2 = ", "{:.7e}".format(force_oneGeV_in_N), "N")
print("Cross-section: 1 GeV^2 = ", "{:.7f}".format(area_oneGeV_in_mb), "mb")

print ("-----------")

e_field_oneGeV2 = force_oneGeV_in_N/e
b_field_oneGeV2 = e_field_oneGeV2/c

print("E-field: 1 GeV = ", "{:.7e}".format(e_field_oneGeV2), "V/m")
print("B-field: 1 GeV = ", "{:.7e}".format(b_field_oneGeV2), "T")


