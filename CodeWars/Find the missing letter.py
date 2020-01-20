def find_missing_letter(chars):
    for i in range(len(chars)):
        char1=ord(chars[i])
        char2=ord(chars[i+1])
        if char2-char1==1:
            pass
        else:
            char3=chr(char1+1)
            return char3

if __name__=="__main__":
    print(find_missing_letter(["O","Q","R","S"]))
        