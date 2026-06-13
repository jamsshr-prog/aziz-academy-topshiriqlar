emails = input().split()
domains = set()
for email in emails:
    at_index = email.find('@')
    if at_index != -1:
        domain = email[at_index + 1:].lower()
        domains.add(domain)
if domains:
    result = sorted(domains)
    print(' '.join(result))
else:
    print("BO'SH")