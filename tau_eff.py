# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

def tau_eff(SigmaRatio):
    k = 1.38e-23
    T = 300
    q = 1.6e-19
    n = np.logspace(10, 18, 101)
    Na = 1.5e16
    B = 9.5e-15
    Ei = 0
    Et = Ei + 0
    ni = 1e10
    SigmaP = 1e-18
    # SigmaN = 1e-18
    # SigmaRatio = np.ceil(SigmaN / SigmaP)
    SigmaN = SigmaP * SigmaRatio
    vth = 1e7
    Nt = 1e15
    Cn = 2.2e-31
    Cp = 9.9e-32
    Sp0 = 1e2
    Sn0 = 1e2
    W = 0.03
    
    tauRad = 1 / (B * (n + Na))
    
    n1 = ni * np.exp((Et - Ei) * q / k / T)
    p1 = ni ** 2 / n1
    taup0 = 1 / SigmaP / vth / Nt
    taun0 = 1 / SigmaN / vth / Nt
    tauSRH = taup0 * (n1 + n) / (Na + n) + taun0 * (Na + p1 + n) / (Na + n)
    
    tauAug = 1 / (Cp * (Na + n) ** 2 + Cn * (Na + n) * n)
    
    tauB = 1 / (1 / tauRad + 1 / tauSRH + 1 / tauAug)
    
    S0 = (Na + n) / ((n1 + n) / Sp0 + (Na + p1 + n) / Sn0)
    Sw = S0
    
    tauS = W / (S0 + Sw)
    
    tauEff = 1/ (1 / tauB + 1 / tauS)
    
    plt.figure(num = 1, figsize = (8, 6), dpi = 120, \
               facecolor = 'w', edgecolor = 'k')
    plt.loglog(n, tauB * 1e6, n, tauRad * 1e6, n, tauSRH * 1e6, \
               n, tauAug * 1e6, linewidth = 4)
    plt.xlabel(r'$\Delta n\ (cm^{-3})$')
    plt.ylabel(r'$\tau\ (\mu s)$')
    plt.title('Injection level dependent lifetime ($\sigma_n/\sigma_p$ = $10^{' \
              + str(np.log10(SigmaRatio)) + '}$)')
    plt.legend([r'$\tau_{Bulk}$', r'$\tau_{Radiative}$', r'$\tau_{SRH}$', \
                r'$\tau_{Auger}$'], loc = 0)
    # plt.savefig('Bulk lifetime (SigmaRatio = ' + str(SigmaRatio) + ').png')
    
    plt.figure(num = 2, figsize = (8, 6), dpi = 120, \
               facecolor = 'w', edgecolor = 'k')
    plt.loglog(n, tauB * 1e6, n, tauS * 1e6, n, tauEff * 1e6, \
               linewidth = 4)
    plt.xlabel(r'$\Delta n\ (cm^{-3})$')
    plt.ylabel(r'$\tau\ (\mu s)$')
    plt.title('Injection level dependent lifetime ($\sigma_n/\sigma_p$ = $10^{' + \
              str(np.log10(SigmaRatio)) + '}$)')
    plt.legend([r'$\tau_{Bulk}$', r'$\tau_{Surface}$', r'$\tau_{Effective}$'], \
               loc = 0)
    # plt.savefig('Bulk, surface and effective lifetimes (SigmaRatio = ' + \
    #             str(SigmaRatio) + ').png')
    
    plt.show()


tau_eff(11)

