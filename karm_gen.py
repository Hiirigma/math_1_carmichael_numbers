import math
import datetime
from sympy.ntheory import factorint

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True

# def GenCarmichaelNumbers():
# 	numPrime = 3
# # use KORSELT’S CRITERION
# 	dBlock = 10**3

# 	while (numPrime):
# 		start = datetime.datetime.now()
# 		# Carmichael numbers if odd 
# 		if (numPrime % 2 == 0):
# 			numPrime+=1
# 			continue

# 		if (math.isqrt(numPrime) == True):
# 			numPrime+=1
# 			continue

# 		# https://arxiv.org/pdf/1305.1867.pdf
# 		# Corollary 2.16
# 		if (is_prime(numPrime) == True):
# 			numPrime+=1
# 			continue

# 		k = 1
# 		dSum = 0
# 		while k < numPrime:
# 			if (math.gcd(k,numPrime) == 1):
# 				dSum += pow(k, numPrime - 1, numPrime)
# 			k += 1
# 		# bIsCarm = True
# 		# while k < numPrime:
# 		# 	if (math.gcd(k, numPrime) == 1):
# 		# 		if (pow(k,numPrime - 1, numPrime) != 1):
# 		# 			bIsCarm = False
# 		# 	k += 1

# 		#if (bIsCarm == True):
# 		if (dSum == phi(numPrime)):
# 			lCarmichaelPrime = factorint(numPrime, multiple=True)
# 			if (len(lCarmichaelPrime) <= 8):
# 				if (len([*filter(lambda x: x >= dBlock, lCarmichaelPrime)]) == 0):
# 					end = datetime.datetime.now()
# 					print (f"Carmichael number is: {numPrime} = {lCarmichaelPrime}")
# 					print(f"Time: {(end - start).microseconds}")

# 		numPrime += 1
# 	return True

def GenCarmichaelNumbers():
	numPrime = 3
# use KORSELT’S CRITERION
	dBlock = 10**3
	start = datetime.datetime.now()
	end = datetime.datetime.now()

	lCarmichaelPrime = factorint(numPrime, multiple=True)
	if (len(lCarmichaelPrime) <= 8):
		if (len([*filter(lambda x: x >= dBlock, lCarmichaelPrime)]) == 0):
			end = datetime.datetime.now()
			print (f"Carmichael number is: {numPrime} = {lCarmichaelPrime}")
			print(f"Time: {(end - start).microseconds}")

		numPrime += 1
	return True


def main():
	print(f'Generate Carmichael numbers')	
	GenCarmichaelNumbers()

	return 0


if __name__ == "__main__":
	main()