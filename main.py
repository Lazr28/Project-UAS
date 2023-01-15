from view.input_nilai import *
from model.daftar_nilai import *
from view.view_nilai import *
print("|-------------------------------------------------------------------|")
print("|--------------------PROGRAM NILAI MAHASISWA------------------------|")
print("|-------------------------------------------------------------------|")
while True:
    menu = input(
        "Pilih Menu : (L)ihat (T)ambah (U)bah (H)apus (C)ari (X)Exit : ").capitalize()
    if (menu == "L"):
        cetak_daftar_nilai()
    if (menu == "T"):
        input_data()
    if (menu == "U"):
        Ubah_data()
    if (menu == "H"):
        Hapus_data()
    if (menu == "C"):
        cetak_hasil_pencarian()
    if (menu == "X"):
        break
