
def staircase(n):
    c=1
    i=1
    b = " "
    d = "#"

    for i in range(n):
        print((b * (n-1)+d*c))
        c +=1
        n -=1
        i+1