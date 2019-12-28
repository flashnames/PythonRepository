def rgb(r, g, b):
    #your code here :)
    r=bin(r)
    g=bin(g)
    b=bin(b)
    Str=''.join(r+b+g)
    return Str

if __name__=="__main__":
    Str=rgb(0,0,0)
    print(Str)