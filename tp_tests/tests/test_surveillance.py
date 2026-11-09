from unittest.mock import patch
from app.surveillance import surveiller
import pytest

def test_surveillance_0_15():

    with patch("app.surveillance.envoyer_notification") as notifier:

        result = surveiller(0.15)

        assert result == "alerte"

        notifier.assert_called_once_with("Taux eleve")

def test_surveillance_0_05():

    with patch("app.surveillance.envoyer_notification") as notifier:

        result = surveiller(0.05)

        assert result == "ok"

        notifier.assert_not_called()

def test_surveillance_0_10():

    with patch("app.surveillance.envoyer_notification") as notifier:

        result = surveiller(0.10)

        assert result == "ok"

        notifier.assert_not_called()

def test_surveillance_error():
    with patch("app.surveillance.envoyer_notification") as notifier:

        notifier.side_effect = RuntimeError("Service non configure")

        with pytest.raises(RuntimeError):
            surveiller(0.15)