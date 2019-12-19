#CHAR_TO_MORSE preloaded to convert characters into Morse code
def encryption(string):
    #your code here
    i=0
    Str=''
    List=[]
    List=list(string)
    if len(List)==0:
        return ''
    while True:
        Str=List[i]
        if Str=='A' or Str=='a':
            Str1=".-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='B' or Str=='b':
            Str1="-..."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='C' or Str=='c':
            Str1="-.-."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='D' or Str=='d':
            Str1="-.."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='E' or Str=='e':
            Str1="."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='F' or Str=='f':
            Str1="..-."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='G' or Str=='g':
            Str1="--."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='H' or Str=='h':
            Str1="...."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='I' or Str=='i':
            Str1=".."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='J' or Str=='j':
            Str1=".---"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='K' or Str=='k':
            Str1="-.-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='L' or Str=='l':
            Str1=".-.."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='M' or Str=='m':
            Str1="--"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='N' or Str=='n':
            Str1="-."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='O' or Str=='o':
            Str1="---"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='P' or Str=='p':
            Str1=".--."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='Q' or Str=='q':
            Str1="--.-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='R' or Str=='r':
            Str1=".-."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='S' or Str=='s':
            Str1="..."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='T' or Str=='t':
            Str1="-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='U' or Str=='u':
            Str1="..-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='V' or Str=='v':
            Str1="...-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='W' or Str=='w':
            Str1=".--"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='X' or Str=='x':
            Str1="-..-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='Y' or Str=='y':
            Str1="-.--"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='Z' or Str=='z':
            Str1="--.."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='1':
            Str1=".----"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='2':
            Str1="..---"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='3':
            Str1="...--"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='4':
            Str1="....-"
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='5':
            Str1="....."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='6':
            Str1="-...."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='7':
            Str1="--..."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='8':
            Str1="---.."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='9':
            Str1="----."
            Str1=Str1+" "
            List[i]=Str1
        elif Str=='0':
            Str1="-----"
            Str1=Str1+" "
            List[i]=Str1
        elif Str==' ':
            Str1="  "
            List[i]=Str1
        i+=1
        if i==len(List):
            break
    string=''.join(List)
    string=string.strip()
    return string