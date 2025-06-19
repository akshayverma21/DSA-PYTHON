def printN(n):
    if n>=0:
        printN(n-1)
        print(n, end='  ')

def p_reversed(n):
    if n!=0:
        print(n,end=" ")
        p_reversed(n-1)
    
def printodd(n):
    if n>0:
        printodd(n-1)
        print(2*n-1,end=" ")

def printeven(n):
    if n>0:
        printeven(n-1)
        print(2*n,end=" ")
    
    
def printOddreverse(n):
    if n>0:
        print(2*n-1,end=" ")
        printOddreverse(n-1)
    

def printevenreverse(n):
    if n>0:
        print(2*n,end=" ")
        printevenreverse(n-1)
    


printevenreverse(10)
