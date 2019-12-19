# return masked string
def maskify(cc):
    i=0
    List=list(cc)
    while True:
        if(len(List)<=4):
            List=''.join(List)
            return List
        List[i]="#"
        i+=1
        if(i==((len(cc)-4))):
            break
    List=''.join(List)
    return List


if __name__=="__main__":
    List=maskify('')
    print(List)
