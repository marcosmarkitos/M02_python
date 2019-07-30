def retrocontador (e):
    print(" {}," .format(e), end="")
    if e > 0:
        retrocontador (e-1)

def sumatorio (n):
    if n>0:
        return (n+sumatorio(n-1))
    else:
        return (0)
    


retrocontador(10)
sumatorio (4)