a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Ces longueurs forment un triangle équilatéral.")
    elif a == b or a == c or b == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Ces longueurs forment un triangle rectangle et isocèle.")
        else:
            print("Ces longueurs forment un triangle isocèle.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Ces longueurs forment un triangle rectangle.")
    else:
        print("Ces longueurs forment un triangle quelconque.")
else:
    print("Ces longueurs ne peuvent pas former un triangle.")
