def Decrypt(etext,d,n):
    try:
        text = [chr(pow(char,d,n)) for char in etext]
        return "".join(text)
    except TypeError as e:
        print(e)

