def divisibleSumPairs(n, k, ar):
    contador = 0

    for i in range(n):
        for a in range(i+1, n):
            if (ar[i]+ar[a]) % k == 0:
                contador +=1

    return contador