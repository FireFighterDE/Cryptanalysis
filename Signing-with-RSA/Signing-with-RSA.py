#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Signing-with-RSA.py
description    : Sign message x via RSA
author         : Sebastian Pflaum (240646)
usage          : python Signing-with-RSA.py p q x
example        : python Signing-with-RSA.py 11 5 10
python_version :3.6.3
"""

import sys
import platform
from random import randint

def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p

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

def main(p,q,x):
    system = platform.system()
    
    print('Signing-with-RSA.py running on {0}'.format(system))
    print('--------------------------------------')
    
    print('> 0. Pre-Definitions:       p={0}, q={1}, x={2}'.format(p,q,x))
    
    n = p * q
    sn = (p - 1) * (q - 1)
    
    ggTCheck = 0
    
    while ggTCheck != 1:
        e = randint(1, 10)
        
        ggTCheck = ggT(sn, e)
        
    print('> 1. Calculation of Kpub:   n={0}, sn={1}, Kpub=(n,e)=({2},{3})'.format(n,sn,n,e))
    
    ine = ExtGCD(sn, e)
    
    if ine < 0:
        print('')
        print('> Note: ine is smaller than 0! Original value of ine={0}. Additive inverse element must be calculated!'.format(ine))
        print('')
        
        ine = sn + ine
    
    print('> 2. Calcualation of Kpr:   Kpr=(d)=({0})'.format(ine))
    
    s = x**ine % n
    
    print('> 3. Signature and message: s={0}, x={1}'.format(s,x))
    
if __name__ == "__main__":
    p = int(sys.argv[1])
    if p == 0:
        n = 4
        p = generate_big_prime(n)
    
    q = int(sys.argv[2])
    if q == 0:
        n = 3
        q = generate_big_prime(n)
    x = int(sys.argv[3])
    
    main(p,q,x)