# Find next number which is triangonal, pentagonal and hexagonal.
# ====================================================================================

def compute():
	i = 286
	j = 166
	k = 144
	# Loops forever (until we meet our break/return condition):
	while True:
		triangle = i * (i + 1) // 2
		pentagon = j * (j * 3 - 1) // 2
		hexagon  = k * (k * 2 - 1)
		minimum = min(triangle, pentagon, hexagon)
		# Nice way of checking if all elements are the same:
		if minimum == max(triangle, pentagon, hexagon):
			return str(triangle)
		# Ensures we step through the set one by one, in a sense:
		if minimum == triangle: i += 1
		if minimum == pentagon: j += 1
		if minimum == hexagon : k += 1


if __name__ == "__main__":
	print(compute())
