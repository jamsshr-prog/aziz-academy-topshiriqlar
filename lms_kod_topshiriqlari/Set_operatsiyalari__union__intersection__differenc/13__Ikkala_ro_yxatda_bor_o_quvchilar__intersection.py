A = set(input().strip().split())
B = set(input().strip().split())
common = A.intersection(B)
sorted_common = sorted(common)
print(len(sorted_common))
for name in sorted_common:
    print(name)