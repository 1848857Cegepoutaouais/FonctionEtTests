import pytest
import Fonction3Test as fonctions_a_tester

def test_division_entiere_1():
    # Arrange
    n = 6
    m = 2
    resultat_attendu = 3
    # Act
    resultat_division = fonctions_a_tester.division_entiere_1(n, m)

    # Assert
    assert resultat_division == resultat_attendu
