# menginput angka menggunakan tipe data integer(int)
# menginput variabel angka denga kode "input"
angka=int(input("masukan angka :"))
#pengecekan kondisi apakah angka yang di input habis dibagi 2?
#jika iya maka kondisi ini yang dijalankan
if angka % 2 == 0 :
    print(angka,"adalah bilangan genap")
# dan jika tidak maka kondisi ini yang dijalankan 
else:
    print(angka,"adalah bilangan ganjil.")
