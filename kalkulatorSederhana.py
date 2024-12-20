def calculator():
    while True:
        print("==================================")
        print("|           Calculator           |")
        print("==================================")
        print("| 1. Penjumlahan                 |")
        print("| 2. Pengurangan                 |")
        print("| 3. Perkalian                   |")
        print("| 4. Pembagian                   |")
        print("| 5. Sisa Bagi                   |")
        print("| 6. Pangkat                     |")
        print("| 7. Akar Kuadrat                |")
        print("| 8. Keluar                      |")
        print("==================================")
        
        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 8:
                print("\nthank you (^o^)")
                break

        if pilihan == 7:
                angka1 = int(input("Masukkan angka: "))
                hasil = angka1 ** 0.5
                print(f"{angka1} = {hasil}")
                continue

        if pilihan in [1, 2, 3, 4, 5, 6]:
                angka1 = int(input("Masukkan angka: "))
                angka2 = int(input("Masukkan angka: "))
        if pilihan == 1:
                hasil = angka1 + angka2
                operasi = " + "
        elif pilihan == 2:
                hasil = angka1 - angka2
                operasi = " - "
        elif pilihan == 3:
                hasil = angka1 * angka2
                operasi = " * "
        elif pilihan == 4:
                while angka2 == 0:
                    print("Pembagian dengan angka 0 tidak diperbolehkan.")
                    angka2 = int(input("Masukkan angka: "))
                hasil = angka1 / angka2
                operasi = " / "
        elif pilihan == 5:
                hasil = angka1 % angka2
                operasi = " % "
        elif pilihan == 6:
                hasil = angka1 ** angka2
                operasi = " ^ "

        print("\nHasil Perhitungan: ")
        print(f"{angka1}{operasi}{angka2} = {hasil}\n")

if __name__ == "__main__":
    calculator()