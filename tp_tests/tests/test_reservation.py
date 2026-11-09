import pytest
from app.reservation import Stock
from app.reservation import Reservation


@pytest.fixture
def objet_stock():
    return Stock(5)

def test_reservation_5_unite(objet_stock):

    reservation = Reservation(objet_stock)

    res=reservation.reserver(5)

    assert res == "confirmee"
    assert objet_stock.quantite==0

def test_reservation_2_unite(objet_stock):
    #arrange
    reservation = Reservation(objet_stock)
    #act
    result = reservation.reserver(2)

    assert result == "confirmee"
    assert objet_stock.quantite==3


def test_reservation_6_unite(objet_stock):

    reservation = Reservation(objet_stock)

    res=reservation.reserver(6)

    assert res == "refusee"
    assert objet_stock.quantite==5




def test_reservation_0_unite(objet_stock):
    reservation = Reservation(objet_stock)
    
    with pytest.raises(ValueError):
        reservation.reserver(0)

    assert objet_stock.quantite==5



