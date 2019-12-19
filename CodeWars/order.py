def order(sentence):
    # code here
    i=0
    j=0
    k=0
    num=0
    Str1=''
    List1=[]
    List2=[]
    List3=list(sentence)
    while True:
        Str1=List3[i]
        List2.append(Str1)
        if List3[i]==' ':
            while True:
                if List2[k]!=str(1):
                    k+=1
                else:
                    Str2=''.join(List2)
                    List1.append(Str2)
                    break
                if k==len(List2):
                    k=0
                    break
            i+=1
        else:
            i+=1
            continue
    return List1
if __name__=='__main__':
    List1=[]
    List1=order("is2 Thi1s T4est 3a")
    print(List1)




    #False