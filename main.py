import view.view_nilai as view
import view.input_nilai as inp
import model.daftar_nilai as dn
DaftarNilai = {}
while True:
    menu = input(
        "Pilih Menu : (L)ihat (T)ambah (U)bah (H)apus (C)ari (X)Exit : ").capitalize()
    if (menu == "L"):
        view.cetak_daftar_nilai(DaftarNilai)
    if (menu == "T"):
        inp.input_data(DaftarNilai, dn)
    if (menu == "U"):
        dn.Ubah_data(DaftarNilai)
    if (menu == "H"):
        dn.Hapus_data()
    if (menu == "C"):
        view.cetak_hasil_pencarian(DaftarNilai, dn)
    if (menu == "X"):
        break
