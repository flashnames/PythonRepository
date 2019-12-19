def DNA_strand(dna):
    # code here
    i=0
    dna_1=list(dna)
    while True:
        if dna_1[i]=='A':
            dna_1[i]='T'
        elif dna_1[i]=='T':
            dna_1[i]='A'
        elif dna_1[i]=='G':
            dna_1[i]='C'
        elif dna_1[i]=='C':
            dna_1[i]='G'
        i+=1
        if i==len(dna_1):
            dna_1=''.join(dna_1)
            return dna_1
if __name__=='__main__':
        Pr=DNA_strand("AAAA")
        print(Pr)