# Lista zakupów z podziałem na sklepy
lista_zakupow = {
    "Warzywniak": ["Pomidor", "Ogórek", "Marchew", "Ziemniaki"],
    "Mięsny": ["Kurczak", "Wołowina", "Wieprzowina", "Kiełbasa"],
    "Rybny": ["Łosoś", "Dorsz", "Makrela", "Tuńczyk"]
}

# Wyświetlanie listy zakupów
for sklep, produkty in lista_zakupow.items():
    print(f"{sklep}: {', '.join(produkty)}")