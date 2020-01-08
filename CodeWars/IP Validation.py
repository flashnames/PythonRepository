def is_valid_IP(strng):
    List=[]
    Ipadds=strng.split(".")
    if len(Ipadds)!=4:
        return False
    for Ipadd in Ipadds:
        if Ipadd.isdigit():
            List=list(Ipadd)
            for i in range(len(List)):
                if len(List)!=0:
                    if int(List[0])==0:
                        return False
        else:
            return False
    for Ipadd in Ipadds:
        if int(Ipadd)>=0 and int(Ipadd)<256:
            pass
        else:
            return False
    return True

if __name__=="__main__":
    Result=is_valid_IP('abc.def.ghi.jkl')
    print(Result)