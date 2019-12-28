def spin_words(sentence):
    # Your code goes here
    List1=[]
    List=sentence.split(' ')
    for Str in List:
        if len(Str)<=4:
            List1.append(Str)
        else:
            Str1=list(Str)
            Str1.reverse()
            Str1=''.join(Str1)
            List1.append(Str1)
        sentence=' '.join(List1)
    return sentence

