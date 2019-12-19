def is_triangle(a, b, c):
    d=max(a,b,c)
    if a+b>d and a-b<d and b+c>d and b-c<d and c+a>d and c-a<d:
        return True
    else:
        return False

if __name__=="__main__":
    pr=is_triangle(1,2,2)
    print(pr)