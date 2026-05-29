def choose(a, b, mode):
    return max(a, b) if mode == 'max' else min(a, b) if mode == 'min' else a 

a, b = map(int, input().split())
mode = input()

print(choose(a, b, mode))
print(choose(mode=mode, a=a, b=b))