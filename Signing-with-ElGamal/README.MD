Signing-with-ElGamal.py running on Windows
--------------------------------------
> 0. Pre-Definitions:                       p=11, g=5, m=8 for letter I, Kpr=(d)=3
> 1. Public Key:                            Kpub=(p,g,e)=(11,5,4)
> 2. Random number:                         r=1 whereby ggT(r,p-1)=ggT(1,10)=1
> 3. Calculate multiplicative element of r: mir=1
> 4. Message identifier:                    rho=5
> 5. Signature element:                     s=3
> 6. Signed message:                        (m,rho,s)=(8,5,3))

Signing-with-ElGamal.py running on Windows
--------------------------------------
> 0. Pre-Definitions:                       p=11, g=5, m=8 for letter I, Kpr=(d)=3
> 1. Public Key:                            Kpub=(p,g,e)=(11,5,4)
> 2. Random number:                         r=9 whereby ggT(r,p-1)=ggT(9,10)=1

> Note: mir is smaller than 0! Original value of mir=-1. Additive inverse element must be calculated!

> 3. Calculate multiplicative element of r: mir=9
> 4. Message identifier:                    rho=9
> 5. Signature element:                     s=9
> 6. Signed message:                        (m,rho,s)=(8,9,9))

Signing-with-ElGamal.py running on Windows
--------------------------------------
> 0. Pre-Definitions:                       p=11, g=5, m=8 for letter I, Kpr=(d)=3
> 1. Public Key:                            Kpub=(p,g,e)=(11,5,4)
> 2. Random number:                         r=7 whereby ggT(r,p-1)=ggT(7,10)=1
> 3. Calculate multiplicative element of r: mir=3
> 4. Message identifier:                    rho=3
> 5. Signature element:                     s=7
> 6. Signed message:                        (m,rho,s)=(8,3,7))