a, b, c, d = map(int, input().split())
natija = (a + b * 2) - (c // 2) + (d % 3)
if natija == 9:
	print(f"Result: {natija - 1}")
else:
    print(f"Result: {natija + 1}")