products_list = []
products_dict = {}
i = 1

while input('Enter "y" to enter a product or enter "n" to stop typing: ') != 'n':
    products_dict = {
        "Product's name": input("Enter product's name: "),
        "Cost": input("Enter the product's cost: "),
        "Quantity": input("Enter the product's quantity: "),
        "Unit of measure": input("Enter the product's unit of measure: ")
    }
    products_tuple = (i, products_dict)
    products_list.append(products_tuple)
    i += 1

analitics_dict = {}
for num, el in products_list:
    for key, value in el.items():
        if not analitics_dict.get(key):
            analitics_dict[key] = [value]
        else:
            analitics_dict[key].append(value)

for key, value in analitics_dict.items():
    analitics_dict[key] = list(set(value))

print(analitics_dict)
