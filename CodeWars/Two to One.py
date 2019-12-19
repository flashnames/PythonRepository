def longest(s1, s2):
    # your code
    i=0
    j=0
    Str=''
    Str1=''
    List1=[]
    List2=[]
    List3=[]
    List1=list(s1)
    List2=list(s2)
    if len(List1)==0 or len(List2)==0:
        return ""
    if s1==s2:
        return s1
    else:
        while True:
            Str=List1[i]
            while True:
                if Str==List2[j]:
                    List3.append(Str)
                    flag=True
                    j+=1
                    break
                j+=1
                if j==len(List2):
                    break
            i+=1
            j=0
            flag=False
            if i==len(List1):
                break
        i=0
        j=0
        while True:
            Str=List2[i]
            while True:
                if Str!=List3[j]:
                    List3.append(Str)
                    j+=1
                j+=1
                if j==(len(List3)-1):
                    break
            i+=1
            j=0
            if i==len(List3):
                break
    List3=''.join(List3)
    return List3

if __name__=="__main__":
    pr=longest("aretheyhere","yestheyarehere")
    print(pr)




