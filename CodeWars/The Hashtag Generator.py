def generate_hashtag(s):
    if len(s)>140:
        return False
    s=s.strip()
    ss=s.split(" ")
    if len(s)==0:
        return False
    for i in range(len(ss)):
        if i==0:
            Str="#"+ss[i].title()
            ss[i]=Str
        else:
            Str=ss[i].title()
            ss[i]=Str
    ss="".join(ss)
    return ss

if __name__=="__main__":
    print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
    
