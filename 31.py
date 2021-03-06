# How many ways to make 2 pounds (200 cents) out of combo of (any number of) 8 types of coin?
# ====================================================================================

# I do not get this one. There is something fairly deep going on here...



# We use the standard dynamic programming algorithm to solve the subset sum problem over integers.
# The order of the coin values does not matter, but the values need to be unique.
def compute():
	TOTAL = 200

	# At the start of each loop iteration, ways[i] is the number of ways to use {any copies
	# of the all the coin values seen before this iteration} to form an unordered sum of i
	ways = [1] + [0] * TOTAL
	for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
		for i in range(len(ways) - coin):
			ways[i + coin] += ways[i]
	return str(ways[-1])


if __name__ == "__main__":
	print(compute())

# lista = [1, 2]
alist = [1, 2, 3]
print(alist[-1])
