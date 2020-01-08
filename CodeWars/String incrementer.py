def increment_string(strng):
    strng=strng.split("",strng.isdigit())
    List=list(strng)
    ListCopy=[]
    if len(List)==1:
        if List.isdigit():
            List=int(List)
            List+=1
            List=str(List)
            return List
        else:
            List.append("1")
            return List
if __name__=="__main__":
    pr=increment_string("foobar99")
    print(pr)