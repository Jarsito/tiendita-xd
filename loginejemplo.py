import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Store")
        self.root.geometry("400x500")
        self.root.configure(bg='#6366F1')
        
        self.create_widgets()

    def create_widgets(self):
        # Container for form
        container = tk.Frame(self.root, bg='#6366F1')
        container.pack(expand=True)

        # Placeholder for logo
        logo = tk.Label(container, text="Logo", bg='#6366F1', fg='white', font=("Helvetica", 16, "bold"))
        logo.pack(pady=10)

        # Heading
        heading = tk.Label(container, text="Sign in to your account", bg='#6366F1', fg='white', font=("Helvetica", 20, "bold"))
        heading.pack(pady=10)

        # Subheading
        subheading = tk.Label(container, text="Or start your 14-day free trial", bg='#6366F1', fg='white', font=("Helvetica", 10))
        subheading.pack(pady=5)

        # Username entry
        self.username_entry = tk.Entry(container, width=30, font=("Helvetica", 12))
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, 'Username'))
        self.username_entry.pack(pady=5)

        # Password entry
        self.password_entry = tk.Entry(container, show='*', width=30, font=("Helvetica", 12))
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, 'Password'))
        self.password_entry.pack(pady=5)

        # Remember me checkbox
        self.remember_var = tk.BooleanVar()
        remember_me = tk.Checkbutton(container, text="Remember me", variable=self.remember_var, bg='#6366F1', fg='white', font=("Helvetica", 10))
        remember_me.pack(pady=5)

        # Forgot password link
        forgot_password = tk.Label(container, text="Forgot your password?", bg='#6366F1', fg='white', font=("Helvetica", 10), cursor="hand2")
        forgot_password.pack(pady=5)

        # Sign in button
        sign_in_button = tk.Button(container, text="Sign in", command=self.sign_in, width=30, bg='#6366F1', fg='white', font=("Helvetica", 12, "bold"))
        sign_in_button.pack(pady=10)

        # Create account and Continue as guest links
        create_account = tk.Label(container, text="Create an account", bg='#6366F1', fg='white', font=("Helvetica", 10), cursor="hand2")
        create_account.pack(side=tk.LEFT, padx=20)

        continue_as_guest = tk.Label(container, text="Continue as guest", bg='#6366F1', fg='white', font=("Helvetica", 10), cursor="hand2")
        continue_as_guest.pack(side=tk.RIGHT, padx=20)

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        remember_me = self.remember_var.get()
        
        # Placeholder logic for sign in
        if username and password:
            messagebox.showinfo("Success", f"Signed in as {username}")
        else:
            messagebox.showerror("Error", "Please enter both username and password")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
