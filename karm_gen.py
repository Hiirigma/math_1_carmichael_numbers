import math
from mpmath.functions.functions import arg
from sympy.ntheory import factorint

G_D = 3

def is_prime(n):
	""""pre-condition: n is a nonnegative integer
	post-condition: return True if n is prime and False otherwise."""
	if n < 2: 
		 return False;

	k = 3
	while k*k <= n:
		 if n % k == 0:
			 return False
		 k += 2
	return True

def GenCarmichaelNumbers(dPrimeCount : int):
	numPrime = 1
	dBlock = 10**3

	while (numPrime):
		# https://arxiv.org/pdf/1305.1867.pdf
		# Corollary 2.16

		# Carmichael numbers is odd 
		sqr = math.isqrt(numPrime)
		if (sqr * sqr == numPrime):
			numPrime += 2
			continue

		lCarmichaelPrime = factorint(numPrime)

		bCarmichael = True
		for cPrime, dCnt in lCarmichaelPrime.items():
			if (dCnt != 1):
				bCarmichael = False
				break
			if ((numPrime - 1) % (cPrime - 1) != 0):
				bCarmichael = False
				break

		if (bCarmichael == True and len(lCarmichaelPrime) == dPrimeCount):
			if (len([*filter(lambda x: x >= dBlock, lCarmichaelPrime)]) == 0):
				print(f"{numPrime} = {list(lCarmichaelPrime.keys())}")
			else:
				print (f"Number:{numPrime}. With 1000 factor")
				return True
		
		numPrime += 2


# def GenCarmichaelNumbers(numPrime : int):
# 	# dIdx = numPrime
# 	dThreadId = numPrime
# 	numPrimeBlock = 100000 ** (numPrime + 1) + 1
# 	numPrime = 100000 ** numPrime + 1

# 	dBlock = 10**3
# 	while (numPrime < numPrimeBlock):
# 		start = datetime.datetime.now()
# 		# https://arxiv.org/pdf/1305.1867.pdf
# 		# Corollary 2.16
# 		# Carmichael numbers is odd 
# 		if (is_prime(numPrime) == True):
# 			numPrime+=2
# 			continue

# 		k = 1
# 		dSum = 0
# 		bIsCarm = True

# 		while k < numPrime:
# 			# НОД = 1
# 			if (math.gcd(k, numPrime) == 1):
# 			# a^(n-1) 	
# 				dPow = pow(k, numPrime - 1, numPrime)
# 				dSum += dPow
# 				if (dPow != 1):
# 					bIsCarm = False
# 					break
# 			k += 1

# 		if (bIsCarm == True):
# 			if (dSum == phi(numPrime)):
# 				lCarmichaelPrime = factorint(numPrime, multiple=True)
# 				if (len([*filter(lambda x: x >= dBlock, lCarmichaelPrime)]) == 0):
# 					end = datetime.datetime.now()
# 					print (f"{dThreadId}: Carmichael number is: {numPrime} = {lCarmichaelPrime}")
# 					print(f"{dThreadId}: Time: {(end - start)}")
# 				else:
# 					print (f"{dThreadId}: Number:{numPrime}. With 1000 factor")

# 		numPrime += 2

# 	return True

def main():
	print('Generate Carmichael numbers')
	GenCarmichaelNumbers(G_D)
	return 0


if __name__ == "__main__":
	main()