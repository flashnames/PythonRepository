import numpy
def square_digits(num):
    i=0
    num=str(num)
    List=list(num)
    while True:
        Num=List[i]
        List[i]=str(int(Num)*int(Num))
        i+=1
        if i==len(List):
            num=''.join(List)
            return int(num)
    pass

if __name__=='__main__':
    num=square_digits(9119)
    print(num)
