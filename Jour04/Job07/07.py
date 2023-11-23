L = [8, 24, 48, 2, 16]
print(L)
print(f"Le nombre de multiple de 3 dans la liste est de : {sum(1 for nombre in L if nombre % 3 == 0)}")