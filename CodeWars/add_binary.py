def add_binary(a,b):
    #your code here
    c=a+b
    c=''.join(bin(c))
    return c

if __name__=='__main__':
    pr=add_binary(1,1)
    print(pr)