def Encrypt(text,e,n):
    etext = [pow(ord(char),e,n) for char in text]
    return etext





