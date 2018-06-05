#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Pollard-Rho-Method.py
description    : Calculation of RSA encrypt/decrypt with Pollard-Rho-Method
author         : Sebastian Pflaum (240646)
usage          : python Pollard-Rho-Method.py <encrypt/decrypt> Kpub y p q x
example        : python Pollard-Rho-Method.py decrypt (24881,5) 2647 0 0 0
                 python Pollard-Rho-Method.py encrypt 0 0 139 179 100
python_version :3.6.3
"""

import sys
import platform
import math
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

def rho(n):
    x = y = 2
    p = 1
    i = 1
    
    print('')
    print('Execution Pollard-Rho-Method for n={0}'.format(n))
    print('Note: Values in parentheses are the predecessor values!')
    print('')
    print('i \t xi=f(xi-1)) \t yi=x2i=f(f(yi-1)) \t ggT(xi-yi,n)')
    print('-----------------------------------------------------------------')
    
    while p <= 1:
        xi = x
        yi = y
        
        x = (x**2 + 23) % n
        y = (y**2 + 23) % n
        y = (y**2 + 23) % n
     
        p = math.gcd(x - y, n)
        
        print('{0} \t {1} ({2}) \t {3} ({4}) \t\t ggT({5}-{6},{7})=ggT({8},{9})={10}'.format(i,x,xi,y,yi,x,y,n,x-y,n,p))
        
        i = i + 1
    
    print('')
    
    return p

def main(mode,Kpub,y,p,q,x):
    system = platform.system()
    
    print('Pollard-Rho-Method.py running on {0}'.format(system))
    print('--------------------------------------')
    print('> 0. Selected mode: \t\t\t {0}'.format(mode))
    
    
    if mode == 'encrypt':
        print('> 1. Pre-Definitions: \t\t\t p={0}, q={1}, x={2}'.format(p,q,x))
        
        n = p * q
        phi_n = (p - 1) * (q - 1)
        
        ggTCheck = 0
    
        while ggTCheck != 1:
            e = randint(1, 10)
            
            ggTCheck = ggT(phi_n, e)
        
        d = ExtGCD(phi_n, e)
    
        if d < 0:
            print('')
            print('> Note: d is smaller than 0! Original value of d={0}. Additive inverse element must be calculated!'.format(d))
            print('')
            
            d = phi_n + d
        
        print('> 2. Calculated keys: \t\t\t Kpub=(n,e)=({0},{1}), Kpr=(d)=({2})'.format(n,e,d))
        
        y = x**e % n
        
        print('> 4. Encrypted text: \t\t\t y={0}'.format(y))
        
    if mode == 'decrypt':
        n = int(Kpub[1:-1].split(',')[0])
        e = int(Kpub[1:-1].split(',')[1])
        
        print('> 1. Pre-Definitions: \t\t\t Kpub=(n,e)=({0},{1}), y={2}'.format(n,e,y))
        
        p = rho(n)
        
        q = int(n / p)
        
        print('> 2. Result of Pollard-Rho-Method: \t p={0}, q={1}, n={2}'.format(p,q,n))
        
        phi_n = (p - 1) * (q - 1)
        
        d = ExtGCD(phi_n, e)
    
        if d < 0:
            print('')
            print('> Note: d is smaller than 0! Original value of d={0}. Additive inverse element must be calculated!'.format(d))
            print('')
            
            d = phi_n + d
    
        print('> 3. Calcualation of Kpr: \t\t Kpr=(d)=({0})'.format(d))
        
        x = y**d % n
        
        print('> 4. Decrypted text: \t\t\t x={0}'.format(x))
        
        
if __name__ == "__main__":
    mode = sys.argv[1]
    
    Kpub = sys.argv[2]
    if mode == 'encrypt':
        Kpub = '0'
    
    y = int(sys.argv[3])
    if mode == 'encrypt':
        y == 0
        
    p = int(sys.argv[4])
    if p == 0:
        n = 4
        p = generate_big_prime(n)
    
    q = int(sys.argv[5])
    if q == 0:
        n = 3
        q = generate_big_prime(n)
        
    x = int(sys.argv[6])
    if mode == 'decrypt':
        x == 0
    
    main(mode,Kpub,y,p,q,x)