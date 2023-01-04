

def tambah_data(df, nim, nama, tugas, uts, uas):
    print("Menambahkan Data..")
    akhir = ((int(tugas) / 100*30) + (int(uts)/100*35) + (int(uas) / 100*35))
    df[nim] = {"nama": nama, "tugas": tugas,
               "uts": uts, "uas": uas, "akhir": akhir}
    print("Data Berhasil tersimpan")


def Ubah_data(df):
    found = 0
    nama = input("Cari Data Mahasiswa yang ingin di ubah : ")
    for i, j in df.items():
        if ((df.get(i)).get('nama') == nama):
            found = i
    if (found == 0):
        print("Data tidak ada")
    else:
        nama = input("Masukan Nama         : ")
        if nama == "":
            nama = df[found]['nama']
        tugas = input("Masukan Nilai Tugas  : ")
        if tugas == "":
            tugas = df[found]['tugas']
        uts = input("Masukan Nilai UTS    : ")
        if uts == "":
            uts = df[found]['uts']
        uas = input("Masukan Nilai UAS    : ")
        if uas == "":
            uas = df[found]['uas']
        akhir = ((int(tugas) / 100*30) +
                 (int(uts)/100*35) + (int(uas) / 100*35))
        df[found] = {"nama": nama, "tugas": tugas,
                          "uts": uts, "uas": uas, "akhir": akhir}
        print("Berhasil Mengubah Data")


def Hapus_data():
    print("Hapus Data..")


def Cari_data(df, nama):
    x, found = 0, 0
    for i, j in df.items():
        x += 1
        if ((df.get(i)).get('nama').startswith(nama)):
            found += 1
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:6.2f} |'.format(
                1, i, df[i]["nama"], df[i]["tugas"], df[i]["uts"], df[i]["uas"], df[i]["akhir"]))
    if (found == 0):
        print("Data tidak ada")
