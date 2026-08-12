def var1():
    return 1,2

def pr(a,b,c=0):
    print(a,b,c)


e,f = var1()
pr(e,f,3)