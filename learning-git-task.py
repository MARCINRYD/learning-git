# Słownik z listą zakupów
shopping_list = {
    "warzywniak": ["pomidor", "ogórek", "marchew", "ziemniaki"],
    "mięsny": ["kurczak", "wołowina", "wieprzowina", "kiełbasa"],
    "rybny": ["łosoś", "dorsz", "makrela", "tuńczyk"]
}

# Iteracja po słowniku i wyświetlanie wiadomości
total_products = 0
for shop, products in shopping_list.items():
    shop_capitalized = shop.capitalize()  # Wielka litera w nazwie sklepu
    products_capitalized = ", ".join([product.capitalize() for product in products])  # Wielka litera w nazwie produktów
    print(f"Idę do {shop_capitalized} i kupuję tam {products_capitalized}.")
    total_products += len(products)

# Wyświetlenie sumy produktów
print(f"W sumie kupuję {total_products} produktów.")
print("Pozdrawiam! Zaczynają się już konkretne zagadnienia. Mam pytanie dotyczące sposobu pisania komend—widzę, że wiele rzeczy w kursie jest pisanych w wierszu poleceń, a niektóre w Git Bash. Co wybrać? Na czym się skupić?")