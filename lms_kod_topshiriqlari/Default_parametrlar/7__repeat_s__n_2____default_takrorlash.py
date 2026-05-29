def repeat(s, n=2):
    return s * n 

s = input()
n = input()

print(repeat(s) if n == '' else repeat(s, int(n)))