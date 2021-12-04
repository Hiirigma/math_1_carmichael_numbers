import math
import threading
from mpmath.functions.functions import arg
from sympy.ntheory import factorint

G_D = 5
G_MAX = 1000000000000

def GenCarmichaelNumbers(dPrimeCount : int, dIndex : int):
	dBlock = 1000
	numPrime = 1
	f = open(f'{dPrimeCount}.txt', 'w')

	while numPrime < G_MAX:
		numPrime += 2
		lCarmichaelPrime = factorint(numPrime)
		if (len(lCarmichaelPrime) != dPrimeCount):
			continue

		if (all((dCnt == 1 and (numPrime - 1) % (cPrime - 1) == 0) for cPrime, dCnt in lCarmichaelPrime.items())):
			print(f"{numPrime} = {list(lCarmichaelPrime.keys())}")


	print(f'{dPrimeCount}: Completed')

def main():
	print('Generate Carmichael numbers')
	# threads = list()
	# dPrimeCount = 3
	# lIdx = [1,4 * (10 ** 4) + 1,8 * (10 ** 5) + 1, 3 * (10 ** 8) + 1, 5 * (10 ** 9) + 1, 2 * (10**11) + 1]
	# while dPrimeCount != 9:
	# 	t1 = threading.Thread(target=GenCarmichaelNumbers, args=(dPrimeCount,lIdx[dPrimeCount - 3],))
	# 	threads.append(t1)
	# 	t1.start()
	# 	dPrimeCount+=1

	# for t1 in threads:
	# 	t1.join()
	GenCarmichaelNumbers(G_D, 1)
	return 0


if __name__ == "__main__":
	main()