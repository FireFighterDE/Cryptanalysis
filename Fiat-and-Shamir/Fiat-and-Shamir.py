#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Fiat-and-Shamir.py
description    : Get key K for given encrypted string
author         : Sebastian Pflaum (240646)
usage          : python CaesarEncryption.py 'encrypted string'
example        : python CaesarEncryption.py 'Lpu lpumhjolz Jhlzhy Ilpzwpls'
python_version :3.6.3
"""

import sys
import platform
from random import randint

def ggT(k, n):
    while k > 0 and n > 0:
        if k >= n:
            k = k - n
        else:
            n = n - k
    return k+n

def ExtGCD(x, y):
    m,n=x,y
    b,d=0,1
    p,t=1,0
    
    while (m!=0):
        q = n//m  # yes, //
        n,m=m,n-q*m
        d,b=b,d-q*b
        t,p=p,t-q*p
    
    return d


def main():
    system = platform.system()
    
    ggTCheck = 0
    
    print('Fiat-and-Shamir.py running on {0}'.format(system))
    print('--------------------------------------')
    
    while ggTCheck != 1:
        p = randint(1, 10)
        #p = 5
        
        q = randint(1, 10)
        #q = 3
    
        n = p * q
    
        k = randint(1, 20)
        #k = 13
    
        ggTCheck = ggT(k, n)
        
    s = randint(1, 10)
    #s = 7
    
    v = ExtGCD(n, s**2)
    
    if v < 0:
        print('> Info: v is smaller than 0! Original value of v={0}'.format(v))
        v = n + v
    
    print('> 0. Pre-Definitions: p={0}, q={1}, n={2}, Kpr=(s)=({3}), Kpub=(n,v)=({4},{5})'.format(p,q,n,s,n,v))
       
    x = k**2 % n
    
    print('> 1. Commitment:      k={0} > ggT(k,n)={1}, x={2}'.format(k,ggTCheck,x))
    
    b = randint(0, 1)
    
    print('> 2. Challenge:       b={0}'.format(b))
    
    if b == 0:
        y = k % n
    
    elif b == 1:
        y = k * s % n
        
    print('> 3. Response:        y={0}'.format(y))

if __name__ == "__main__":
    main()