import pytest
from src.convertisseur import (
    celsius_vers_fahrenheit, 
    kelvin_vers_celsius, 
    celsius_vers_kelvin
)

def test_0c_vers_32f():
    assert celsius_vers_fahrenheit(0) == 32.0

def test_100c_vers_212f():
    assert celsius_vers_fahrenheit(100) == 212.0

def test_273_15k_vers_0c():
    assert kelvin_vers_celsius(273.15) == 0.0

def test_celsius_vers_0k():
    assert celsius_vers_kelvin(-273.15) == pytest.approx(0.0)

def test_kelvin_negatif_exception():
    with pytest.raises(ValueError):
        kelvin_vers_celsius(-10)

def test_valeur_decimale_36_6c():
    assert celsius_vers_fahrenheit(36.6) == pytest.approx(97.88)
