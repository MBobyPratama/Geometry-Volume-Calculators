# 'pip install tk' (jika tkinter belum terinstall)
from tkinter import *
from tkinter import ttk
import tkinter as tk

PHI = 3.14159265358979323846

def capsule(PHI, r, a):
  return PHI * r * r * ((4/3) * r + a)

def kerucut(PHI, r, h):
  return (1/3) * PHI * r * r * h

def tabung(PHI, r, h):
  return PHI * r * r * h

def kerucutTerpancung(PHI, r1, r2, h):
  return (1/3) * PHI * h * (r1 * r1 + r2 * r2 + (r1 * r2))

def balok(a, b, c):
  return a * b * c

def setengahBola(PHI, r):
  return (2/3) * PHI * r * r * r

def limasSegiEmpat(a, h):
  return (1/3) * a * a * h

def limasSegiTiga(a, b, h):
  return (1/6) * a * b * h

def bola(PHI, r):
  return (4/3) * PHI * r * r * r

def torus(PHI, r, R):
  return 2 * PHI * r * R * R

# Fungsi untuk menghitung volume geometri berdasarkan bentuk yang dipilih
def calculate():
  global satuan_combo, r_entry, a_entry, h_entry, r1_entry, r2_entry, b_entry, R_entry
  shape_name = selected_geometry.get()
  select = shape_mapping.get(shape_name, 0)
  satuan = satuan_combo.get()

  if satuan not in ["mm", "cm", "m", "km"]:
    result_label.config(text="Satuan tidak valid. Silakan coba lagi.")
    return

  if select == 11:
    result_label.config(text="Terima kasih telah menggunakan kalkulator volume geometri ^ᵕ^!")
    return

  if select == 1:
    r = float(r_entry.get())
    a = float(a_entry.get())
    result_label.config(text="Volume Capsule adalah " + str(capsule(PHI, r, a)) + " " + satuan + "³")

  elif select == 2:
    r = float(r_entry.get())
    h = float(h_entry.get())
    result_label.config(text="Volume Kerucut adalah " + str(kerucut(PHI, r, h)) + " " + satuan + "³")

  elif select == 3:
    r = float(r_entry.get())
    h = float(h_entry.get())
    result_label.config(text="Volume Tabung adalah " + str(tabung(PHI, r, h)) + " " + satuan + "³")

  elif select == 4:
    r1 = float(r1_entry.get())
    r2 = float(r2_entry.get())
    h = float(h_entry.get())
    result_label.config(text="Volume Kerucut Terpancung adalah " + str(kerucutTerpancung(PHI, r1, r2, h)) + " " + satuan + "³")

  elif select == 5:
    a = float(r_entry.get())
    b = float(h_entry.get())
    c = float(h_entry.get())
    result_label.config(text="Volume Balok adalah " + str(balok(a, b, c)) + " " + satuan + "³")

  elif select == 6:
    r = float(r_entry.get())
    result_label.config(text="Volume setengahBola adalah " + str(setengahBola(PHI, r)) + " " + satuan + "³")

  elif select == 7:
    a = float(a_entry.get())
    h = float(h_entry.get())
    result_label.config(text="Volume Limas Segiempat adalah " + str(limasSegiEmpat(a, h)) + " " + satuan + "³")

  elif select == 8:
    a = float(a_entry.get())
    b = float(b_entry.get())
    h = float(h_entry.get())
    result_label.config(text="Volume Limas Segitiga adalah " + str(limasSegiTiga(a, b, h)) + " " + satuan + "³")

  elif select == 9:
    r = float(r_entry.get())
    result_label.config(text="Volume Bola adalah " + str(bola(PHI, r)) + " " + satuan + "³")

  elif select == 10:
    r = float(r_entry.get())
    R = float(R_entry.get())
    result_label.config(text="Volume Torus adalah " + str(torus(PHI, r, R)) + " " + satuan + "³")

  else:
    result_label.config(text="Input tidak valid. Silakan coba lagi.")

