#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Signing-with-ElGamal.py
description    : m = default means letter I, which results in m = 8, 
                 setting value of p, g or d to '0' results in default values
author         : Sebastian Pflaum (240646)
usage          : python Signing-with-ElGamal.py p g m d
example        : python Signing-with-ElGamal.py 11 5 default 3
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

def main(p,g,m,d):
    system = platform.system()
    
    alphabet = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}
    
    print('Signing-with-ElGamal.py running on {0}'.format(system))
    print('--------------------------------------')
    
    key = int(list(alphabet.keys())[list(alphabet.values()).index('{0}'.format(m))])
    
    print('> 0. Pre-Definitions:                       p={0}, g={1}, m={2} for letter {3}, Kpr=(d)={4}'.format(p,g,key,m,d))
    
    e = g**d % p
    
    print('> 1. Public Key:                            Kpub=(p,g,e)=({0},{1},{2})'.format(p,g,e))
    
    
    ggTCheck = 0
    
    while ggTCheck != 1:
        r = randint(1, p-1)
        
        ggTCheck = ggT(r, p-1)
        
    print('> 2. Random number:                         r={0} whereby ggT(r,p-1)=ggT({1},{2})=1'.format(r,r,p-1))
    
    mir = ExtGCD(p-1, r)
    if mir < 0:
        print('')
        print('> Note: mir is smaller than 0! Original value of mir={0}. Additive inverse element must be calculated!'.format(mir))
        print('')
        
        mir = (p-1) + mir
    
    print('> 3. Calculate multiplicative element of r: mir={0}'.format(mir))
    
    rho = g**r % p
    
    print('> 4. Message identifier:                    rho={0}'.format(rho))
    
    s = ((key - (d * rho)) * mir) % (p-1)
    
    print('> 5. Signature element:                     s={0}'.format(s))
    
    print('> 6. Signed message:                        (m,rho,s)=({0},{1},{2}))'.format(key,rho,s))

if __name__ == "__main__":
    p = int(sys.argv[1])
    if p == 0:
        n = 4
        p = generate_big_prime(n)
    
    g = int(sys.argv[2])
    if g == 0:
        n = 3
        g = generate_big_prime(n)
        
    m = sys.argv[3]
    if m == 'default':
        m = 'I'
     
    d = int(sys.argv[4])
    if d == 0:
        d = randint(1, 10)
        
    main(p,g,m,d)