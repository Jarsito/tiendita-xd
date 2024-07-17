import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Carrito de compras")
        self.root.geometry("600x400")
        
        self.cart = [
            {
                "id": 1,
                "name": "Camiseta de algodón",
                "quantity": 2,
                "price": 19.99,
            },
            {
                "id": 2,
                "name": "Pantalones vaqueros",
                "quantity": 1,
                "price": 49.99,
            },
            {
                "id": 3,
                "name": "Zapatos deportivos",
                "quantity": 1,
                "price": 59.99,
            },
        ]
        
        self.create_widgets()

    def create_widgets(self):
        # Card frame
        card_frame = ttk.Frame(self.root, padding="10 10 10 10")
        card_frame.pack(fill=tk.BOTH, expand=True)

        # Card Header
        card_header = ttk.Label(card_frame, text="Carrito de compras", font=("Helvetica", 16, "bold"))
        card_header.pack(pady=10)

        # Card Content (Table)
        columns = ("Producto", "Cantidad", "Precio unitario", "Precio total")
        self.tree = ttk.Treeview(card_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, minwidth=0, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        self.update_table()

        # Card Footer
        card_footer = ttk.Frame(card_frame)
        card_footer.pack(fill=tk.X, pady=10)

        total_label = ttk.Label(card_footer, text=f"Total: ${self.calculate_total():.2f}", font=("Helvetica", 12, "bold"))
        total_label.pack(side=tk.LEFT, padx=10)
        
        button_frame = ttk.Frame(card_footer)
        button_frame.pack(side=tk.RIGHT)

        continue_button = ttk.Button(button_frame, text="Continuar comprando", command=self.continue_shopping)
        continue_button.pack(side=tk.LEFT, padx=5)
        
        checkout_button = ttk.Button(button_frame, text="Proceder al pago", command=self.checkout)
        checkout_button.pack(side=tk.LEFT, padx=5)

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for item in self.cart:
            total_price = item["quantity"] * item["price"]
            self.tree.insert("", "end", values=(item["name"], item["quantity"], f"${item['price']:.2f}", f"${total_price:.2f}"))

    def calculate_total(self):
        return sum(item["quantity"] * item["price"] for item in self.cart)

    def continue_shopping(self):
        messagebox.showinfo("Información", "Continúe comprando!")

    def checkout(self):
        messagebox.showinfo("Información", "Procediendo al pago!")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
