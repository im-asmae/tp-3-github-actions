import pytest
from app.texte import nettoyer_texte

def test_nettoyer_texte_clean():

    assert nettoyer_texte("déjà propre") == "déjà propre"


def test_nettoyer_texte_not_clean():
    entree="  BONJOUR   monde  "
    attendu="bonjour monde"
    assert nettoyer_texte(entree) == attendu


@pytest.mark.parametrize("entree, attendu", [
    (" HELLO       ", "hello"),
    (" bonjour asmae       ", "bonjour asmae"),

])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu

def test_nettoyer_texte_invalide():

    with pytest.raises(TypeError):
        assert nettoyer_texte(123)


