def is_pangram(s):
    count=0
    List=s.split(' ')
    for Data in List:
        Data=list(Data)
        for Str in Data:
            if Str>='A' and Str<='Z' or Str>='a' and Str<='z':
                count+=1
            if count==0:
                return False
                
    return True

if __name__=="__main__":
    print(is_pangram('The quick, brown fox jumps over the lazy dog!'))