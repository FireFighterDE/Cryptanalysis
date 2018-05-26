#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Fiat-and-Shamir.py
description    : Values have to be adjusted within script or run with random values
author         : Sebastian Pflaum (240646)
usage          : python Fiat-and-Shamir.py
example        : python Fiat-and-Shamir.py
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
        #p = randint(1, 10)
        p = 5
        
        #q = randint(1, 10)
        q = 3
    
        n = p * q
        #n = 15
        
        k = randint(1, 20)
        #k = 13
    
        ggTCheck = ggT(k, n)
        
    ggTCheck2 = 0
    
    while ggTCheck2 !=1:
        s = randint(1, 10)
        #s = 7
        
        ggTCheck2 = ggT(n, s)
    
    print('> Info: s is choosen randomly. v is calculated according following condition: s**2 * v = 1 mod n')
    print('> Info: This means that the multiplicative element of s**2 must be calculated.')
    print('> Info: If v is negative, the additive inverse element must be calculated.')
    print('')
    
    ggTCheck3 = 0
    
    while ggTCheck3 !=1:
        v = ExtGCD(n, s**2)
        #v = 4
    
        if v < 0:
            print('> Note: v is smaller than 0! Original value of v={0}'.format(v))
            print('')
            v = n + v
        
        ggTCheck3 = ggT(n, v)
    
    print('> 0. Pre-Definitions: p={0}, q={1}, n={2}, Kpr=(s)=({3}), Kpub=(n,v)=({4},{5})'.format(p,q,n,s,n,v))
       
    x = k**2 % n
    #x = 6
    
    print('> 1. Commitment:      k={0} > ggT(k,n)={1}, x={2}'.format(k,ggTCheck,x))
    
    b = randint(0, 1)
    #b = 1
    
    print('> 2. Challenge:       b={0}'.format(b))
    
    if b == 0:
        y = k % n
    
    elif b == 1:
        y = (k * s) % n
        #y = 3
        
    print('> 3. Response:        y={0}'.format(y))
    
    if b == 0:
        check1 = y**2 % n
        
        check2 = x % n
        
    elif b == 1:
        check1 = y**2 % n
        
        vmi = ExtGCD(n, v)
        
        check2 = (x * vmi) % n
        
    print('> 4. Verification:    Check1={0}, Check2={1}'.format(check1,check2))

if __name__ == "__main__":
    main()