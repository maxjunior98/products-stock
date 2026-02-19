import tkinter as tk
import json
from src.functions.fileManager import openJson, saveData
from datetime import date
from src.functions.interface import ProductContainer
from src.interfaces.app import App

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
    

def getDate():
    today = date.today()
    today = today.strftime('%d-%m-%Y')
    print(today)
    return today

# data = openJson('data.json')
# data = updateProd('Sol', 9, 4.99, data)
# newProd = addProduct('Sol', 20, 4.99)
# data['Produtos'].append(newProd)
# saveData('data.json', data)


def on_click():
    name = entry.get()
    label_result.config(text=f"Hello, {name}!")

# root = tk.Tk()
# root.title("Estoque Manager")
# root.geometry("300x200")

# label = tk.Label(root, text="Gerenciamento de Estoque")
# label.pack(pady=10)

# entry = tk.Entry(root)
# entry.pack(pady=5)

# button = tk.Button(root, text="Submit", command=on_click)
# button.pack(pady=10)

# label_result = tk.Label(root, text="")
# label_result.pack(pady=10)

# frame = ProductContainer(root, 'Name', 'Price', 'Qnt')

# root.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()