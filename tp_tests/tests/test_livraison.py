from app.livraison import frais_livraison
import pytest

def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


def test_livraison_panier_299():
    # Arrange
    montant = 299
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25

def test_livraison_panier_300():
    # Arrange
    montant = 300
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 0

def test_livraison_panier_301():
    # Arrange
    montant = 301
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 0

def test_livraison_panier_0():
    # Arrange
    montant = 0
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25

def test_livraison_panier_negatif():
    # Arrange
    montant = -12

    with pytest.raises(ValueError):
        frais_livraison(montant)