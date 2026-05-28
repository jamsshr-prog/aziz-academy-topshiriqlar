s = input()
unlin = "aeiou"
hisob = 0
for harf in s:
    if harf in unlin:
        hisob += 1
print(hisob)