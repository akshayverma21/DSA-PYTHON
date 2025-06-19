def sumN(n):
    if n==0:
        return 0
    return n + sumN(n-1)

def sumNodd(n):
    if n==0:
        return 0
    return 2*n-1 + sumNodd(n-1)

def sumNeven(n):
    if n==1:
        return 2
    return 2*n + sumNeven(n-1)


def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

def square(n):
    if n==1:
        return 1
    return n*n + square(n-1)


print(square(5))



    
