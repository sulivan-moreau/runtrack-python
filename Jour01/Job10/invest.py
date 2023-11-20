# Demander à l'utilisateur d'entrer les valeurs initiales
montant_initial = float(input("Entrez le montant initial de l'investissement en euros : "))
taux_rendement_annuel = float(input("Entrez le taux de rendement annuel en pourcentage : "))

# Gain annuel initial
gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel initial : {gain_annuel} euros")

# Augmentation du capital et taux de rendement de 2%
montant_initial += 5000
taux_rendement_annuel += 2

# Gain annuel après augmentation
gain_annuel_apres_augmentation = (taux_rendement_annuel / 100) * montant_initial
print(f"Gain annuel après augmentation du capital et du taux de rendement : {gain_annuel_apres_augmentation} euros")

# Retrait de 10% du portefeuille et diminution du rendement de 1%
retrait = 0.10 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1
montant_final = montant_initial + (taux_rendement_annuel / 100) * montant_initial
nouveau_gain = (taux_rendement_annuel / 100) * montant_final
print(f"Nouveau gain après retrait et diminution du rendement : {nouveau_gain} euros")
