def make_user(name, role='student'):
    return f"name={name}, role={role}"

p = input().split()
print(make_user(*p))