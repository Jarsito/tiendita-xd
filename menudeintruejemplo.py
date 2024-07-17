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
        
        self.show_instruments()

    def show_instruments(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        instruments_frame = tk.Frame(self.main_frame)
        instruments_frame.pack(fill=tk.BOTH, expand=True)
        
        instruments = [
            ("Electric Guitar", "High-quality electric guitar with advanced features.", 499, "/path/to/guitar.png"),
            ("Digital Piano", "Versatile digital piano with weighted keys.", 799, "/path/to/piano.png"),
            ("Drum Set", "Professional-grade drum set with premium hardware.", 999, "/path/to/drums.png"),
            ("Studio Headphones", "High-fidelity headphones for professional audio.", 149, "/path/to/headphones.png"),
            ("Condenser Microphone", "High-quality condenser microphone for recording.", 199, "/path/to/microphone.png"),
            ("Studio Monitors", "High-fidelity speakers for professional audio mixing.", 499, "/path/to/monitors.png"),
        ]
        
        for instrument in instruments:
            self.create_instrument_card(instruments_frame, instrument)

    def create_instrument_card(self, parent, instrument):
        name, description, price, image_path = instrument
        
        card = tk.Frame(parent, bg="#ffffff", relief=tk.RAISED, bd=2)
        card.pack(fill=tk.X, padx=10, pady=10)

        # Placeholder for image
        image_label = tk.Label(card, text="Image", width=20, height=10, bg="gray")
        image_label.pack(side=tk.TOP, fill=tk.X)
        
        # Product name
        name_label = tk.Label(card, text=name, font=("Helvetica", 16, "bold"), bg="#ffffff")
        name_label.pack(pady=5)

        # Product description
        desc_label = tk.Label(card, text=description, bg="#ffffff")
        desc_label.pack(pady=5)
        
        # Product price and View Brands button
        price_label = tk.Label(card, text=f"${price}", font=("Helvetica", 14, "bold"), fg="#1a202c", bg="#ffffff")
        price_label.pack(side=tk.LEFT, padx=10)
        
        view_brands_button = tk.Button(card, text="View Brands", font=("Helvetica", 12), bg="#1a202c", fg="#ffffff", command=self.view_brands)
        view_brands_button.pack(side=tk.RIGHT, padx=10)

    def show_guitars(self):
        messagebox.showinfo("Navigation", "Guitars section coming soon!")
    
    def show_pianos(self):
        messagebox.showinfo("Navigation", "Pianos section coming soon!")
    
    def show_drums(self):
        messagebox.showinfo("Navigation", "Drums section coming soon!")
    
    def show_accessories(self):
        messagebox.showinfo("Navigation", "Accessories section coming soon!")

    def view_brands(self):
        messagebox.showinfo("Information", "View Brands coming soon!")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
