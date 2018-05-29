Signing-with-ElGamal.py running on Windows
--------------------------------------
> 0. Pre-Definitions:                       p=11, g=5, m=8 for letter I, Kpr=(d)=3
> 1. Public Key:                            Kpub=(p,g,e)=(11,5,4)
> 2. Random number:                         r=9 whereby ggT(r,p-1)=ggT(9,10)=1

> Note: mir is smaller than 0! Original value of mir=-1. Additive inverse element must be calculated!

> 3. Calculate multiplicative element of r: mir=9
> 4. Message identifier:                    rho=9
> 5. Signature element:                     s=9
> 6. Signed message:                        (m,rho,s)=(8,9,9)

Signature-verification-with-ElGamal.py running on Windows
--------------------------------------
> 0. Pre-Definitions:     Kpub=(p,g,e)=(11,5,4), sigN=(m,rho,s)=(8,9,9)
> 1. Verification Step 1: A=4
> 2. Verification Step 2: B=4

> Verification result:    passed