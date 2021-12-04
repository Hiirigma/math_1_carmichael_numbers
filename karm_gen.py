import threading
import os
import datetime
from mpmath.functions.functions import arg
from sympy.ntheory import factorint

G_D = 6
G_MAX = 10000000000000000

file_array = []

def GenCarmichaelNumbers(numPrime : int, maxNum : int):
    start = datetime.datetime.now()
    locPrime = numPrime
    while numPrime < G_MAX:
        numPrime += 2
        lCarmichaelPrime = factorint(numPrime)
        dLen = len(lCarmichaelPrime)
        if (dLen < 3 or dLen > 8):
            continue

        # Corselt's Criterio
        if (all((dCnt == 1 and (numPrime - 1) % (cPrime - 1) == 0) for cPrime, dCnt in lCarmichaelPrime.items())):
            end = datetime.datetime.now()
            file_array[dLen-3].write(f"time: {(end - start).seconds}: {numPrime} = {list(lCarmichaelPrime.keys())}" + os.linesep)
            file_array[dLen-3].flush()
            start = datetime.datetime.now()

    
    print(f'end for {numPrime}')

def main():
    print('Generate Carmichael numbers')

    for i in range(3,9):
        file_array.append(open(f'{i}.txt', 'w'))

    threads = list()
    dPrimeCount = 3
    lIdx = [1,4 * (10 ** 4) + 1,8 * (10 ** 4) + 1, 321197185 - 2, 5394826801 - 2, 232250619601 - 2, 10**19 + 1, 10**22 + 1]
    while dPrimeCount != 9:
        t1 = threading.Thread(target=GenCarmichaelNumbers, args=(lIdx[dPrimeCount - 3],lIdx[dPrimeCount - 2],))
        threads.append(t1)
        t1.start()
        dPrimeCount+=1

    for t1 in threads:
        t1.join()

    return 0

if __name__ == "__main__":
    main()
