# Tworzenie słownika z listą zakupów
lista_zakupow = {
    "warzywniak": ["pomidor", "ogórek", "marchew", "ziemniaki"],
    "mięsny": ["kurczak", "wołowina", "wieprzowina", "kiełbasa"],
    "rybny": ["łosoś", "dorsz", "makrela", "tuńczyk"]
}

# Iteracja po słowniku i wypisywanie formatowanego tekstu
for sklep, produkty in lista_zakupow.items():
    sklep_wielka_litera = sklep.capitalize()  # Pierwsza litera wielka
    produkty_wielka_litera = ", ".join([produkt.capitalize() for produkt in produkty])  # Każdy produkt z wielką literą
    print(f"Idę do {sklep_wielka_litera} i kupuję tam {produkty_wielka_litera}.")