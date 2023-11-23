def my_long_word(longueur_min, phrase):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if len(mot) > longueur_min]
    resultat = " ".join(mots_filtres)
    return resultat


chiffre_entier = 3
phrase_exemple = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(chiffre_entier, phrase_exemple)

print("Output:", resultat)
