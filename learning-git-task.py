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
print ("To jest koniec programu.")  # Komunikat końcowy
print ("kłamałem") 
#powoli zaczynam to rozumieć 
