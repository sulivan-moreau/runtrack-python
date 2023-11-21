N = int(input("Entrez un entier N supérieur à zéro : "))
if N <= 0:
    print("Veuillez entrer un entier supérieur à zéro.")
else:
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i} :")
        for j in range(1, 11):
            resultat = i * j
            print(f"{i} * {j} = {resultat}")
