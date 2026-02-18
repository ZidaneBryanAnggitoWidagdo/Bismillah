import random
import time
import re  
from bank_soal import QUESTIONS

DATA_FILE = "data.txt"

# =========================
# FUNGSI UTAMA
# =========================

def tampilkan_menu():
    print("\n=== MENU UTAMA ===")
    print("1. Mulai Quiz")
    print("2. Lihat Skor")
    print("3. Keluar")

def pilih_pelajaran():
    while True:
        print("\nPilih Pelajaran:")
        print("1. MTK")
        print("2. Geografi")
        print("3. Inggris")
        try:
            p = int(input("Masukkan pilihan: "))
            if p == 1:
                return "MTK"
            elif p == 2:
                return "Geografi"
            elif p == 3:
                return "Inggris"
            else:
                print("Pilihan tidak valid.")
        except:
            print("Input harus angka.")

def pilih_level():
    while True:
        print("\nPilih Level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        try:
            l = int(input("Masukkan level: ").strip())
            if l in [1, 2, 3]:
                return l
            else:
                print("Level tidak valid.")
        except:
            print("Input harus angka.")

def mulai_quiz(pelajaran, level):
    # 1. Ambil data soal dari bank_soal
    bank_soal = QUESTIONS[pelajaran][level]

    # 2. Ambil 10 soal secara acak
    soal_dipakai = random.sample(bank_soal, 10)

    skor = 0
    salah_list = []

    # --- MULAI HITUNG WAKTU ---
    waktu_mulai = time.time()

    # 3. Perulangan untuk menampilkan soal
    for idx, soal in enumerate(soal_dipakai, start=1):
        print(f"\nSoal {idx}")
        print(soal["question"])
        for k, v in soal["options"].items():
            print(f"{k}. {v}")

        while True:
            jawab = input("Jawaban (A/B/C/D): ").upper()
            if jawab in ["A", "B", "C", "D"]:
                break
            else:
                print("Input tidak valid.")

        if jawab == soal["answer"]:
            skor += 10
        else:
            salah_list.append({
                "nomor": idx,
                "pertanyaan": soal["question"],
                "jawaban_user": jawab,
                "jawaban_benar": soal["answer"],
                "opsi": soal["options"]
            })

    # --- SELESAI HITUNG WAKTU ---
    waktu_selesai = time.time()
    
    # Hitung durasi
    durasi_detik = int(waktu_selesai - waktu_mulai)
    menit = durasi_detik // 60
    detik = durasi_detik % 60

    # 4. Selesai Kuis
    print("\n=== QUIZ SELESAI ===")
    print(f"Skor akhir kamu: {skor}")
    print(f"Waktu pengerjaan: {menit} menit {detik} detik")

    # --- FITUR REKAP JAWABAN SALAH ---
    if salah_list:
        print("\n" + "="*40)
        print("   REKAP JAWABAN YANG SALAH")
        print("="*40)
        for item in salah_list:
            print(f"\nNo. {item['nomor']}: {item['pertanyaan']}")
            print(f"   Jawaban Kamu  : {item['jawaban_user']} ({item['opsi'][item['jawaban_user']]})")
            print(f"   Jawaban Benar : {item['jawaban_benar']} ({item['opsi'][item['jawaban_benar']]})")
        print("\n" + "="*40)
    else:
        print("\nSelamat! Kamu menjawab semua soal dengan benar! (Perfect Score)")

    # --- VALIDASI NAMA (ANTI EMOJI & KARAKTER ANEH) ---
    while True:
        nama = input("\nMasukkan nama untuk disimpan: ").strip()
        
        # 1. Cek jika kosong
        if not nama:
            print("Nama tidak boleh kosong!")
            continue
        
        # 2. Cek menggunakan Regex (Hanya Huruf A-Z, a-z, Angka 0-9, dan Spasi)
        # Pola: ^[A-Za-z0-9 ]+$ artinya dari awal sampai akhir harus karakter tersebut
        if re.fullmatch(r'[A-Za-z0-9 ]+', nama):
            break  # Valid, keluar dari loop
        else:
            print("Nama mengandung karakter ilegal (Emoji/Simbol). Hanya boleh huruf, angka, dan spasi.")

    # Kirim durasi ke fungsi simpan_skor
    simpan_skor(nama, pelajaran, level, skor, durasi_detik)
    
    print("\nKamu akan kembali ke Menu Utama.")
    input("Tekan [Enter] untuk melanjutkan...")
    
def simpan_skor(nama, pelajaran, level, skor, waktu_detik):
    with open(DATA_FILE, "a") as f:
        f.write(f"{nama}|{pelajaran}|{level}|{skor}|{waktu_detik}\n")
    print("Skor berhasil disimpan.")

def tampilkan_skor():
    print("\n=== DATA SKOR ===")
    try:
        with open(DATA_FILE, "r") as f:
            data = f.readlines()

            if not data:
                print("Skor belum ada di data")
                return

            for d in data:
                bagian = d.strip().split("|")

                if len(bagian) < 4:
                    continue

                nama, pelajaran, level, skor = bagian[0], bagian[1], bagian[2], bagian[3]
                
                waktu_str = ""
                if len(bagian) == 5:
                    try:
                        w_detik = int(bagian[4])
                        m = w_detik // 60
                        s = w_detik % 60
                        waktu_str = f"{m}m {s}s"
                    except:
                        waktu_str = "-"

                if level == "1":
                    level_text = "Easy"
                elif level == "2":
                    level_text = "Medium"
                else:
                    level_text = "Hard"

                print(f"{nama} | {pelajaran} | {level_text} | Skor: {skor} | Waktu: {waktu_str}")

    except FileNotFoundError:
        print("Skor belum ada di data")


# =========================
# MAIN LOOP
# =========================

def main():
    while True: 
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                pelajaran = pilih_pelajaran()
                level = pilih_level()
                mulai_quiz(pelajaran, level)
            elif pilihan == 2:
                tampilkan_skor()
            elif pilihan == 3:
                print("Terima kasih sudah bermain!")
                break
            else:
                print("Menu tidak valid.")
        except:
            print("Input harus angka.")

main()