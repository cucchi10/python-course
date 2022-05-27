n=4
def fibonaccin(n):
    fibo =0
    if n == 0 or n == 1:
        fibo =+1
    else:
        fibo =+ fibonaccin(n-2) + fibonaccin(n-1)

    return fibo

print(fibonaccin(n))