import pytest
import fctListes as moyenne

@pytest.mark.parametrize("j1, j2, resultat_attendu", [
    ("roche", "ciseau", "joueur 1 gagne avec roche."),
    ("roche", "papier", "joueur 2 gagne avec papier."),
    ("Roche", "Papier", "joueur 2 gagne avec Papier.")
])
def test_moyenne(moyenne_rouge, moyenne_vert, moyenne_bleu):
    # Arrange
    resultat_attendu = 3
    # Act
    resultat_division = moyenne(moyenne_rouge, moyenne_vert, moyenne_bleu)

    # Assert
    assert resultat_division == resultat_attendu
