L = [0, 1, 2, 3, 4, 5]
l = len(L)
L[0], L[l-1] = L[l-1], L[0]
print(L)