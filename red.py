
def isreducible(a, b):
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            if a % j == 0 and b % j == 0:
                print('hi')
                return (a, b, j, True)
    return (a, b, False)

ans = isreducible(5, 6)
ans2 = isreducible(2, 4)
ans3 = isreducible(4, 2)
ans4 = isreducible(3, 12)
print(ans, ans2, ans3, ans4)
