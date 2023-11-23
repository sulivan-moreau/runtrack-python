def tri(liste):
    if not liste:
        return liste

    pivot = liste[0]
    inferieurs = [x for x in liste[1:] if x <= pivot]
    superieurs = [x for x in liste[1:] if x > pivot]

    return tri(inferieurs) + [pivot] + tri(superieurs)

L = [3, 99, 43, 28, 9,75, 86, 31, 39, 60]

liste_triee= tri(L)

print(liste_triee)