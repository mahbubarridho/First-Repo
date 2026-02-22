import random

# ====== STRUKTUR DATA ======
data_pemain = []  # list untuk menyimpan data sementara


# ====== FUNGSI ======

def menu():
    print("\n===== GAME PETUALANGAN CLI =====")
    print("1. Mulai Game")
    print("2. Lihat Riwayat Pemenang")
    print("3. Keluar")


def mulai_game():
    nama = input("Masukkan nama pemain: ")
    ending = petualangan(nama)

    if ending != "KALAH":
        simpan_data(nama, ending)

    input("\nTekan ENTER untuk kembali ke menu...")


def petualangan(nama):
    print("\n===== PETUALANGAN DIMULAI =====")
    print("Malam gelap menyelimuti Hutan Terlarang...")
    print("Angin dingin berhembus pelan memanggil namamu,", nama)
    print("Konon siapa pun yang masuk ke hutan ini akan diuji keberanian dan hatinya.\n")

    print("Setelah berjalan cukup lama, kamu menemukan persimpangan.")
    print("KIRI → terdengar suara sungai dan cahaya biru samar.")
    print("KANAN → terlihat jalan menanjak menuju jembatan tua.")

    pilihan = input("Kamu pilih kiri / kanan? ").lower()

    # ================= JALUR KIRI =================
    if pilihan == "kiri":
        print("\nKamu berjalan menuju sungai misterius.")
        print("Airnya berkilau seperti mengandung sihir.")
        print("Di tepi sungai, kamu menemukan sebuah PERAHU tua dan juga jalan memutar.")

        pilih1 = input("Naik perahu atau jalan memutar? (perahu/jalan): ").lower()

        if pilih1 == "perahu":
            print("\nKamu mendayung perlahan ke tengah sungai...")
            print("Tiba-tiba kabut turun dan air mulai berputar!")

            pilih2 = input("Lompat ke air atau tetap di perahu? (lompat/tetap): ").lower()

            if pilih2 == "lompat":
                print("\nArus sangat kuat!")

                if random.randint(1, 2) == 1:
                    print("Seekor monster air muncul dan menyerangmu!")
                    print("💀 ENDING: DITELAN MONSTER SUNGAI")
                    return "KALAH"
                else:
                    print("Seekor naga air muncul dan menyelamatkanmu!")
                    print("🐉 ENDING RAHASIA: PENUNGGANG NAGA")
                    return "NAGA"

            elif pilih2 == "tetap":
                print("\nPerahu hampir terbalik, tapi kamu berhasil mencapai seberang.")
                print("Di sana ada peti emas terkubur di pasir.")
                print("💰 ENDING: PENEMU HARTA KARUN")
                return "KAYA"
            else:
                print("Kamu ragu terlalu lama dan perahu terbalik.")
                print("🌊 ENDING: TENGGELAM")
                return "KALAH"

        elif pilih1 == "jalan":
            print("\nKamu berjalan menyusuri hutan yang semakin gelap.")
            print("Tiba-tiba kamu menemukan reruntuhan kuil kuno.")

            pilih2 = input("Masuk ke dalam kuil atau abaikan? (masuk/abaikan): ").lower()

            if pilih2 == "masuk":
                print("\nDi dalam kuil ada teka-teki kuno.")
                jawab = input("Berapa hasil 3 x 3? ")

                if jawab == "9":
                    print("Pintu rahasia terbuka!")
                    print("🏆 ENDING: PAHLAWAN PENAKLUK KUIL")
                    return "PAHLAWAN"
                else:
                    print("Lantai runtuh di bawah kakimu.")
                    print("💀 ENDING: TERJEBAK DI KUIL")
                    return "KALAH"
            else:
                print("Kamu melewati kesempatan besar dan tersesat.")
                print("🌫 ENDING: HILANG DI HUTAN")
                return "KALAH"
        else:
            print("Kamu bingung dan kembali ke awal... tapi tersesat.")
            print("🌑 ENDING: LENYAP TANPA JEJAK")
            return "KALAH"

    # ================= JALUR KANAN =================
    elif pilihan == "kanan":
        print("\nKamu mendaki jalan berbatu menuju jembatan tua.")
        print("Di bawahnya jurang gelap tak terlihat dasarnya.")
        print("Saat hampir menyeberang, kamu melihat PEDANG tua tertancap di tanah.")

        pilih1 = input("Ambil pedang atau abaikan? (ambil/abaikan): ").lower()

        if pilih1 == "ambil":
            print("\nSaat kamu mencabut pedang, cahaya menyelimuti tubuhmu.")
            print("Tiba-tiba muncul penjaga bayangan!")

            pilih2 = input("Lawan atau lari? (lawan/lari): ").lower()

            if pilih2 == "lawan":
                if random.randint(1, 2) == 1:
                    print("Dengan pedang suci, kamu mengalahkannya!")
                    print("🏆 ENDING: SANG KSATRIA LEGENDA")
                    return "PAHLAWAN"
                else:
                    print("Penjaga terlalu kuat.")
                    print("💀 ENDING: GUGUR SEBAGAI PEJUANG")
                    return "KALAH"
            else:
                print("Kamu terpeleset saat lari dan jatuh ke jurang.")
                print("💀 ENDING: TERJATUH")
                return "KALAH"

        elif pilih1 == "abaikan":
            print("\nKamu menyeberangi jembatan dengan hati-hati.")
            print("Di ujung jembatan ada pria berjubah hitam.")

            bicara = input("Berbicara dengannya? (ya/tidak): ").lower()

            if bicara == "ya":
                print("Ia menawarkanmu kekayaan atau kekuasaan.")
                pilih2 = input("Pilih kekayaan atau kekuasaan? ").lower()

                if pilih2 == "kekayaan":
                    print("💰 ENDING: PENGUASA EMAS")
                    return "KAYA"
                elif pilih2 == "kekuasaan":
                    print("🏆 ENDING: RAJA HUTAN TERLARANG")
                    return "PAHLAWAN"
                else:
                    print("Ia marah karena jawabanmu tidak jelas.")
                    print("💀 ENDING: DIKUTUK")
                    return "KALAH"
            else:
                print("Pria itu menghilang dan jembatan runtuh.")
                print("💀 ENDING: TERPERANGKAP DI JURANG")
                return "KALAH"

        else:
            print("Langkahmu salah dan papan jembatan patah.")
            print("💀 ENDING: TERJATUH")
            return "KALAH"

    else:
        print("\nKamu diam terlalu lama.")
        print("Kabut perlahan menelan tubuhmu.")
        print("🌑 ENDING: LENYAP TANPA JEJAK")
        return "KALAH"


def simpan_data(nama, ending):
    data = {"nama": nama, "ending": ending}
    data_pemain.append(data)

    try:
        with open("data.txt", "a") as file:
            file.write(nama + " - " + ending + "\n")
    except:
        print("⚠ Gagal menyimpan ke file. Periksa izin folder.")


def lihat_data():
    print("\n===== RIWAYAT PEMENANG =====")
    try:
        with open("data.txt", "r") as file:
            isi = file.read()
            if isi == "":
                print("Belum ada data.")
            else:
                print(isi)
    except FileNotFoundError:
        print("File data.txt belum ada.")


# ===== PROGRAM UTAMA =====
if __name__ == "__main__":
    while True:
        menu()

        try:
            pilihan = int(input("Pilih menu (1-3): "))
        except:
            print("Input harus angka!")
            continue

        if pilihan == 1:
            mulai_game()
        elif pilihan == 2:
            lihat_data()
        elif pilihan == 3:
            print("Terima kasih sudah bermain!")
            break
        else:
            print("Menu tidak tersedia.")