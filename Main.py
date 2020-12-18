import My_Math
import Create_key
import Encrypt
import Decrypt
def main():
    p,q,n,phi,e,d = Create_key.Create_key()
    print("P =",p,"Q =",q,"=> phi =",phi)
    print("Public key :",e,n)
    print("Private key : ",d,n)
    text = input("Nhập văn bản cần mã hoá : ")
    etext=Encrypt.Encrypt(text,e,n)
    print("Văn bản đã được mã hoá : ",''.join(map(str,etext)))
    dtext=Decrypt.Decrypt(etext,d,n)
    print("Văn bản đã được giải mã : ",dtext)
main()