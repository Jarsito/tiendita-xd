import tkinter as tk
from tkinter import messagebox

class ProductoMusical:
    def __init__(self, nombre, marcas_precios_stock):
        self.nombre = nombre
        self.marcas_precios_stock = marcas_precios_stock

    def mostrar_inventario(self):
        inventario = f"{self.nombre.capitalize()} - Productos Disponibles en LIMA MUSIC:\n"
        inventario += "{:<15} {:<15} {:<10} {:<10}\n".format("Marca", "Precio (USD)", "Stock", "Total")
        inventario += "=" * 50 + "\n"
        for marca, (precio, stock) in self.marcas_precios_stock.items():
            inventario += "{:<15} {:<15.2f} {:<10} {:<10.2f}\n".format(marca.capitalize(), precio, stock, precio * stock)
        return inventario

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
        tk.Label(self.root, text="Bienvenido a LIMA MUSIC", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion_window).pack(pady=10)
        tk.Button(self.root, text="Crear Nuevo Usuario", command=self.crear_usuario_window).pack(pady=10)
        tk.Button(self.root, text="Ver Inventario", command=self.inventario_window).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

    def iniciar_sesion_window(self):
        self.clear_frame()
        tk.Label(self.root, text="Iniciar Sesión", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self.root, text="Nombre de Usuario:").pack(pady=5)
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.pack(pady=5)
        tk.Label(self.root, text="Contraseña:").pack(pady=5)
        self.contrasena_entry = tk.Entry(self.root, show="*")
        self.contrasena_entry.pack(pady=5)
        tk.Button(self.root, text="Iniciar Sesión", command=self.verificar_sesion).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.main_window).pack(pady=10)

    def verificar_sesion(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        if self.usuarios.get(usuario) == contrasena:
            messagebox.showinfo("Éxito", f"Bienvenido, {usuario}!")
            self.inventario_window()
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos. Intente nuevamente.")

    def crear_usuario_window(self):
        self.clear_frame()
        tk.Label(self.root, text="Crear Nuevo Usuario", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self.root, text="Nuevo Nombre de Usuario:").pack(pady=5)
        self.nuevo_usuario_entry = tk.Entry(self.root)
        self.nuevo_usuario_entry.pack(pady=5)
        tk.Label(self.root, text="Nueva Contraseña:").pack(pady=5)
        self.nueva_contrasena_entry = tk.Entry(self.root, show="*")
        self.nueva_contrasena_entry.pack(pady=5)
        tk.Button(self.root, text="Crear Usuario", command=self.crear_usuario).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.main_window).pack(pady=10)

    def crear_usuario(self):
        nuevo_usuario = self.nuevo_usuario_entry.get()
        nueva_contrasena = self.nueva_contrasena_entry.get()
        if nuevo_usuario and nueva_contrasena:
            self.usuarios[nuevo_usuario] = nueva_contrasena
            messagebox.showinfo("Éxito", "Usuario creado exitosamente. Ahora puede iniciar sesión.")
            self.main_window()
        else:
            messagebox.showerror("Error", "Por favor complete ambos campos para crear un nuevo usuario.")

    def inventario_window(self):
        self.clear_frame()
        tk.Label(self.root, text="Inventario de LIMA MUSIC", font=("Helvetica", 16)).pack(pady=10)
        for producto in self.productos.values():
            tk.Label(self.root, text=producto.mostrar_inventario(), justify=tk.LEFT).pack(anchor='w')
        tk.Button(self.root, text="Seleccionar Producto", command=self.seleccionar_producto_window).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.main_window).pack(pady=10)

    def seleccionar_producto_window(self):
        self.clear_frame()
        tk.Label(self.root, text="Seleccionar Producto", font=("Helvetica", 16)).pack(pady=10)
        self.producto_entry = tk.Entry(self.root)
        self.producto_entry.pack(pady=5)
        tk.Button(self.root, text="Seleccionar", command=self.seleccionar_marca_window).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.inventario_window).pack(pady=10)

    def seleccionar_marca_window(self):
        producto_seleccionado = self.producto_entry.get().upper()
        producto = self.productos.get(producto_seleccionado)
        if producto:
            self.clear_frame()
            tk.Label(self.root, text=producto.mostrar_inventario(), justify=tk.LEFT).pack(anchor='w')
            tk.Label(self.root, text="Marcas Disponibles: " + ", ".join(producto.marcas_precios_stock.keys())).pack(pady=10)
            self.marca_entry = tk.Entry(self.root)
            self.marca_entry.pack(pady=5)
            tk.Label(self.root, text="Cantidad:").pack(pady=5)
            self.cantidad_entry = tk.Entry(self.root)
            self.cantidad_entry.pack(pady=5)
            tk.Button(self.root, text="Agregar al Carrito", command=lambda: self.agregar_al_carrito(producto)).pack(pady=10)
            tk.Button(self.root, text="Volver", command=self.inventario_window).pack(pady=10)
        else:
            messagebox.showerror("Error", "Producto no encontrado en LIMA MUSIC.")
            self.seleccionar_producto_window()

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
        self.inventario_window()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
