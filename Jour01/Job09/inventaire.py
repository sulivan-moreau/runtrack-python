nom = "Tee-shirt"
prix_unitaire = 40
quantite_en_stock = 100

print(nom)
print(f"{prix_unitaire}€")
print(quantite_en_stock)

quant_aj = int(input("Entrez la qté à ajouter au stock : "))
quantite_en_stock += quant_aj
print(quantite_en_stock)

quant_achat = int(input("Entrez la qté que vous voulez acheter : "))
quantite_en_stock -= quant_achat

print(quantite_en_stock)

prix_unitaire *= 1.10

print(nom)
print(prix_unitaire)
print(quantite_en_stock)

