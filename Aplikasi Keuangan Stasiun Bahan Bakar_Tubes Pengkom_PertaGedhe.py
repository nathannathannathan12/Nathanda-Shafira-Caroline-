# Kelompok 4 
# Anggota :
# Nabila Fathurrohman (16423002)
# Nathanda Shafira Caroline (16423212)
# Athalia Arsyahera (16423272)
# Amanda Natasya (16423282)
# Aisha Raudhatul Jannah (16423292)

# Tanggal/Hari : jum'at/20 Oktober 2023
# Deskripsi : Menentukan keuntungan yang diperoleh dari penjualan bahan bakar dalam sehari

# KAMUS :
# solar, pertalite, pertamax, pertamax_turbo, dexlite (harga bahan bakar per liter dengan jenis tertentu) : integer
# biaya_operasional (terdiri dari biaya listrik, gaji karyawan, dll) : integer
# jenis (jenis bahan bakar yang diinginkan): string
# sum_solar, sum_pertalite, sum_pertamax, sum_pertamax_turbo, sum_dexlite (jumlah awal liter tiap bahan bakar) : integer
# transaksi : integer
# total_solar, total_pertalite, total_pertamax, total_pertamax_turbo, total_dexlite (total liter yang dihabiskan dalam satu hari): integer
# total_penjualan : integer
# total_keuntungan : integer
# C : string
# tanggal : string

# ALGORITMA
# Input

# Hari dan tanggal pembelian bahan bakar
tanggal = input("Masukkan tanggal transaksi : ")

# Harga bahan bakar per liter dengan jenis tertentu
solar = 8000
pertalite = 10000
pertamax = 14000
pertamax_turbo = 16000
dexlite = 18000

# Biaya operasional terdiri dari biaya listrik, gaji karyawan, dll
biaya_operasional = int(input("Masukkan biaya operasional : "))

# Jumlah awal bahan bakar (liter)
sum_solar = 0
sum_pertalite = 0
sum_pertamax = 0
sum_pertamax_turbo = 0
sum_dexlite = 0

# Untuk menyimpan data 
transaksi = [ ]

# Jumlah pembeli dalam satu hari 
N = int(input("Masukkan jumlah pembeli : "))

# Proses
for i in range (N): 
    print(f"Riwayat Pembelian Pembeli ke-{i+1}: ")
    jenis = str(input("Masukkan jenis bahan bakar yang dibeli : "))
    while jenis != "tidak ada" :
        if jenis == "solar" :
            total_solar = int(input("Masukkan jumlah liter solar yang dibeli : "))
            while total_solar > 0 :
                sum_solar += total_solar
                transaksi.append(("solar", total_solar))
                total_solar = int(input("Masukkan jumlah liter solar yang dibeli : "))
            C = str(input(f"Apakah ada lagi bahan bakar yang dibeli pembeli ke-{i+1}? "))
            if C == "ada" : 
                jenis = str(input("Masukkan jenis bahan bakar yang dibeli : "))
            else :
                break
                
        elif jenis == "pertalite" :
            total_pertalite = int(input("Masukkan jumlah liter pertalite yang dibeli : "))
            while total_pertalite > 0 :
                sum_pertalite += total_pertalite
                transaksi.append(("pertalite", total_pertalite))
                total_pertalite = int(input("Masukkan jumlah liter pertalite yang dibeli : "))
            C = str(input(f"Apakah ada lagi bahan bakar yang dibeli pembeli ke-{i+1}? "))
            if C == "ada" : 
                jenis = str(input("Masukkan jenis bahan bakar yang dibeli : "))
            else :
                break

        elif jenis == "pertamax" :
            total_pertamax = int(input("Masukkan jumlah liter pertamax yang dibeli : "))
            while total_pertamax > 0 :
                sum_pertamax += total_pertamax
                transaksi.append(("pertamax", total_pertamax))
                total_pertamax = int(input("Masukkan jumlah liter pertamax yang dibeli : "))
            C = str(input(f"Apakah ada lagi bahan bakar yang dibeli pembeli ke-{i+1}? "))
            if C == "ada" : 
                jenis = str(input("Masukkan jenis bahan bakar yang dibeli : "))
            else :
                break

        elif jenis == "pertamax turbo" :
            total_pertamax_turbo = int(input("Masukkan jumlah liter pertamax turbo yang dibeli : "))
            while total_pertamax_turbo > 0 :
                sum_pertamax_turbo += total_pertamax_turbo
                transaksi.append(("pertamax turbo", total_pertamax_turbo))
                total_pertamax_turbo = int(input("Masukkan jumlah liter pertamax turbo yang dibeli : "))
            C = str(input(f"Apakah ada lagi bahan bakar yang dibeli pembeli ke-{i+1}? "))
            if C == "ada" : 
                jenis = str(input("Masukkan jenis bahan bakar yang dibeli : "))
            else :
                break

        elif jenis == "dexlite" :
            total_dexlite = int(input("Masukkan jumlah liter dexlite yang dibeli : "))
            while total_dexlite > 0 :
                sum_dexlite += total_dexlite
                transaksi.append(("dexlite", total_dexlite))
                total_dexlite = int(input("Masukkan jumlah liter dexlite yang dibeli : "))
            C = str(input(f"Apakah ada lagi bahan bakar yang dibeli pembeli ke-{i+1}? "))
            if C == "ada" : 
                jenis = str(input("Masukkan jenis bahan bakar yang dibeli : "))
            else :
                break
        
        else :
            print ("Maaf, sepertinya kamu kurang fokus dalam input datanya, cek lagi ya dan minum aqua :D, terima kasih!")
            break
        
# Menghitung total penjualan     
total_penjualan = sum_solar*solar + sum_pertalite*pertalite + sum_pertamax*pertamax + sum_pertamax_turbo*pertamax_turbo + sum_dexlite*dexlite

# Menghitung keuntungan yag diperoleh
total_keuntungan = total_penjualan - biaya_operasional

# Menghitung jumlah liter yang dihabiskan dalam satu hari
jumlah_liter_solar = sum(jumlah for jenis, jumlah in transaksi if jenis == "solar")
jumlah_liter_pertalite = sum(jumlah for jenis, jumlah in transaksi if jenis == "pertalite") 
jumlah_liter_pertamax = sum(jumlah for jenis, jumlah in transaksi if jenis == "pertamax") 
jumlah_liter_pertamax_turbo = sum(jumlah for jenis, jumlah in transaksi if jenis == "pertamax turbo")
jumlah_liter_dexlite = sum(jumlah for jenis, jumlah in transaksi if jenis == "dexlite")

# Mencetak total liter yang terjual dan keuntungan yang didapatkan dalam satu hari
print (f"Jumlah solar yang terjual {jumlah_liter_solar} liter")
print (f"Jumlah pertalite yang terjual {jumlah_liter_pertalite} liter") 
print (f"Jumlah pertamax yang terjual {jumlah_liter_pertamax} liter")
print (f"Jumlah pertamax turbo yang terjual {jumlah_liter_pertamax_turbo} liter")
print (f"Jumlah dexlite yang terjual {jumlah_liter_dexlite} liter")
print (f"Total keuntungan yang diperoleh adalah Rp{total_keuntungan}")