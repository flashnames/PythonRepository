def rot13(message):
    List=list(message)
    for i in range(len(List)):
        if List[i]!=" ":
            if ord(List[i])>=65 and ord(List[i])<=90:
                if ord(List[i])<78:
                    Str=ord(List[i])+13
                    List[i]=chr(Str)
                else:
                    Str=abs(ord(List[i])-ord("N"))
                    Str=ord("A")+Str
                    List[i]=chr(Str)
            elif ord(List[i])>=97 and ord(List[i])<=122:
                if ord(List[i])<110:
                    Str=ord(List[i])+13
                    List[i]=chr(Str)
                else:
                    Str=abs(ord(List[i])-ord("n"))
                    Str=ord("a")+Str
                    List[i]=chr(Str)
    List="".join(List)
    return List


if __name__=="__main__":
    print(rot13("EBG13 rknzcyr."))