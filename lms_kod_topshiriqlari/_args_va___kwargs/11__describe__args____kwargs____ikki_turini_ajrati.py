def describe(*args, **kwargs):
    return {
        'args_count': len(args),
        'args_sum': sum(args),
        'kwargs_count': len(kwargs),
        'kwargs_sum': sum(kwargs.values())
        
    }
    
args = list(map(int, input().split()))

n = int(input())

kwargs = {}

for _ in range(n):
    key, value = input().split()
    kwargs[key] = int(value)
    
print(describe(*args, **kwargs))