def toJadenCase(string):
    # ...
    i=0
    j=0
    List=list(string)
    while True:
        if i==0:
             if ord(List[i])>=97 and ord(List[i])<=122: #判断是不是小写
                Str1=ord(List[i])-ord(' ')
                Str2=chr(Str1)
                List[i]=Str2
                i+=1
        if ord(List[i])>=65 and ord(List[i])<=90: #判断是不是大写
            i+=1
        elif ord(List[i])!=32: # 是不是空格
            i+=1
        if ord(List[i])==32: #是空格
            if ord(List[i+1])>=97 and ord(List[i+1])<=122:#空格后是不是大写
                Str1=ord(List[i+1])-ord(' ')
                Str2=chr(Str1)
                List[i+1]=Str2
            i+=1
        if (i+1)==(len(List)-1):
            string=''.join(List)
            return string
if __name__=='__main__':
    List=toJadenCase("if i can speak english so i can walk on sheets")
    print(List)