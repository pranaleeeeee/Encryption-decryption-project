# cyber_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# ------------------ BACKEND (your functions) ------------------

def clean_path(path):
    """Remove quotes and extra spaces from user file paths."""
    return path.strip().replace('"', '').replace("'", "")


def encrypt(text, key, shift):
    encrypted = ""
    if not key:
        raise ValueError("Key must not be empty for Vigenère encryption.")
    key = key.lower()
    key_len = len(key)

    for i, ch in enumerate(text):
        if ch.isalpha():
            key_shift = ord(key[i % key_len]) - ord('a')
            base = ord('a') if ch.islower() else ord('A')
            new_char = chr((ord(ch) - base + key_shift + shift) % 26 + base)
            encrypted += new_char
        else:
            encrypted += ch
    return encrypted


def decrypt(ciphertext, key, shift):
    decrypted = ""
    if not key:
        raise ValueError("Key must not be empty for Vigenère decryption.")
    key = key.lower()
    key_len = len(key)

    for i, ch in enumerate(ciphertext):
        if ch.isalpha():
            key_shift = ord(key[i % key_len]) - ord('a')
            base = ord('a') if ch.islower() else ord('A')
            new_char = chr((ord(ch) - base - key_shift - shift) % 26 + base)
            decrypted += new_char
        else:
            decrypted += ch
    return decrypted


def encrypt_file(input_path, output_path, key, shift):
    try:
        input_path = clean_path(input_path)
        output_path = clean_path(output_path)

        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        encrypted_text = encrypt(text, key, shift)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(encrypted_text)

        return True, f"File encrypted and saved: {output_path}"
    except FileNotFoundError:
        return False, "Error: Input file not found."
    except Exception as e:
        return False, f"Unexpected error: {e}"


def decrypt_file(input_path, output_path, key, shift):
    try:
        input_path = clean_path(input_path)
        output_path = clean_path(output_path)

        with open(input_path, "r", encoding="utf-8") as f:
            ciphertext = f.read()

        decrypted_text = decrypt(ciphertext, key, shift)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(decrypted_text)

        return True, f"File decrypted and saved: {output_path}"
    except FileNotFoundError:
        return False, "Error: Input file not found."
    except Exception as e:
        return False, f"Unexpected error: {e}"


def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


def caesar_decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch
    return result


# ------------------ GUI ------------------

