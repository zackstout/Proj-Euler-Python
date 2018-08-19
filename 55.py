# How many numbers below 10,000 are Lychrel, i.e. do not collapse into palindromes by adding them with their reverses after 50 iterations?
# ====================================================================================


# This is nice for thinking about palindromes:
def compute():
	ans = sum(1 for i in range(10000) if is_lychrel(i))
	return str(ans)


def is_lychrel(n):
	for i in range(50):
        # Reverse the number and add it to the number:
		n += int(str(n)[ : : -1])
        # Check whether it's a palindrome:
		if str(n) == str(n)[ : : -1]:
			return False
	return True


if __name__ == "__main__":
	print(compute())
