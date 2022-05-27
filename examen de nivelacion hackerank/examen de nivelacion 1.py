#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    grupo = []
    soporta =  {'{':'}', '(':')', '[':']'}
    
    for i in s:                                         # para i en s, variable con mierda que recibo
        if i in ['{','(','['] :                         # si i esta en abiertos
            grupo.append(i)                             # me deja una lista de i
        else:                                           # entonces
            if grupo:                                   # si lista de abiertos
                ta = grupo.pop()                        # dame 1 de abierto y eliminalo
                if soporta[ta] != i:                    # si el que elimine de grupo no esta en soporta que es de abierto y cerrado en sintonia,
                    return 'NO'                         # decime que "NO"
            else:                                       # si no hay grupo
                return 'NO'                             # decime que no
            
    return "NO" if grupo else "YES"                     # decime que "NO", Si Hay grupo decime que "YES"
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()