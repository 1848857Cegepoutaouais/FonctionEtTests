# Pour chaque fonction une personne différente va :
# a. Programmer la fonction
# b. Créer le plan de tests
# c. Programmer les tests

"""
1. Fonction qui reçoit les points de vies et les points de défenses d'un joueur et les points d'attaques de l'autre et
qui retourne les points de vies restants après l'attaque.
"""

"""
2. Fonction qui reçoit une liste de legos et une couleur et qui le pourcentage de blocs de cette couleur
"""

#fonction pour le pourcentage
    #boucle de 7 fois
        #input de la couleur et ajoute à la liste
    #demande la couleur
    #nombre de lego avec la couleur dans la liste
    #nombre total de lego
    #return moyenne

liste_pourcentage = [""]
def pourcentage():
    for i in range(8):
        liste_pourcentage.append(str(input("ajouter un lego avec une couleur")))
    choix_couleur_1 = str(input("quelle couleur est que vous voulez trouvez son pourcentage avec?"))
    montant_lego_choisi = len(choix_couleur_1)
    lego_total = len(liste_pourcentage)
    pourcentage_couleur = 100*montant_lego_choisi/lego_total
    return f"{pourcentage_couleur}%"



"""
3. Fonction qui reçoit une liste de legos et qui il y a combien de blocs de chaque couleur en moyenne
"""
# Pseudo

def moyenne():


    return
ls_lego = ["bleu", "jaune", "rouge", "vert", "bleu", "jaune"]
len(ls_lego)

"""

# Répartition des tâches :
                        a   b   c
Nom : Jonathan          1   2   3
Nom : Sam               2   3   1
Nom : William           3   1   2
"""