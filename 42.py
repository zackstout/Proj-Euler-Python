# How many words are triangular, i.e. sum of characters (as alphabet-positions) is triangular?
# ====================================================================================


# Oh there's a lot I don't get here:

def compute():
	ans = sum(1
		for s in WORDS
		if is_triangular_number(sum((ord(c) - ord('A') + 1) for c in s)))
	return str(ans)


def is_triangular_number(n):
	temp = 0
	for i in itertools.count():
		temp += i
		if n == temp:
			return True
		elif n < temp:
			return False
