def addProduct(name, qnt, price):
    prod = openJson('./src/templates/product.json')
    prod['name'] = name
    prod['quantity'] = qnt
    prod['price'] = price
    return prod

def updateProd(name, qnt, price, data):
    index = next((index for (index, d) in enumerate(data['Produtos']) if d['name'] == name), None)
    newProd = addProduct(name, qnt, price)
    data['Produtos'][index] = newProd
    return data
