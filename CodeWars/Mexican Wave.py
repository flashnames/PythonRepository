def wave(Str):
    # Code here
    List1=[]
    List=list(Str)
    for i in range(0,len(List)):
        if List[i]==' ':
            continue
        if List[i]!=' ' and i==0:
            Str1=chr(ord(List[i])-ord(' '))
            List[i]=Str1
            Str2=''.join(List)
            List1.append(Str2)
        else:
            if List[i-1]!=' ':
                Str3=chr(ord(List[i-1])+ord(' '))
                List[i-1]=Str3
            elif List[i-2]!=' ':
                Str3=chr(ord(List[i-2])+ord(' '))
                List[i-2]=Str3
            Str1=chr(ord(List[i])-ord(' '))
            List[i]=Str1
            Str2=''.join(List)
            List1.append(Str2)
    return List1

if __name__=='__main__':
    pr=wave(" gap ")
    print(pr)