# Fungsi untuk mengupdate field input berdasarkan bentuk geometri yang dipilih
def update_fields(event):
  global satuan_combo, r_entry, a_entry, h_entry, r1_entry, r2_entry, b_entry, R_entry

  for widget in input_frame.winfo_children():
    widget.destroy()

  selected = selected_geometry.get()

  satuan_label = tk.Label(input_frame, text="Masukkan satuan:")
  satuan_label.pack()
  satuan_combo = ttk.Combobox(input_frame, values=["mm", "cm", "m", "km"], state="readonly")
  satuan_combo.pack(pady=(0, 10))

  if selected == "Capsule":
    r_label = tk.Label(input_frame, text="Masukkan jari-jari r:")
    r_label.pack()
    r_entry = tk.Entry(input_frame)
    r_entry.pack()

    a_label = tk.Label(input_frame, text="Masukkan tinggi a:")
    a_label.pack()
    a_entry = tk.Entry(input_frame)
    a_entry.pack()

  elif selected == "Kerucut":
    r_label = tk.Label(input_frame, text="Masukkan jari-jari r:")
    r_label.pack()
    r_entry = tk.Entry(input_frame)
    r_entry.pack()

    h_label = tk.Label(input_frame, text="Masukkan tinggi h:")
    h_label.pack()
    h_entry = tk.Entry(input_frame)
    h_entry.pack()

  elif selected == "Tabung":
    r_label = tk.Label(input_frame, text="Masukkan jari-jari r:")
    r_label.pack()
    r_entry = tk.Entry(input_frame)
    r_entry.pack()

    h_label = tk.Label(input_frame, text="Masukkan tinggi h:")
    h_label.pack()
    h_entry = tk.Entry(input_frame)
    h_entry.pack()

  elif selected == "Kerucut Terpancung":
    r1_label = tk.Label(input_frame, text="Masukkan jari-jari r1:")
    r1_label.pack()
    r1_entry = tk.Entry(input_frame)
    r1_entry.pack()

    r2_label = tk.Label(input_frame, text="Masukkan jari-jari r2:")
    r2_label.pack()
    r2_entry = tk.Entry(input_frame)
    r2_entry.pack()

    h_label = tk.Label(input_frame, text="Masukkan tinggi h:")
    h_label.pack()
    h_entry = tk.Entry(input_frame)
    h_entry.pack()

  elif selected == "Balok":
    r_label = tk.Label(input_frame, text="Masukkan panjang a:")
    r_label.pack()
    r_entry = tk.Entry(input_frame)
    r_entry.pack()

    h_label = tk.Label(input_frame, text="Masukkan lebar b:")
    h_label.pack()
    h_entry = tk.Entry(input_frame)
    h_entry.pack()

    h_label = tk.Label(input_frame, text="Masukkan tinggi c:")
    h_label.pack()
    h_entry = tk.Entry(input_frame)
    h_entry.pack()

  elif selected == "Setengah Bola":
    r_label = tk.Label(input_frame, text="Masukkan jari-jari r:")
    r_label.pack()
    r_entry = tk.Entry(input_frame)
    r_entry.pack()

  elif selected == "Limas Segiempat":
    a_label = tk.Label(input_frame, text="Masukkan panjang sisi a:")
    a_label.pack()
    a_entry = tk.Entry(input_frame)
    a_entry.pack()

    h_label = tk.Label(input_frame, text="Masukkan tinggi h:")
    h_label.pack()
    h_entry = tk.Entry(input_frame)
    h_entry.pack()

  elif selected == "Limas Segitiga":
    a_label = tk.Label(input_frame, text="Masukkan panjang sisi a:")
    a_label.pack()
    a_entry = tk.Entry(input_frame)
    a_entry.pack()

    b_label = tk.Label(input_frame, text="Masukkan panjang sisi b:")
    b_label.pack()
    b_entry = tk.Entry(input_frame)
    b_entry.pack()

    h_label = tk.Label(input_frame, text="Masukkan tinggi h:")
    h_label.pack()
    h_entry = tk.Entry(input_frame)
    h_entry.pack()

  elif selected == "Bola":
    r_label = tk.Label(input_frame, text="Masukkan jari-jari r:")
    r_label.pack()
    r_entry = tk.Entry(input_frame)
    r_entry.pack()

  elif selected == "Torus":
    r_label = tk.Label(input_frame, text="Masukkan jari-jari r:")
    r_label.pack()
    r_entry = tk.Entry(input_frame)
    r_entry.pack()

    R_label = tk.Label(input_frame, text="Masukkan jari-jari besar R:")
    R_label.pack()
    R_entry = tk.Entry(input_frame)
    R_entry.pack()

# Main Window
root = tk.Tk()
root.title("Kalkulator Volume Geometri")
root.geometry("360x450")

title_label = tk.Label(root, text="Menghitung Volume Geometri", font=("Helvetica", 14), relief="solid")
title_label.pack(pady=30)

shape_mapping = {
  "Capsule": 1,
  "Kerucut": 2,
  "Tabung": 3,
  "Kerucut Terpancung": 4,
  "Balok": 5,
  "Setengah Bola": 6,
  "Limas Segiempat": 7,
  "Limas Segitiga": 8,
  "Bola": 9,
  "Torus": 10
}

