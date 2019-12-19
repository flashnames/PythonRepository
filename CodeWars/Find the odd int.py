def find_it(seq):
    i=0
    j=0
    List=[]
    List=seq
    Num_count=0
    while True:
        Num=List[i]
        Num_count+=1
        j=i+1
        while True:
            if List[j]==Num:
                Num_count+=1
                i+=1
            j+=1
            if j==(len(List)-1):
                break
        if Num_count%2!=0:
            return Num
        else:
            flag=-1
            Num_count=0
            i+=1
        if i==len(List):
            break

if __name__=="__main__":
    pr=find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    print(pr)