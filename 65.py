# Something about sums of digits of numerators of convergents toward e.
#  **  Useful in its own right for thinking about e more.  **  
# ====================================================================================


# There's something compressed here that I will understand if I think on it:

def compute():
	numer = 1
	denom = 0
	for i in reversed(range(100)):
		numer, denom = e_contfrac_term(i) * numer + denom, numer
	ans = sum(int(c) for c in str(numer))
	return str(ans)


def e_contfrac_term(i):
	if i == 0:
		return 2
	elif i % 3 == 2:
		return i // 3 * 2 + 2
	else:
		return 1


if __name__ == "__main__":
	print(compute())
