# date and time 

# import liblary 
import datetime  as dt

print(5*"=" + " Selamat Datang " + 5*"=")
print(" Silahkan masukkan tanggal \n bulan dan tahun lahir kamu \n")

Tanggal = int(input("Tanggal \t: "))
Bulan = int(input("Bulan \t\t: "))
Tahun = int(input("Tahun \t\t: "))
print('\n')
tanggal_lahir = dt.date(Tahun,Bulan,Tanggal)
print(f"Hari dan tanggal lahir kamu = {tanggal_lahir:%A} {tanggal_lahir} " )

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_sisa_bulan = (umur_hari.days % 365) // 30

print(F"Umur kamu sekarang adalah {umur_tahun} tahun {umur_sisa_bulan} bulan")

