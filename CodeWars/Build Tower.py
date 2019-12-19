def tower_builder(n_floors):
    # build here
    List=[]
    Str='*'
    Num=0
    if n_floors<=1:
        return List.append(Str)
    while True:
        if Num==0:
            List.insert(Num,Str)
            Num+=1
        else:
            Str=Str+'**'
            List.insert(Num,Str)
            Num+=1
        if Num==n_floors:
            break
    return List
    
if __name__=='__main__':
    pr=tower_builder(9)
    print(pr)