import json
from src.functions.fileManager import openJson, saveData

def addProduct(name, qnt, price):
    prod = openJson('./src/templates/product.json')
    prod['name'] = name
    prod['quantity'] = qnt
    prod['price'] = price
    return prod

data = openJson('data.json')
newProd = addProduct('Sol', 20, 4.99)
data['Produtos'].append(newProd)
saveData('data.json', data)