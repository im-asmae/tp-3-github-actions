from unittest.mock import Mock
from app.moderation import decider
import pytest


def test_moderation_bloquer():

    modele = Mock()
    modele.predict.return_value = "spam"

    #arrange
    message = "Offre miracle"

    #act
    result = decider(modele, message)

    #assert
    assert result == "bloquer"

    modele.predict.assert_called_once_with("Offre miracle")

def test_moderation_autoriser():
    modele = Mock()
    modele.predict.return_value = "normal"
    #arrange
    message = "rapport tp"
    #act
    result = decider(modele, message)
    #assert
    assert result == "autoriser"

    modele.predict.assert_called_once_with("rapport tp")



def test_moderation_model_indisponible():
    modele=Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError):
        decider(modele, "action compte bancaire")
