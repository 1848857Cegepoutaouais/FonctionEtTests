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
    #return pourcentage

liste_pourcentage = []
def pourcentage():
    for i in range(8):
        liste_pourcentage.append(str(input("ajouter un lego avec une couleur")))
    choix_couleur_1 = str(input("quelle couleur est que vous voulez trouvez son pourcentage avec?")).strip()
    montant_lego_choisi = (len(choix_couleur_1) -1)
    lego_total = len(liste_pourcentage)
    pourcentage_couleur = 100*montant_lego_choisi/lego_total
    return f"{pourcentage_couleur: .2f}%"




"""
3. Fonction qui reçoit une liste de legos et qui il y a combien de blocs de chaque couleur en moyenne
"""
# Pseudo

def moyenne(moyenne_rouge, moyenne_vert, moyenne_bleu):
    moyenne_rouge = ls_lego.count("rouge")/len(ls_lego)
    moyenne_vert = ls_lego.count("vert")/len(ls_lego)
    moyenne_bleu = ls_lego.count("bleu")/len(ls_lego)
    moyenne_rose = ls_lego.count("rose")/len(ls_lego)
    moyenne_cyan = ls_lego.count("cyan")/len(ls_lego)
    moyenne_orange = ls_lego.count("orange")/len(ls_lego)
    moyenne_rose = ls_lego.count("rose")/len(ls_lego)

ls_lego = ["bleu", "jaune", "rouge", "vert", "bleu", "jaune"]

moyenne(moyenne_rouge)

print("Moyenne blocs Lego rouges :", moyenne_rouge)
print("Moyenne blocs Lego verts :", moyenne_vert)
print("Moyenne blocs Lego bleus :", moyenne_bleu)
print("Moyenne blocs Lego roses :", moyenne_rose)
print("Moyenne blocs Lego cyans :", moyenne_cyan)
print("Moyenne blocs Lego oranges :", moyenne_orange)
print("Moyenne blocs Lego roses :", moyenne_rose)

"""

# Répartition des tâches :
                        a   b   c
Nom : Jonathan          1   2   3
Nom : Sam               2   3   1
Nom : William           3   1   2
"""