Pollard-Rho-Method.py running on Windows
--------------------------------------
> 0. Selected mode:                      encrypt
> 1. Pre-Definitions:                    p=179, q=139, x=100

> Note: d is smaller than 0! Original value of d=-3509. Additive inverse element must be calculated!

> 2. Calculated keys:                    Kpub=(n,e)=(24881,7), Kpr=(d)=(21055)
> 4. Encrypted text:                     y=21497


Pollard-Rho-Method.py running on Windows
--------------------------------------
> 0. Selected mode:                      decrypt
> 1. Pre-Definitions:                    Kpub=(n,e)=(24881,7), y=21497

Execution Pollard-Rho-Method for n=24881
Note: Values in parentheses are the predecessor values!

i        xi=f(xi-1))     yi=x2i=f(f(yi-1))       ggT(xi-yi,n)
-----------------------------------------------------------------
1        27 (2)          752 (2)                 ggT(27-752,24881)=ggT(-725,24881)=1
2        752 (27)        15656 (752)             ggT(752-15656,24881)=ggT(-14904,24881)=1
3        18145 (752)     14629 (15656)           ggT(18145-14629,24881)=ggT(3516,24881)=1
4        15656 (18145)   12296 (14629)           ggT(15656-12296,24881)=ggT(3360,24881)=1
5        7628 (15656)    21528 (12296)           ggT(7628-21528,24881)=ggT(-13900,24881)=139

> 2. Result of Pollard-Rho-Method:       p=139, q=179, n=24881

> Note: d is smaller than 0! Original value of d=-3509. Additive inverse element must be calculated!

> 3. Calcualation of Kpr:                Kpr=(d)=(21055)
> 4. Decrypted text:                     x=100


Pollard-Rho-Method.py running on Windows
--------------------------------------
> 0. Selected mode:                      encrypt
> 1. Pre-Definitions:                    p=179, q=139, x=100
> 2. Calculated keys:                    Kpub=(n,e)=(24881,5), Kpr=(d)=(4913)
> 4. Encrypted text:                     y=2647


Pollard-Rho-Method.py running on Windows
--------------------------------------
> 0. Selected mode:                      decrypt
> 1. Pre-Definitions:                    Kpub=(n,e)=(24881,5), y=2647

Execution Pollard-Rho-Method for n=24881
Note: Values in parentheses are the predecessor values!

i        xi=f(xi-1))     yi=x2i=f(f(yi-1))       ggT(xi-yi,n)
-----------------------------------------------------------------
1        27 (2)          752 (2)                 ggT(27-752,24881)=ggT(-725,24881)=1
2        752 (27)        15656 (752)             ggT(752-15656,24881)=ggT(-14904,24881)=1
3        18145 (752)     14629 (15656)           ggT(18145-14629,24881)=ggT(3516,24881)=1
4        15656 (18145)   12296 (14629)           ggT(15656-12296,24881)=ggT(3360,24881)=1
5        7628 (15656)    21528 (12296)           ggT(7628-21528,24881)=ggT(-13900,24881)=139

> 2. Result of Pollard-Rho-Method:       p=139, q=179, n=24881
> 3. Calcualation of Kpr:                Kpr=(d)=(4913)
> 4. Decrypted text:                     x=100