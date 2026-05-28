t = (1, 2, 3,)
try:
    t[0] = 99
except TypeError:
    print("Error")