N, lst = int(input()), list(map(int, input().split()))
print(all(i > 0 for i in lst) and any(i <10 or str(i) == (str(i))[::-1] for i in lst))