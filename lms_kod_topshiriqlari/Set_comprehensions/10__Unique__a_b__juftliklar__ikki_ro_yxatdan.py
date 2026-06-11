A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
pairs = {(a, b) for a in A for b in B}
print(len(pairs))
for a, b in sorted(pairs):
    print(f"{a},{b}")