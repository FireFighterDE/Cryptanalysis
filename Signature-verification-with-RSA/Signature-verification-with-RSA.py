#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title          : Signature-verification-with-RSA.py
description    : Verify signature
author         : Sebastian Pflaum (240646)
usage          : python Signature-verification-with-RSA.py n e s x
example        : python Signature-verification-with-RSA.py 91 5 82 10
python_version :3.6.3
"""

import sys
import platform

def main(n,e,s,x):
    system = platform.system()
    
    print('Signature-verification-with-RSA.py running on {0}'.format(system))
    print('--------------------------------------')
    
    print('> 0. Pre-Definitions:       Kpub=(n,e)=({0},{1}), s={2}, x={3}'.format(n,e,s,x))
    
    cx = s**e % n
    
    print('> 1. Calculated message:    x={0}'.format(cx))
    
    if cx==x:
        result = 'passed'
    else:
        result = 'failed'
        
    print('')
    print('> Verification result: {0}'.format(result))
    
if __name__ == "__main__":
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    s = int(sys.argv[3])
    x = int(sys.argv[4])
    
    main(n,e,s,x)