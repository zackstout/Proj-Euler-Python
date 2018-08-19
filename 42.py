# How many words are triangular, i.e. sum of characters (as alphabet-positions) is triangular?
# ====================================================================================


def compute():
	ans = sum(1 # Ahhh instead of i for i in .... we're just adding 1 each time:
		for s in WORDS
		# ord gives Unicode character.
		if is_triangular_number(sum((ord(c) - ord('A') + 1) for c in s)))
	return str(ans)


def is_triangular_number(n):
	temp = 0
	for i in itertools.count(): # I think this counts indefinitely
		temp += i
		# Check whether we've landed on our number, which would make it triangular:
		if n == temp:
			return True
		elif n < temp:
			return False
