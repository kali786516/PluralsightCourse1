def convert(s):
    '''convert to an integer'''
    try:
        x=int(s)
        print("Conversion succeeded ! x=",x)
    except ValueError:
        print("Conversion failed!")
        x=-1
    return x


convert("kali")


convert(10)

