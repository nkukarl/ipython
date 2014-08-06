# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

c = 4.18; # specific heat capacity of water
L1 = 0.25; # water depth in cm
A = 10; # open area in cm^2
V = L1 * A; # water volume
rho = 1; # water density
m = rho * V; # water mass
P1 = c * m * 1.186481 / 60; # initial power
T_conv = 273.15; # to convert from degree celsius to absolute temperature (Kelvin)
T_water_ini = 30 + T_conv; # water temperature in Kelvin
emissivity = 1; # emissivity of sky and water
sigma = 5.67 * 10 ** -8; # Stefan-Boltzmann constant
T_sky = (T_water_ini ** 4 - P1 / emissivity / sigma / (A * 10 ** -4)) ** 0.25; # sky temperature

molar_mass = 18; # water molar mass in grams
mole_water = m / molar_mass; # water mole
h_f = 6020; # water heat of fusion in joule per mole
E = mole_water * h_f; # energy required
T_water_fin = 0 + T_conv; # water temperature in Kelvin before freezing
P2 = emissivity * sigma * (A * 10 ** -4) * (T_water_fin ** 4 - T_sky **4); # final power
t1 = E / P2 / 60; # time required for completely freezing in minutes

t2 = 8; # time for completely freezing for new depth of water
L2 = t2 * 60 / t1 * L1; # new depth of water

print "*******************************************"
print "Sky temperature : " + str(T_sky) + " K"
print "Time required for completely freezing : " + str(t1) + " minutes"
print "Depth of water : " + str(L2) + " cm"
print "*******************************************"

# <codecell>


