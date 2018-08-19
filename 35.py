# How many circular primes below 1,000,000? Circular if all rotations of digits are prime.
# ====================================================================================

# Want to grasp this one:

def compute():
	isprime = eulerlib.list_primality(999999)
	def is_circular_prime(n):
		s = str(n)
		return all(isprime[int(s[i : ] + s[ : i])] for i in range(len(s)))

	ans = sum(1
		for i in range(len(isprime))
		if is_circular_prime(i))
	return str(ans)


if __name__ == "__main__":
	print(compute())
