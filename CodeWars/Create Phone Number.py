def create_phone_number(n):
    List=[]
    ListCopy=[]
    List_Copy=[]
    for i in range(len(n)):
        if i<3:
            List.append(str(n[i]))
        else:
            if i<6:
                ListCopy.append(str(n[i]))
            else:
                List_Copy.append(str(n[i]))
    List="".join(List)
    ListCopy="".join(ListCopy)
    List_Copy="".join(List_Copy)
    return "("+List+")"+" "+ListCopy+"-"+List_Copy

if __name__=="__main__":
    pr=create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    print(pr)