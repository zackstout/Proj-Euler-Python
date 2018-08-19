# How many circular primes below 1,000,000? Circular if all rotations of digits are prime.
# ====================================================================================

# Want to grasp this one:

import eulerlib

def compute():
	isprime = eulerlib.list_primality(999999) # List of True, False,.... for whether each number is prime.
	def is_circular_prime(n):
		s = str(n)
		# Returns true if all elements pass a test:
		return all(isprime[int(s[i : ] + s[ : i])] for i in range(len(s))) # Cycling

	ans = sum(1 # Ahhh instead of i for i in .... we're just adding 1 each time
		for i in range(len(isprime))
		if is_circular_prime(i))
	return str(ans)


if __name__ == "__main__":
	print(compute())

	# n = 125
	# s = str(n)
	# print(int(s[2: ] + s[ : 2]))
