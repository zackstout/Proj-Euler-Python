# Multiply up d(1), d(10), ..., d(100,000) for d(n) the nth digit of 0.12345678910111213...
# ====================================================================================

# Very elegant:

def compute():
	s = "".join(str(i) for i in range(1, 1000000))
	ans = 1
	for i in range(7):
		ans *= int(s[10**i - 1])
	return str(ans)


if __name__ == "__main__":
	print(compute())
	for i in range(7):
		print(i) # 0, 1, ..., 6
