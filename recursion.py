def fi(n):
    if n==1:
        return 1
    s= n + fi(n-1)
    return s


r=fi(5)
print(r)

