import random
import My_Math
def Create_key():
    p = random.randrange(1, 1000, 2)
    while My_Math.is_prime(p) is False:
        p = random.randrange(1, 1000, 2)
    q = random.randrange(1, 1000, 2)
    while My_Math.is_prime(q) is False:
        q = random.randrange(1, 1000, 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi, 2)
    e1 = My_Math.GCD(e, phi)
    while e1 != 1:
        e = random.randrange(1, phi, 2)
        e1 = My_Math.GCD(e, phi)
    d = My_Math.Euclid_extened(e,phi)
    return p,q,n,phi,e,d


