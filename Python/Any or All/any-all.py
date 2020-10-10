N, lst = int(input()), list(map(int, input().split()))
print(all(i > 0 for i in lst) and any(i < 10 or i % 11 == 0 for i in lst))