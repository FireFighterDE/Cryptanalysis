#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Elliptic-Curve-Diffie-Hellman.py
description    : Key exchange according to Diffie-Hellman
author         : Sebastian Pflaum (240646)
usage          : python Elliptic-Curve-Diffie-Hellman.py aec bec p P
example        : python Elliptic-Curve-Diffie-Hellman.py 1 1 5 (2|1)
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

def main(aec,bec,p,P):
    system = platform.system()
    
    print('Elliptic-Curve-Diffie-Hellman.py running on {0}'.format(system))
    print('--------------------------------------')
    
    
    print('> 0. Pre-Definitions between Alice and Bob: aec={0}, bec={1}, p={2}'.format(aec,bec,p))
    
    checkpy = 1
    checkpx = 2
    
    if P != '0':
        px = int(P[1:-1].split('|')[0])
        py = int(P[1:-1].split('|')[1])
        
        checkpy = py**2 % p
        checkpx = (px**3 + aec * px + bec) % p
        
        if checkpy != checkpx:
            print('> Program abort: Point P({0}|{1}) is not on elliptic curve!'.format(px,py))
            sys.exit()        
    
    else:
        while checkpy != checkpx:
            px = randint(1,10)
            py = randint(1,10)
        
            checkpy = py**2 % p
            checkpx = (px**3 + aec * px + bec) % p
    
    print('> 1. Public point P on elliptic curve:      P({0}|{1})'.format(px,py))
    
    ak = randint(1,2)
    bk = randint(1,2)
    
    print('> 2. Alice and Bob choose private numbers:  ak={0}, bk={1}'.format(ak,bk))
    
    if ak == 2:
        m1 = 3 * px**2 + aec
        m2 = 2 * py
        
        inm2 = ExtGCD(p, m2)
        
        print('')
        
        if inm2 < 0:
            print('> Note: inm2 is smaller than 0! Original value of inm2={0}. Additive inverse element must be calculated!'.format(inm2))
            
            
            inm2 = p + inm2
        
        print('> Note: m1={0}, m2={1}'.format(m1,inm2))
        print('')
        
        m = m1 * inm2 % p
        
        ax = (m**2 - 2 * px) % p
        
        ay = (py - m * (px - ax)) % p
        
        may = 0 - ay

        nax = ax % p
        nay = may % p
        
        print('> 3. Point doubling at Alice side:          m={0}, Ak=({1}|{2})'.format(m,nax,nay))
        
    elif ak == 1:
        
        nax = px % p
        nay = py % p
        
        print('> 3. No point doubling at Alice side:       Ak=({0}|{1})'.format(nax,nay))
        
    if bk == 2:
        m1 = 3 * px**2 + aec
        m2 = 2 * py
        
        inm2 = ExtGCD(p, m2)
        
        print('')
        
        if inm2 < 0:
            print('> Note: inm2 is smaller than 0! Original value of inm2={0}. Additive inverse element must be calculated!'.format(inm2))
            
            
            inm2 = p + inm2
        
        print('> Note: m1={0}, m2={1}'.format(m1,inm2))
        print('')
        
        m = m1 * inm2 % p
        
        bx = (m**2 - 2 * px) % p
        
        by = (py - m * (px - bx)) % p
        
        mby = 0 - by

        nbx = bx % p
        nby = mby % p
        
        print('> 3. Point doubling at Bob side:            m={0}, Bk=({1}|{2})'.format(m,nbx,nby))
        
    elif bk == 1:
        
        nbx = px % p
        nby = py % p
        
        print('> 3. No point doubling at Bob side:         Bk=({0}|{1})'.format(nbx,nby))
        
    if ak == 1:
        
        print('> 4. K at Alice side:                       K = ak * Bk = 1 * Bk = Bk = ({0}|{1})'.format(nbx,nby))
        
    elif ak == 2:
        
        bx = (m**2 - 2 * px) % p
        
        by = (py - m * (px - bx)) % p
        
        mby = 0 - by

        nbx = bx % p
        nby = mby % p
        
        print('> 4. K at Alice side:                       K = ak * Bk = 2 * Bk = Bk * Bk = ({0}|{1})'.format(nbx,nby))
        
    if bk == 1:
        
        print('> 4. K at Bob side:                         K = bk * Ak = 1 * Ak = Ak = ({0}|{1})'.format(nax,nay))
        
    elif bk == 2:
        
        ax = (m**2 - 2 * px) % p
        
        ay = (py - m * (px - ax)) % p
        
        may = 0 - ay

        nax = ax % p
        nay = may % p
        
        print('> 4. K at Bob side:                         K = bk * Ak = 2 * Ak = Ak * Ak = ({0}|{1})'.format(nax,nay))
        
    if (nax==nbx and nay==nby):
        result = 'passed'
    else:
        result = 'failed'
        
    print('')
    print('> Verification result: {0}'.format(result))
    
if __name__ == "__main__":
    aec = int(sys.argv[1])
    if aec == 0:
        aec = randint(1,10)
        
    bec = sys.argv[2]
    if bec == 'NULL':
        bec = randint(1,10)
    else:
        bec = int(bec)
        
    p = int(sys.argv[3])
    if p == 0:
        n = 4
        p = generate_big_prime(n)
        
    P = sys.argv[4]
        
    main(aec,bec,p,P)