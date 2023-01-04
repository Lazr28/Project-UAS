def input_data(df, dn):
    nim = input("Masukan NIM : ")
    nama = input("Masukan Nama : ")
    tugas = input("Masukan Nilai Tugas : ")
    uts = input("Masukan Nilai UTS : ")
    uas = input("Masukan Nilai UAS : ")

    dn.tambah_data(df, nim, nama, tugas, uts, uas)