class CyberApp:
    def __init__(self, root):
        self.root = root
        root.title("Cyber Encryption App — Neon")
        root.geometry("900x640")
        root.config(bg="#0b0f0b")
        # fonts & colors
        self.bg = "#0b0f0b"
        self.panel = "#0f1a0f"
        self.text_bg = "#081208"
        self.neon = "#39ff14"   # neon green
        self.accent = "#2ee8a6"

        # top frame
        header = tk.Frame(root, bg=self.bg)
        header.pack(fill="x", pady=(8, 4))
        title = tk.Label(header, text="⟡ Cyber Encryption App", fg=self.neon,
                         bg=self.bg, font=("Consolas", 18, "bold"))
        title.pack(side="left", padx=12)

        subtitle = tk.Label(header, text="Vigenère+Shift  •  Caesar  •  File/ Text", fg=self.accent,
                            bg=self.bg, font=("Consolas", 10))
        subtitle.pack(side="left", padx=8)

        # center frame
        center = tk.Frame(root, bg=self.bg)
        center.pack(fill="both", expand=True, padx=12, pady=6)

        # Left: Controls
        controls = tk.Frame(center, bg=self.panel, padx=12, pady=12)
        controls.pack(side="left", fill="y", padx=(0,12))

        # Key & Shift entries
        tk.Label(controls, text="Key (Vigenère):", fg=self.neon, bg=self.panel, font=("Consolas", 10)).pack(anchor="w")
        self.key_entry = tk.Entry(controls, width=28, bg=self.text_bg, fg=self.neon, insertbackground=self.neon)
        self.key_entry.pack(pady=(2,8))

        tk.Label(controls, text="Shift (integer):", fg=self.neon, bg=self.panel, font=("Consolas", 10)).pack(anchor="w")
        self.shift_entry = tk.Entry(controls, width=10, bg=self.text_bg, fg=self.neon, insertbackground=self.neon)
        self.shift_entry.pack(pady=(2,8))

        # File chooser
        tk.Label(controls, text="File operations:", fg=self.neon, bg=self.panel, font=("Consolas", 11,"bold")).pack(anchor="w", pady=(6,4))
        self.file_path_var = tk.StringVar()
        self.file_entry = tk.Entry(controls, textvariable=self.file_path_var, width=36, bg=self.text_bg, fg=self.neon, insertbackground=self.neon)
        self.file_entry.pack(pady=(2,6))
        tk.Button(controls, text="Browse", width=12, bg=self.panel, fg=self.neon, relief="raised", command=self.browse_file).pack(pady=4)

        tk.Button(controls, text="Encrypt File", width=18, bg=self.neon, fg="#001", command=self.encrypt_file_action).pack(pady=(8,4))
        tk.Button(controls, text="Decrypt File", width=18, bg=self.neon, fg="#001", command=self.decrypt_file_action).pack(pady=4)

        # Separator
        tk.Label(controls, text="—", bg=self.panel).pack(pady=6)

        # Text operations
        tk.Label(controls, text="Text operations:", fg=self.neon, bg=self.panel, font=("Consolas", 11,"bold")).pack(anchor="w", pady=(6,4))
        tk.Button(controls, text="Encrypt Text (V+Shift)", width=20, bg=self.neon, fg="#001", command=self.encrypt_text_action).pack(pady=(6,4))
        tk.Button(controls, text="Decrypt Text (V+Shift)", width=20, bg=self.neon, fg="#001", command=self.decrypt_text_action).pack(pady=4)
        tk.Button(controls, text="Caesar Encrypt", width=20, bg=self.panel, fg=self.neon, command=self.caesar_encrypt_action).pack(pady=(8,4))
        tk.Button(controls, text="Caesar Decrypt", width=20, bg=self.panel, fg=self.neon, command=self.caesar_decrypt_action).pack(pady=4)
        tk.Button(controls, text="Clear Output", width=20, bg="#550000", fg="white", command=self.clear_output).pack(pady=(12,4))

        # Right: Text areas
        right = tk.Frame(center, bg=self.bg)
        right.pack(side="left", fill="both", expand=True)

        # Input label & area
        tk.Label(right, text="Input / Source Text", fg=self.accent, bg=self.bg, font=("Consolas", 11)).pack(anchor="w")
        self.input_area = scrolledtext.ScrolledText(right, wrap="word", height=12, bg=self.text_bg, fg=self.neon, insertbackground=self.neon, font=("Consolas",11))
        self.input_area.pack(fill="both", expand=False, pady=(4,8))

        # Output label & area
        tk.Label(right, text="Output / Result", fg=self.accent, bg=self.bg, font=("Consolas", 11)).pack(anchor="w")
        self.output_area = scrolledtext.ScrolledText(right, wrap="word", height=12, bg="#001100", fg=self.neon, font=("Consolas",11))
        self.output_area.pack(fill="both", expand=True, pady=(4,8))

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(root, textvariable=self.status_var, anchor="w", bg="#040604", fg=self.neon, font=("Consolas", 10))
        status_bar.pack(fill="x", side="bottom")

    # ------------------ GUI actions ------------------

    def browse_file(self):
        p = filedialog.askopenfilename()
        if p:
            self.file_path_var.set(p)
            self.status_var.set("File selected.")

    def _get_shift(self):
        s = self.shift_entry.get().strip()
        if s == "":
            return 0
        try:
            return int(s)
        except ValueError:
            raise ValueError("Shift must be an integer.")

    def _get_key(self):
        k = self.key_entry.get().strip()
        if k == "":
            raise ValueError("Key cannot be empty for Vigenère operations.")
        return k

    def encrypt_file_action(self):
        input_path = self.file_path_var.get().strip()
        if not input_path:
            messagebox.showwarning("No file", "Please choose an input file first.")
            return
        out = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not out:
            return
        try:
            key = self._get_key()
            shift = self._get_shift()
            ok, msg = encrypt_file(input_path, out, key, shift)
            if ok:
                self.status_var.set("File encrypted.")
                messagebox.showinfo("Success", msg)
            else:
                self.status_var.set("Error")
                messagebox.showerror("Error", msg)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error")

    def decrypt_file_action(self):
        input_path = self.file_path_var.get().strip()
        if not input_path:
            messagebox.showwarning("No file", "Please choose a file first.")
            return
        out = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not out:
            return
        try:
            key = self._get_key()
            shift = self._get_shift()
            ok, msg = decrypt_file(input_path, out, key, shift)
            if ok:
                self.status_var.set("File decrypted.")
                messagebox.showinfo("Success", msg)
            else:
                self.status_var.set("Error")
                messagebox.showerror("Error", msg)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error")

    def encrypt_text_action(self):
        text = self.input_area.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showwarning("Empty", "Input text is empty.")
            return
        try:
            key = self._get_key()
            shift = self._get_shift()
            out = encrypt(text, key, shift)
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, out)
            self.status_var.set("Text encrypted (Vigenère+Shift).")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error")

    def decrypt_text_action(self):
        text = self.input_area.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showwarning("Empty", "Input text is empty.")
            return
        try:
            key = self._get_key()
            shift = self._get_shift()
            out = decrypt(text, key, shift)
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, out)
            self.status_var.set("Text decrypted (Vigenère+Shift).")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error")

    def caesar_encrypt_action(self):
        text = self.input_area.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showwarning("Empty", "Input text is empty.")
            return
        try:
            shift = self._get_shift()
            out = caesar_encrypt(text, shift)
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, out)
            self.status_var.set("Text encrypted (Caesar).")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error")

    def caesar_decrypt_action(self):
        text = self.input_area.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showwarning("Empty", "Input text is empty.")
            return
        try:
            shift = self._get_shift()
            out = caesar_decrypt(text, shift)
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, out)
            self.status_var.set("Text decrypted (Caesar).")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_var.set("Error")

    def clear_output(self):
        self.output_area.delete("1.0", tk.END)
        self.status_var.set("Cleared output.")


# ------------------ RUN APP ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberApp(root)
    root.mainloop()