geometry = ["Balok", "Bola", "Capsule", "Kerucut", "Kerucut Terpancung", "Limas Segiempat", "Limas Segitiga", "Setengah Bola", "Tabung", "Torus"]
selected_geometry = tk.StringVar(value="Balok")

title_label = tk.Label(root, text="Pilih bentuk yang ingin anda hitung volumenya:")
title_label.pack()

select_geometry = ttk.Combobox(root, width=20, textvariable=selected_geometry, values=geometry, state="readonly")
select_geometry.pack()
select_geometry.bind("<<ComboboxSelected>>", update_fields)

input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

result_btn = tk.Button(root, text="Hitung", command=calculate)
result_btn.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

github_label = tk.Label(root, text="GitHub: @MBobyPratama", fg="purple", font=("Helvetica", 8))
github_label.place(x=65, y=440, anchor="center")

update_fields(None)

root.mainloop()

# Konsep awal
# print("Selamat datang di kalkulator volume geometri ^ᵕ^!")

# while True:
#   select = int(input("\nPilih bentuk yang ingin Anda hitung volumenya: \
#                       \n1. Capsule \
#                       \n2. Kerucut \
#                       \n3. Tabung \
#                       \n4. Kerucut Terpancung \
#                       \n5. balok \
#                       \n6. setengahBola \
#                       \n7. Limas Segiempat \
#                       \n8. Limas Segitiga \
#                       \n9. Bola \
#                       \n10. Torus \
#                       \n11. Keluar \
#                       \nInput: "))

#   if select == 11:
#     print("\nTerima kasih telah menggunakan kalkulator volume geometri ^ᵕ^!\n")
#     break

#   satuan = input("Masukkan satuan yang akan digunakan (mm/cm/m/km): ")
#   if satuan != "mm" and "cm" and "m" and "km" :
#     print("Satuan tidak valid. Silakan coba lagi.")
#     continue

#   if select == 1:
#     r = float(input("Masukkan jari-jari r: "))
#     a = float(input("Masukkan tinggi a: "))
#     print("\nVolume Capsule adalah", capsule(PHI, r, a), satuan + "³")
#   elif select == 2:
#     r = float(input("Masukkan jari-jari r: "))
#     h = float(input("Masukkan tinggi h: "))
#     print("\nVolume Kerucut adalah", kerucut(PHI, r, h), satuan + "³")
#   elif select == 3:
#     r = float(input("Masukkan jari-jari r: "))
#     h = float(input("Masukkan tinggi h: "))
#     print("\nVolume Tabung adalah", tabung(PHI, r, h), satuan + "³")
#   elif select == 4:
#     r1 = float(input("Masukkan jari-jari r1: "))
#     r2 = float(input("Masukkan jari-jari r2: "))
#     h = float(input("Masukkan tinggi h: "))
#     print("\nVolume Kerucut Terpancung adalah", kerucutTerpancung(PHI, r1, r2, h), satuan + "³")
#   elif select == 5:
#     r = float(input("Masukkan jari-jari r: "))
#     h = float(input("Masukkan tinggi h: "))
#     print("\nVolume balok adalah", balok(PHI, r, h), satuan + "³")
#   elif select == 6:
#     r = float(input("Masukkan jari-jari r: "))
#     print("\nVolume setengahBola adalah", setengahBola(PHI, r), satuan + "³")
#   elif select == 7:
#     a = float(input("Masukkan panjang sisi a: "))
#     h = float(input("Masukkan tinggi h: "))
#     print("\nVolume Limas Segiempat adalah", limasSegiEmpat(a, h), satuan + "³")
#   elif select == 8:
#     a = float(input("Masukkan panjang sisi a: "))
#     b = float(input("Masukkan panjang sisi b: "))
#     h = float(input("Masukkan tinggi h: "))
#     print("\nVolume Limas Segitiga adalah", limasSegiTiga(a, b, h), satuan + "³")
#   elif select == 9:
#     r = float(input("Masukkan jari-jari r: "))
#     print("\nVolume Bola adalah", Bola(PHI, r), satuan + "³")
#   elif select == 10:
#     r = float(input("Masukkan jari-jari r: "))
#     R = float(input("Masukkan jari-jari besar R: "))
#     print("\nVolume Torus adalah", torus(PHI, r, R), satuan + "³")
#   else:
#     print("Input tidak valid. Silakan coba lagi.")