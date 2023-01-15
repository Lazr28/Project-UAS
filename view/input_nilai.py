from model.daftar_nilai import *
from view.view_nilai import *
def input_data():
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    tugas = input("Masukan Nilai Tugas : ")
    uts = input("Masukan Nilai UTS : ")
    uas = input("Masukan Nilai UAS : ")

    tambah_data(nim, nama, tugas, uts, uas)
