n = int(input())
lst = list(map(int, input().split()))
copy_lst = lst[:]
copy_lst.reverse()
print(lst)
print(copy_lst)