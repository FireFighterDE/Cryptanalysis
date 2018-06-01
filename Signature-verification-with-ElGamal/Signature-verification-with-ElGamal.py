#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Signature-verification-with-ElGamal.py
description    : Verifys signature
author         : Sebastian Pflaum (240646)
usage          : python Signature-verification-with-ElGamal.py (p,g,e) (m,rho,s)
example        : python Signature-verification-with-ElGamal.py (11,5,4) (8,9,9)
python_version :3.6.3
"""

import sys
import platform

def main(Kpub,sigN):
    system = platform.system()
    
    print('Signature-verification-with-ElGamal.py running on {0}'.format(system))
    print('--------------------------------------')
    
    print('> 0. Pre-Definitions:     Kpub=(p,g,e)={0}, sigN=(m,rho,s)={1}'.format(Kpub,sigN))
    
    p = int(Kpub[1:-1].split(',')[0])
    g = int(Kpub[1:-1].split(',')[1])
    e = int(Kpub[1:-1].split(',')[2])
    
    m = int(sigN[1:-1].split(',')[0])
    rho = int(sigN[1:-1].split(',')[1])
    s = int(sigN[1:-1].split(',')[2])
    
    A = (e**rho * rho**s) % p
    
    print('> 1. Verification Step 1: A={0}'.format(A))
    
    B = g**m % p
    
    print('> 2. Verification Step 2: B={0}'.format(B))
    
    if A==B:
        result = 'passed'
    else:
        result = 'failed'
        
    print('')
    print('> Verification result:    {0}'.format(result))
    
if __name__ == "__main__":
    Kpub = sys.argv[1]
    sigN = sys.argv[2]
    
    main(Kpub,sigN)