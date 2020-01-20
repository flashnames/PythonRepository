def alphanumeric(password):
    Strs=list(password)
    if len(Strs)==0:
        return False
    for Str in Strs:
        if Str>="a" and Str<="z" or Str>="0" and Str<="9" or Str>="A" and Str<="Z":
            pass
        else:
            return False
    return True



if __name__=="__main__":
    print(alphanumeric("     "))
