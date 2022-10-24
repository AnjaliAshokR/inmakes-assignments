products_prices = {
    "razor": 20,
    "pen": 5,
    "pencil": 2,
    "bag": 250,
    "book": 10
}
i = str(input("Enter the product name"))
print("The price of the product is", products_prices.get(i,"not in the list"))