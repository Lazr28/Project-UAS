from model.daftar_nilai import *
def Jdl_Tbl():
    print("=========================================================================")
    print("| No |     NIM     |       NAMA        |  TUGAS  |  UTS | UAS |  AKHIR  |")
    print("=========================================================================")

def foot_Tbl():
    print("=========================================================================")


def cetak_daftar_nilai():
    print("Mencetak daftar nilai...")
    Jdl_Tbl()
    if (len(df) == 0):
        print("Belum ada data / Kosong")
    else:
        x = 1
        for i, j in df.items():
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:7.2f} |'.format(
                x, i, df[i]["nama"], df[i]["tugas"], df[i]["uts"], df[i]["uas"], df[i]["akhir"]))
            x += 1
        foot_Tbl()


def cetak_hasil_pencarian():
    print("mencetak hasil cari nilai...")
    nama = input("Cari Data nilai berdasarkan Nama : ")
    Jdl_Tbl()
    Cari_data( nama)
    foot_Tbl()
