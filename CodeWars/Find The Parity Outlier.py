def find_outlier(integers):
    for i in range(len(integers)):
        key=i
        for j in range(i+1,len(integers)):
            if integers[key]>integers[j]:
                key=j
        num=integers[i]
        integers[i]=integers[key]
        integers[key]=num
    for i in range(len(integers)):
        if integers[i]!=integers[i+1]:
            num=integers[i]
            return num


if __name__=="__main__":
    print(find_outlier([2, 4, 6, 8, 10, 3]))
    