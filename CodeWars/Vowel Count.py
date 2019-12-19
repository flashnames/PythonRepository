def getCount(inputStr):
    i=0
    num_vowels = 0
    List=list(inputStr)
    if len(List)==0:
        return 0
    # your code here
    while True:
        if List[i]=='a' or List[i]=='e' or List[i]=='i' or List[i]=='o' or List[i]=='u':
            num_vowels+=1
        i+=1
        if i==len(List):
            break
    return num_vowels


if __name__=='__main__':
    pr=getCount('abracadabra')
    print(pr)