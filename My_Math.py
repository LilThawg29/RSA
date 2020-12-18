def GCD(a, b):
    if (b == 0): return a;
    return GCD(b, a % b);

def Euclid_extened(e, phi):
    tmp_phi = phi
    tmp_e = e
    r = tmp_phi%tmp_e
    y1=1
    x1=-(tmp_phi/tmp_e)
    x2=1
    y2=0
    while(r>0):
        tmp_phi=tmp_e
        tmp_e = r
        r = tmp_phi%tmp_e
        k = -(tmp_phi//tmp_e)
        x=int(k*x1+x2)
        y=int(k*y1+y2)
        x2=x1
        y2=y1
        x1=x
        y1=y
        if r==1:
            if x>0 : return x
            else : return x+phi

def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

