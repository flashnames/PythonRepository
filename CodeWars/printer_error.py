def printer_error(s):
    # your code
    i=0
    ErrorNum=0
    s=list(s)
    Count=len(s)
    while True:
        if ord(s[i])>=65 and ord(s[i])<=77 or ord(s[i])>=97 and ord(s[i])<=109:
            i+=1
        else:
            ErrorNum+=1
            i+=1
        if(i==len(s)):
            return  str(ErrorNum)+'/'+str(Count)

if __name__=='__main__':
    pr=printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")
    print(pr)