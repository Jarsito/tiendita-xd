import tkinter as tk
from tkinter import ttk, messagebox

class ProductoMusical:
    def __init__(self, nombre, marcas_precios_stock):
        self.nombre = nombre
        self.marcas_precios_stock = marcas_precios_stock

    def obtener_inventario(self):
        return [
            (marca, precio, stock, precio * stock)
            for marca, (precio, stock) in self.marcas_precios_stock.items()
        ]

class CarritoItem:
    def __init__(self, producto, marca, cantidad):
        self.producto = producto
        self.marca = marca
        self.cantidad = cantidad

    def calcular_precio_total(self):
        return self.producto.marcas_precios_stock[self.marca][0] * self.cantidad

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("LIMA MUSIC")
        self.root.geometry("1000x700")
        self.root.configure(bg='#6366F1')
        self.usuarios = {"usuario1": "contrasena1", "usuario2": "contrasena2"}
        self.carrito = []
        self.productos = {
            'GUITARRA': ProductoMusical('GUITARRA', {'fender': (1200, 10), 'gibson': (1500, 10), 'ibanez': (1000, 10)}),
            'TECLADO': ProductoMusical('TECLADO', {'roland': (1000, 10), 'yamaha': (1200, 10), 'korg': (900, 10)}),
            'BATERIA': ProductoMusical('BATERIA', {'pearl': (1800, 10), 'sabian': (1600, 10), 'stagg': (1400, 10)}),
            'MICROFONO': ProductoMusical('MICROFONO', {'shure': (150, 10), 'akg': (120, 10), 'sennheiser': (180, 10)}),
            'AMPLIFICADOR': ProductoMusical('AMPLIFICADOR', {'marshall': (700, 10), 'orange': (750, 10), 'fender': (650, 10)}),
            'PIANO': ProductoMusical('PIANO', {'steinway': (3000, 10), 'kawai': (2800, 10), 'casio': (2500, 10)}),
            'VIOLIN': ProductoMusical('VIOLIN', {'stentor': (400, 10), 'yamaha': (380, 10), 'ibanez': (350, 10)}),
            'FLAUTA': ProductoMusical('FLAUTA', {'yamaha': (200, 10), 'pearl': (180, 10), 'gemeinhardt': (220, 10)}),
        }
        self.main_window()

    def main_window(self):
        self.clear_frame()
        
        # Header
        header = tk.Frame(self.root, bg="#1a202c", height=50)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="LIMA MUSIC", font=("Helvetica", 20, "bold"), fg="#ffffff", bg="#1a202c")
        title.pack(side=tk.LEFT, padx=20)
        
        nav = tk.Frame(header, bg="#1a202c")
        nav.pack(side=tk.RIGHT, padx=20)

        nav_buttons = [("Iniciar Sesión", self.iniciar_sesion_window),
                       ("Crear Nuevo Usuario", self.crear_usuario_window)]
        
        for text, command in nav_buttons:
            btn = tk.Button(nav, text=text, font=("Helvetica", 12), fg="#ffffff", bg="#1a202c", relief=tk.FLAT, command=command)
            btn.pack(side=tk.LEFT, padx=10)
        
        # Main content area
        self.main_frame = tk.Frame(self.root, bg='#6366F1')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        for producto_nombre in self.productos:
            tk.Button(self.main_frame, text=producto_nombre, command=lambda p=producto_nombre: self.producto_window(p)).pack(pady=5)

    def iniciar_sesion_window(self):
        self.clear_frame()
        
        # Container for form
        container = tk.Frame(self.root, bg='#6366F1')
        container.pack(expand=True)

        # Placeholder for logo
        logo = tk.Label(container, text="Logo", bg='#6366F1', fg='white', font=("Helvetica", 16, "bold"))
        logo.pack(pady=10)

        # Heading
        heading = tk.Label(container, text="Iniciar Sesión", bg='#6366F1', fg='white', font=("Helvetica", 20, "bold"))
        heading.pack(pady=10)

        # Subheading
        subheading = tk.Label(container, text="O empiece su prueba gratuita de 14 días", bg='#6366F1', fg='white', font=("Helvetica", 10))
        subheading.pack(pady=5)

        # Username entry
        self.usuario_entry = tk.Entry(container, width=30, font=("Helvetica", 12))
        self.usuario_entry.insert(0, 'Usuario')
        self.usuario_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, 'Usuario'))
        self.usuario_entry.pack(pady=5)

        # Password entry
        self.contrasena_entry = tk.Entry(container, show='*', width=30, font=("Helvetica", 12))
        self.contrasena_entry.insert(0, 'Contraseña')
        self.contrasena_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, 'Contraseña'))
        self.contrasena_entry.pack(pady=5)

        # Remember me checkbox
        self.remember_var = tk.BooleanVar()
        remember_me = tk.Checkbutton(container, text="Recuérdame", variable=self.remember_var, bg='#6366F1', fg='white', font=("Helvetica", 10))
        remember_me.pack(pady=5)

        # Forgot password link
        forgot_password = tk.Label(container, text="¿Olvidó su contraseña?", bg='#6366F1', fg='white', font=("Helvetica", 10), cursor="hand2")
        forgot_password.pack(pady=5)

        # Sign in button
        sign_in_button = tk.Button(container, text="Iniciar Sesión", command=self.verificar_sesion, width=30, bg='#6366F1', fg='white', font=("Helvetica", 12, "bold"))
        sign_in_button.pack(pady=10)

        # Create account and Continue as guest links
        create_account = tk.Label(container, text="Crear una cuenta", bg='#6366F1', fg='white', font=("Helvetica", 10), cursor="hand2")
        create_account.pack(side=tk.LEFT, padx=20)

        continue_as_guest = tk.Label(container, text="Continuar como invitado", bg='#6366F1', fg='white', font=("Helvetica", 10), cursor="hand2")
        continue_as_guest.pack(side=tk.RIGHT, padx=20)

    def verificar_sesion(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        if self.usuarios.get(usuario) == contrasena:
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario}!")
            self.main_window()
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos. Intente nuevamente.")

    def crear_usuario_window(self):
        self.clear_frame()
        
        # Container for form
        container = tk.Frame(self.root, bg='#6366F1')
        container.pack(expand=True)

        # Placeholder for logo
        logo = tk.Label(container, text="Logo", bg='#6366F1', fg='white', font=("Helvetica", 16, "bold"))
        logo.pack(pady=10)

        # Heading
        heading = tk.Label(container, text="Crear Nuevo Usuario", bg='#6366F1', fg='white', font=("Helvetica", 20, "bold"))
        heading.pack(pady=10)

        # Username entry
        self.nuevo_usuario_entry = tk.Entry(container, width=30, font=("Helvetica", 12))
        self.nuevo_usuario_entry.insert(0, 'Nuevo Usuario')
        self.nuevo_usuario_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, 'Nuevo Usuario'))
        self.nuevo_usuario_entry.pack(pady=5)

        # Password entry
        self.nueva_contrasena_entry = tk.Entry(container, show='*', width=30, font=("Helvetica", 12))
        self.nueva_contrasena_entry.insert(0, 'Nueva Contraseña')
        self.nueva_contrasena_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, 'Nueva Contraseña'))
        self.nueva_contrasena_entry.pack(pady=5)

        # Create account button
        create_account_button = tk.Button(container, text="Crear Usuario", command=self.crear_usuario, width=30, bg='#6366F1', fg='white', font=("Helvetica", 12, "bold"))
        create_account_button.pack(pady=10)

        # Back button
        back_button = tk.Button(container, text="Volver", command=self.main_window, width=30, bg='#6366F1', fg='white', font=("Helvetica", 12, "bold"))
        back_button.pack(pady=10)

    def crear_usuario(self):
        nuevo_usuario = self.nuevo_usuario_entry.get()
        nueva_contrasena = self.nueva_contrasena_entry.get()
        if nuevo_usuario and nueva_contrasena:
            self.usuarios[nuevo_usuario] = nueva_contrasena
            messagebox.showinfo("Éxito", "Usuario creado exitosamente. Ahora puede iniciar sesión.")
            self.main_window()
        else:
            messagebox.showerror("Error", "Por favor complete ambos campos para crear un nuevo usuario.")

    def producto_window(self, producto_nombre):
        self.clear_frame()
        producto = self.productos[producto_nombre]
        tk.Label(self.root, text=f"{producto.nombre} - Inventario", font=("Helvetica", 16), bg='#6366F1', fg='white').pack(pady=10)
        tree = ttk.Treeview(self.root, columns=("Marca", "Precio", "Stock", "Total"), show="headings")
        tree.heading("Marca", text="Marca")
        tree.heading("Precio", text="Precio (USD)")
        tree.heading("Stock", text="Stock")
        tree.heading("Total", text="Total (USD)")
        for item in producto.obtener_inventario():
            tree.insert("", tk.END, values=item)
        tree.pack(pady=10)

        tk.Label(self.root, text="Marca:", bg='#6366F1', fg='white').pack(pady=5)
        self.marca_entry = tk.Entry(self.root)
        self.marca_entry.pack(pady=5)
        tk.Label(self.root, text="Cantidad:", bg='#6366F1', fg='white').pack(pady=5)
        self.cantidad_entry = tk.Entry(self.root)
        self.cantidad_entry.pack(pady=5)
        tk.Button(self.root, text="Agregar al Carrito", command=lambda: self.agregar_al_carrito(producto), bg='#6366F1', fg='white', font=("Helvetica", 12, "bold")).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.main_window, bg='#6366F1', fg='white', font=("Helvetica", 12, "bold")).pack(pady=10)

    def agregar_al_carrito(self, producto):
        marca_seleccionada = self.marca_entry.get().lower()
        cantidad = int(self.cantidad_entry.get())
        if marca_seleccionada in producto.marcas_precios_stock:
            precio, stock = producto.marcas_precios_stock[marca_seleccionada]
            if 0 < cantidad <= stock:
                self.carrito.append(CarritoItem(producto, marca_seleccionada, cantidad))
                producto.marcas_precios_stock[marca_seleccionada] = (precio, stock - cantidad)
                messagebox.showinfo("Éxito", f"Se han agregado {cantidad} {marca_seleccionada} {producto.nombre}(s) al carrito.")
            else:
                messagebox.showerror("Error", "Cantidad no válida o no hay suficiente stock.")
        else:
            messagebox.showerror("Error", f"Marca no válida para {producto.nombre.capitalize()}.")
        self.main_window()

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
