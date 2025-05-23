import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import logic
import os

def generate(text_input, qr_label, save_button):
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Erreur de saisie", "Veuillez entrer un texte.")
        return

    try:
        logic.save_text(text)
        image_path = logic.generate_qr_code(text)
        img = Image.open(image_path)
        img = img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(img)
        qr_label.configure(image=tk_img)
        qr_label.image = tk_img
        save_button.config(state="normal")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def save_qr():
    dest = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
    if dest:
        try:
            os.replace("qr_code.png", dest)
            messagebox.showinfo("Succès", f"QR Code sauvegardé sous {dest}")
        except Exception as e:
            messagebox.showerror("Erreur de sauvegarde", str(e))

def main():
    root = tk.Tk()
    root.title("Générateur de QR Code")
    root.geometry("400x500")
    root.configure(bg="#121212")

    label = tk.Label(root, text="Générateur de QR Code", fg="white", bg="#121212", font=("Segoe UI", 16))
    label.pack(pady=10)

    text_input = tk.Text(root, height=5, width=40, bg="#2c2c2c", fg="white")
    text_input.pack(pady=10)

    qr_label = tk.Label(root, bg="#121212")
    qr_label.pack(pady=10)

    save_button = tk.Button(root, text="Sauvegarder le QR Code", bg="#3a86ff", fg="white", state="disabled", command=save_qr)
    save_button.pack(pady=10)

    generate_button = tk.Button(root, text="Générer QR Code", bg="#3a86ff", fg="white",
                                 command=lambda: generate(text_input, qr_label, save_button))
    generate_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()