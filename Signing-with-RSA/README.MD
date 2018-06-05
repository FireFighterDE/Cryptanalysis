Signing-with-RSA.py running on Windows
--------------------------------------
> 0. Pre-Definitions:       p=13, q=4, x=14
> 1. Calculation of Kpub:   n=52, phi_n=36, Kpub=(n,e)=(52,7)

> Note: ine is smaller than 0! Original value of ine=-5. Additive inverse element must be calculated!

> 2. Calcualation of Kpr:   Kpr=(d)=(31)
> 3. Signature and message: s=40, x=14


Signing-with-RSA.py running on Windows
--------------------------------------
> 0. Pre-Definitions:       p=13, q=7, x=14
> 1. Calculation of Kpub:   n=91, phi_n=72, Kpub=(n,e)=(91,5)
> 2. Calcualation of Kpr:   Kpr=(d)=(29)
> 3. Signature and message: s=14, x=14


Signature-verification-with-RSA.py running on Windows
--------------------------------------
> 0. Pre-Definitions:       Kpub=(n,e)=(52,7), s=40, x=14
> 1. Calculated message:    x=40

> Verification result: failed


Signature-verification-with-RSA.py running on Windows
--------------------------------------
> 0. Pre-Definitions:       Kpub=(n,e)=(91,5), s=14, x=14
> 1. Calculated message:    x=14

> Verification result: passed