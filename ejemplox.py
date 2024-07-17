import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Store")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Frame(self.root, bg="#1a202c", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="Music Store", font=("Helvetica", 20, "bold"), fg="#ffffff", bg="#1a202c")
        title.pack(side=tk.LEFT, padx=20)
        
        nav = tk.Frame(header, bg="#1a202c")
        nav.pack(side=tk.RIGHT, padx=20)

        nav_buttons = [("Guitars", self.show_guitars),
                       ("Pianos", self.show_pianos),
                       ("Drums", self.show_drums),
                       ("Accessories", self.show_accessories)]
        
        for text, command in nav_buttons:
            btn = tk.Button(nav, text=text, font=("Helvetica", 12), fg="#ffffff", bg="#1a202c", relief=tk.FLAT, command=command)
            btn.pack(side=tk.LEFT, padx=10)

        # Main content area
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.show_products()

    def show_products(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        products = [
            ("Electric Guitar", "$499", "High-quality electric guitar with advanced features.", "/path/to/guitar.png"),
            ("Digital Piano", "$799", "Versatile digital piano with weighted keys.", "/path/to/piano.png"),
            ("Drum Set", "$999", "Professional-grade drum set with premium hardware.", "/path/to/drums.png"),
            ("Studio Headphones", "$149", "High-fidelity headphones for professional audio.", "/path/to/headphones.png"),
            ("Condenser Microphone", "$199", "High-quality condenser microphone for recording.", "/path/to/microphone.png"),
            ("Studio Monitors", "$499", "High-fidelity speakers for professional audio mixing.", "/path/to/monitors.png"),
        ]
        
        for product in products:
            self.create_product_card(product)

    def create_product_card(self, product):
        name, price, description, image_path = product
        
        card = ttk.Frame(self.main_frame)
        card.pack(fill=tk.X, pady=10)
        
        # Placeholder for image
        image_label = tk.Label(card, text="Image", width=20, height=10, bg="gray")
        image_label.grid(row=0, column=0, rowspan=2)
        
        # Product name
        name_label = ttk.Label(card, text=name, font=("Helvetica", 16, "bold"))
        name_label.grid(row=0, column=1, sticky=tk.W)
        
        # Product description
        desc_label = ttk.Label(card, text=description)
        desc_label.grid(row=1, column=1, sticky=tk.W)
        
        # Product price
        price_label = ttk.Label(card, text=price, font=("Helvetica", 14, "bold"), foreground="#1a202c")
        price_label.grid(row=2, column=0, sticky=tk.W, padx=10)
        
        # Add to cart button
        add_to_cart_btn = ttk.Button(card, text="Add to Cart")
        add_to_cart_btn.grid(row=2, column=1, sticky=tk.E)

    def show_guitars(self):
        messagebox.showinfo("Navigation", "Guitars section coming soon!")
    
    def show_pianos(self):
        messagebox.showinfo("Navigation", "Pianos section coming soon!")
    
    def show_drums(self):
        messagebox.showinfo("Navigation", "Drums section coming soon!")
    
    def show_accessories(self):
        messagebox.showinfo("Navigation", "Accessories section coming soon!")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
