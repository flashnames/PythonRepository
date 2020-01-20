def two_sum(numbers, target):
    # start coding!
    if len(numbers)==1:
        return 0
    for i in range(len(numbers)):
        key=i
        for j in range(i+1,len(numbers)):
            if numbers[key]+numbers[j]==target:
                return [key,j]


if __name__=="__main__":
    print(two_sum([1234,5678,9012],14690))