import tkinter as tk

# Warna tema
BG_COLOR = "#1E1E1E"
TEXT_COLOR = "#F5F5F5"
BTN_COLOR = "#333"
BTN_HOVER = "#555"
BTN_EQUAL = "#FF9500"
BTN_CLEAR = "#D9534F"

# Fungsi untuk menampilkan angka/operator ke layar
def tombol_ditekan(value):
    layar.insert(tk.END, value)

# Fungsi untuk menghitung hasil
def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, tk.END)
        layar.insert(tk.END, hasil)
    except:
        layar.delete(0, tk.END)
        layar.insert(tk.END, "Error")

# Fungsi untuk menghapus layar
def hapus():
    layar.delete(0, tk.END)

# Fungsi efek hover pada tombol
def on_enter(e):
    e.widget.config(bg=BTN_HOVER)

def on_leave(e):
    e.widget.config(bg=BTN_COLOR)

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Modern")
root.geometry("300x400")
root.configure(bg=BG_COLOR)

# Entry untuk layar kalkulator
layar = tk.Entry(root, font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR, border=0, justify="right")
layar.pack(fill="both", padx=10, pady=10, ipady=10)

# Daftar tombol
tombol = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Frame untuk tombol
frame_tombol = tk.Frame(root, bg=BG_COLOR)
frame_tombol.pack()

# Loop untuk membuat tombol
for baris in tombol:
    row = tk.Frame(frame_tombol, bg=BG_COLOR)
    row.pack(expand=True, fill="both")
    
    for t in baris:
        warna = BTN_COLOR
        if t == "=":
            warna = BTN_EQUAL
        elif t == "C":
            warna = BTN_CLEAR
        
        btn = tk.Button(row, text=t, font=("Arial", 18), bg=warna, fg=TEXT_COLOR, relief="flat",
                        width=5, height=2, command=lambda t=t: hitung() if t == "=" else hapus() if t == "C" else tombol_ditekan(t))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        
        # Efek hover
        if t not in ["=", "C"]:
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

# Menjalankan aplikasi
root.mainloop()
