def celsius_vers_fahrenheit(c):
    return float(c * 1.8 + 32)

def fahrenheit_vers_celsius(f):
    return float((f - 32) / 1.8)

def celsius_vers_kelvin(c):
    k = c + 273.15
    if k < 0:
        raise ValueError("Erreur : Kelvin négatif impossible")
    return float(k)

def kelvin_vers_celsius(k):
    if k < 0:
        raise ValueError("Erreur : Kelvin négatif impossible")
    return float(k - 273.15)
