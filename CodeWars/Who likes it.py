def likes(names):
    #your code here
    if len(names)==0:
        return "no one likes this"
    List=[]
    i=0
    count=0
    while True:
        Str=names[i]
        Str=''.join(Str)
        List.insert(i,Str)
        i+=1
        if i==len(names):
             break
    i=0
    while True:
        Str=List[i]
        count+=1
        i+=1
        if i==len(List):
            break
    if count==1:
        return Str+" likes this"
    if count==2:
        Str1=List[0]
        Str2=List[1]
        return Str1+" and "+Str2+" like this"  
    if count==3:
        Str1=List[0]
        Str2=List[1]
        Str3=List[2]
        return Str1+", "+Str2+" and "+Str3+" like this"
    if count>=4:
        Str1=List[0]
        Str2=List[1]
        return Str1+", "+Str2+" and "+str(len(List)-2)+" others like this"


if __name__=="__main__":
    pr=likes(["Alex", "Jacob", "Mark"])
    print(pr)
        
