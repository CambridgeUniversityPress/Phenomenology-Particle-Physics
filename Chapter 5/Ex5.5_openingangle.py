#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:11:51 2022

@author: rubbiaa

Phenomenology of Particle Physics

Chapter 5

Exercise 5.5 Opening angle

This work is licensed under the Creative Commons Attribution 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or 
send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""
import math


def openingangle(cost, betaL, beta1, beta2):
    gamma = 1.0/math.sqrt(1-betaL*betaL)
    num = betaL*(beta1+beta2)/(beta1*beta2)*math.sqrt(1-cost*cost)
    D = -betaL*betaL*cost*cost+betaL*(beta1-beta2)/(beta1*beta2)*cost+(betaL*betaL/(beta1*beta2)-1+betaL*betaL)
    return math.atan2(num,gamma*D)

def plotcurve(betaL, beta1, beta2):
    print("% ", betaL, beta1, beta2)
    for ic in range(-100,101):
        cost = float(ic/100.0)
        a = openingangle(cost, betaL, beta1, beta2)
        print("(",cost,",",a*180/math.pi,")")

# cross-check with massless final state particle
betaL = 0.8
beta1 = 1
beta2 = 1
plotcurve(betaL, beta1, beta2)

# case 1: betaL < beta1*, beta2*
betaL = 0.5
beta1 = 0.7
beta2 = 0.9
plotcurve(betaL, beta1, beta2)

# case 2: beta1* < betaL < beta2*
betaL = 0.5
beta1 = 0.3
beta2 = 0.9
plotcurve(betaL, beta1, beta2)

# case 2: beta1*, beta2* < betaL
betaL = 0.7
beta1 = 0.3
beta2 = 0.5
plotcurve(betaL, beta1, beta2)

