import tkinter as tk
from tkinter import messagebox

# Product class to store product information
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# Inventory class to manage the products in the store
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, quantity, price)
        self.show_message(f"Added {quantity} of {name} to the inventory.")
    
    def sell_product(self, name, quantity_sold):
        if name in self.products and self.products[name].quantity >= quantity_sold:
            self.products[name].quantity -= quantity_sold
            self.show_message(f"Sold {quantity_sold} of {name}. Remaining stock: {self.products[name].quantity}")
            self.check_stock(name)
        else:
            self.show_message(f"Not enough stock of {name} to complete the sale.")
    
    def check_stock(self, name):
        if self.products[name].quantity < 5:
            self.show_message(f"Warning: Low stock for {name}. Only {self.products[name].quantity} left!")
    
    def display_inventory(self):
        inventory_str = "\nCurrent Inventory:\n"
        for name, product in self.products.items():
            inventory_str += f"{name}: {product.quantity} units, Price: R{product.price:.2f}\n"
        return inventory_str

    def show_message(self, message):
        messagebox.showinfo("Inventory Management", message)

# GUI Application class
class InventoryApp:
    def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Inventory Management")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.root, text="Product Name:")
        self.label_name.grid(row=0, column=0)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)

        self.label_quantity = tk.Label(self.root, text="Quantity:")
        self.label_quantity.grid(row=1, column=0)
        self.entry_quantity = tk.Entry(self.root)
        self.entry_quantity.grid(row=1, column=1)

        self.label_price = tk.Label(self.root, text="Price:")
        self.label_price.grid(row=2, column=0)
        self.entry_price = tk.Entry(self.root)
        self.entry_price.grid(row=2, column=1)

        self.button_add = tk.Button(self.root, text="Add Product", command=self.add_product)
        self.button_add.grid(row=3, column=0, columnspan=2)

        self.button_sell = tk.Button(self.root, text="Sell Product", command=self.sell_product)
        self.button_sell.grid(row=4, column=0, columnspan=2)

        self.button_display = tk.Button(self.root, text="Display Inventory", command=self.display_inventory)
        self.button_display.grid(row=5, column=0, columnspan=2)

    def add_product(self):
        name = self.entry_name.get()
        quantity = int(self.entry_quantity.get())
        price = float(self.entry_price.get())
        self.inventory.add_product(name, quantity, price)

    def sell_product(self):
        name = self.entry_name.get()
        quantity_sold = int(self.entry_quantity.get())
        self.inventory.sell_product(name, quantity_sold)

    def display_inventory(self):
        inventory_str = self.inventory.display_inventory()
        self.inventory.show_message(inventory_str)

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
