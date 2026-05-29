def greet(name='Guest'):
    return f"Hello, {name}!"

name = input().strip()

if name:
    print(greet(name))
else:
    print(greet())