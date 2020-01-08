def unique_in_order(iterable):
    List=[]
    ListCopy=[]
    List=list(iterable)
    ListCopy=List[:]
    for i in range(len(List)):
        Str=List[i]
        for j in range(i+1,len(List)):
            if Str==ListCopy[j]:
                Str=ListCopy[j]
            del ListCopy[i]
    return ListCopy

if __name__=="__main__":
    pr=unique_in_order('AAAABBBCCDAABBB')
    print(pr)