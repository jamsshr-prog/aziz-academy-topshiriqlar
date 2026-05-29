def apply_op(op, *args):
    if op == 'sum':
        return sum(args)
    elif op == 'prod':
        natija = 1
        for son in args:
            natija *= son 
        return natija
    
op = input()
sonlar = (list(map(int, input().split())))

print(apply_op(op, * sonlar))