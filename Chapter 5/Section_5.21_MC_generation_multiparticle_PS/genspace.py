#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:18:38 2020

@author: rubbiaa

Phenomenology of Particle Physics

Chapter 5

A Python code to generate phase space for the B^0 -> K^*(892)\gamma -> K^+\pi^- \gamma decay chain

This work is licensed under the Creative Commons Attribution 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""

from phasespace import GenParticle

# setting up particle masses in MeV (ignore widths, values taken from the PDG)
B0_MASS = 5279.64
KSTARZ_MASS = 895.5
PION_MASS = 139.571
KAON_MASS = 493.677

# defining particles with the decay chain
pion = GenParticle('pi-', PION_MASS)
kaon = GenParticle('K+', KAON_MASS)

kstar = GenParticle('K*', KSTARZ_MASS).set_children(pion, kaon)

gamma = GenParticle('gamma', 0)
bz = GenParticle('B0', B0_MASS).set_children(kstar, gamma)

# generate 5 events
weights, particles = bz.generate(n_events=5)

# print the outputs
print("Parent particle:", bz)
print("Weights:", weights)
print("K*:", particles['K*'])
print("gamma:", particles['gamma'])

print("pi-:", particles['pi-'])
print("K+:", particles['K+'])
