def camel_case(string):
    #your code here
    string=string.split(" ")
    List=[]
    for Str in string:
        List.append(Str.title())
    List="".join(List)
    return List

if __name__=="__main__":
    print(camel_case("hello world"))
