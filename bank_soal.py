def generate_questions(subject, level):
    questions = []

    if subject == "MTK":
        if level == 1:
            questions.append({
                "question": "Hasil dari 5 + 3 adalah...",
                "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
                "answer": "C"
                })
            questions.append({
                "question": "Hasil dari 12 − 4 adalah...",
                "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
                "answer": "C"
                })
            questions.append({
                "question": "Hasil dari 2 × 5 adalah...",
                "options": {"A": "7", "B": "10", "C": "12", "D": "15"},
                "answer": "B"
                })
            questions.append({
                "question": "8 + 8 = ...",
                "options": {"A": "14", "B": "15", "C": "16", "D": "17"},
                "answer": "C"
                })
            questions.append({
                "question": "15 − 7 = ...",
                "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
                "answer": "C"
                })
            questions.append({
                "question": "4 × 3 = ...",
                "options": {"A": "7", "B": "10", "C": "12", "D": "14"},
                "answer": "C"
                })
            questions.append({
                "question": "20 + 10 = ...",
                "options": {"A": "25", "B": "30", "C": "35", "D": "40"},
                "answer": "B"
                })
            questions.append({
                "question": "25 − 5 = ...",
                "options": {"A": "15", "B": "20", "C": "25", "D": "30"},
                "answer": "B"
                })
            questions.append({
                "question": "6 × 2 = ...",
                "options": {"A": "8", "B": "4", "C": "12", "D": "14"},
                "answer": "C"
                })
            questions.append({
                "question": "9 + 6 = ...",
                "options": {"A": "13", "B": "14", "C": "15", "D": "16"},
                "answer": "C"
                })
            questions.append({
                "question": "30 − 12 = ...",
                "options": {"A": "12", "B": "18", "C": "20", "D": "22"},
                "answer": "B"
                })
            questions.append({
                "question": "5 × 5 = ...",
                "options": {"A": "10", "B": "20", "C": "25", "D": "30"},
                "answer": "C"
                })
            questions.append({
                "question": "11 + 9 = ...",
                "options": {"A": "18", "B": "20", "C": "21", "D": "22"},
                "answer": "B"
                })
            questions.append({
                "question": "18 − 9 = ...",
                "options": {"A": "8", "B": "9", "C": "10", "D": "7"},
                "answer": "B"
                })
            questions.append({
                "question": "3 × 8 = ...",
                "options": {"A": "18", "B": "21", "C": "24", "D": "27"},
                "answer": "C"
                })
            questions.append({
                "question": "Andi memiliki 3 apel. Ibunya memberikan 2 apel lagi. Berapa jumlah apel Andi sekarang?",
                "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
                "answer": "B"
                })
            questions.append({
                "question": "Siti mempunyai 10 permen. Ia memakan 4 permen. Berapa sisa permen Siti?",
                "options": {"A": "4", "B": "5", "C": "6", "D": "8"},
                "answer": "C"
                })
            questions.append({
                "question": "Ada 4 kelompok siswa. Setiap kelompok terdiri dari 2 siswa. Berapa jumlah siswa semuanya?",
                "options": {"A": "6", "B": "8", "C": "10", "D": "12"},
                "answer": "B"
                })
            questions.append({
                "question": "Ayah membeli 5 jeruk dan 3 mangga. Berapa total buah yang dibeli ayah?",
                "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
                "answer": "C"
                })
            questions.append({
                "question": "Ada 12 burung di pohon, 5 burung terbang. Berapa burung yang tersisa?",
                "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
                "answer": "C"
                })
            questions.append({
                "question": "Harga satu buku adalah Rp 2.000,00. Budi membeli 2 buku. Berapa harga yang harus dibayar?",
                "options": {"A": "Rp 2.000,00", "B": "Rp 3.000,00", "C": "Rp 4.000,00", "D": "Rp 5.000,00"},
                "answer": "C"
                })
            questions.append({
                "question": "Ibu memiliki 15 telur. Ibu menggunakan 5 telur untuk membuat kue. Berapa sisa telur Ibu?",
                "options": {"A": "8", "B": "9", "C": "10", "D": "12"},
                "answer": "C"
                })
            questions.append({
                "question": "Di halaman sekolah ada 3 sepeda motor dan 3 mobil. Berapa total kendaraan di halaman sekolah?",
                "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
                "answer": "C"
                })
            questions.append({
                "question": "Sebuah aquarium berisi 8 ikan mas. Ayah membeli lagi 2 ikan. Berapa total ikan di aquarium sekarang?",
                "options": {"A": "8", "B": "9", "C": "10", "D": "11"},
                "answer": "C"
                })
            questions.append({
                "question": "Roni menabung Rp 5.000,00 hari ini dan Rp 5.000,00 besok. Berapa total tabungan Roni?",
                "options": {"A": "Rp 5.000,00", "B": "Rp 10.000,00", "C": "Rp 15.000,00", "D": "Rp 20.000,00"},
                "answer": "B"
                })
            questions.append({
                "question": "Lengkapi urutan angka ini: 2, 4, 6, 8, ...",
                "options": {"A": "9", "B": "10", "C": "11", "D": "12"},
                "answer": "B"
                })
            questions.append({
                "question": "Lengkapi urutan angka ini: 10, 20, 30, 40, ...",
                "options": {"A": "45", "B": "50", "C": "55", "D": "60"},
                "answer": "B"
                })
            questions.append({
                "question": "Mana yang angka yang lebih besar?",
                "options": {"A": "15", "B": "25", "C": "10", "D": "5"},
                "answer": "B"
                })
            questions.append({
                "question": "Mana yang angka yang lebih kecil?",
                "options": {"A": "9", "B": "19", "C": "29", "D": "39"},
                "answer": "A"
                })
            questions.append({
                "question": "Setengah dari 10 adalah...",
                "options": {"A": "2", "B": "4", "C": "5", "D": "6"},
                "answer": "C"
                })
            questions.append({
                "question": "Seperempat dari 8 adalah...",
                "options": {"A": "1", "B": "2", "C": "4", "D": "6"},
                "answer": "B"
                })
            questions.append({
                "question": "Bentuk persegi memiliki berapa sisi?",
                "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
                "answer": "B"
                })
            questions.append({
                "question": "Bentuk segitiga memiliki berapa sudut?",
                "options": {"A": "2", "B": "3", "C": "4", "D": "5"},
                "answer": "B"
                })
            questions.append({
                "question": "Simbol angka Romawi untuk 5 adalah...",
                "options": {"A": "I", "B": "V", "C": "X", "D": "L"},
                "answer": "B"
                })
            questions.append({
                "question": "Jika jam menunjukkan pukul 08:00, 2 jam kemudian jam menunjukkan pukul berapa?",
                "options": {"A": "09:00", "B": "10:00", "C": "11:00", "D": "12:00"},
                "answer": "B"
                })
            questions.append({
                "question": "5 + 2 + 3 = ...",
                "options": {"A": "8", "B": "9", "C": "10", "D": "11"},
                "answer": "C"
                })
            questions.append({
                "question": "10 − 2 − 3 = ...",
                "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
                "answer": "B"
                })
            questions.append({
                "question": "2 × 3 + 1 = ...",
                "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
                "answer": "C"
                })
            questions.append({
                "question": "15 + 5 − 10 = ...",
                "options": {"A": "5", "B": "10", "C": "15", "D": "20"},
                "answer": "B"
                })
            questions.append({
                "question": "4 × 2 + 2 = ...",
                "options": {"A": "6", "B": "8", "C": "10", "D": "12"},
                "answer": "C"
                })
            questions.append({
                "question": "25 + 25 = ...",
                "options": {"A": "40", "B": "45", "C": "50", "D": "55"},
                "answer": "C"
                })
            questions.append({
                "question": "50 − 25 = ...",
                "options": {"A": "15", "B": "20", "C": "25", "D": "30"},
                "answer": "C"
                })
            questions.append({
                "question": "10 × 5 = ...",
                "options": {"A": "15", "B": "50", "C": "55", "D": "100"},
                "answer": "B"
                })
            questions.append({
                "question": "100 − 10 = ...",
                "options": {"A": "80", "B": "90", "C": "95", "D": "110"},
                "answer": "B"
                })
            questions.append({
                "question": "0 + 100 = ...",
                "options": {"A": "0", "B": "10", "C": "100", "D": "1000"},
                "answer": "C"
                })
            questions.append({
                "question": "Isi titik-titik: 12 + ... = 20",
                "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
                "answer": "C"
                })
            questions.append({
                "question": "Isi titik-titik: ... − 5 = 10",
                "options": {"A": "5", "B": "10", "C": "15", "D": "20"},
                "answer": "C"
                })
            questions.append({
                "question": "Isi titik-titik: 3 × ... = 9",
                "options": {"A": "2", "B": "3", "C": "4", "D": "6"},
                "answer": "B"
                })
            questions.append({
                "question": "Berapa hasil dari 10 × 10 ?",
                "options": {"A": "20", "B": "50", "C": "100", "D": "1000"},
                "answer": "C"
                })
            questions.append({
                "question": "Jumlahkan semua angka ganjil dari 1 sampai 5 (1 + 3 + 5)?",
                "options": {"A": "7", "B": "8", "C": "9", "D": "10"},
                "answer": "C"
                })
            
        elif level == 2:
            questions.append({
                "question": "Hasil dari 3/4 + 5/6 adalah ...",
                "options": {"A": "19/12", "B": "38/24", "C": "29/12", "D": "9/10"},
                "answer": "A"
            })
            questions.append({
                "question": "Hasil dari 3/4 - 1/8 adalah ...",
                "options": {"A": "3/8", "B": "5/8", "C": "1/2", "D": "7/4"},
                "answer": "B"
            })
            questions.append({
                "question": "Hasil dari 2/3 x 9/10 adalah ...",
                "options": {"A": "3/5", "B": "6/10", "C": "18/30", "D": "27/30"},
                "answer": "A"
            })
            questions.append({
                "question": "Hasil dari 3/4 + 1/2 adalah ...",
                "options": {"A": "15/12", "B": "5/4", "C": "10/18", "D": "3/5"},
                "answer": "B"
            })
            questions.append({
                "question": "Hasil dari 1/2 + 3/5 adalah ...",
                "options": {"A": "7/15", "B": "11/10", "C": "1 1/10", "D": "13/10"},
                "answer": "C"
            })
            questions.append({
                "question": "6/8 disederhanakan menjadi ...",
                "options": {"A": "3/4", "B": "2/3", "C": "4/9", "D": "6/8"},
                "answer": "A"
            })
            questions.append({
                "question": "2 1/3 = ...",
                "options": {"A": "5/3", "B": "7/3", "C": "6/3", "D": "8/3"},
                "answer": "B"
            })
            questions.append({
                "question": "Hasil dari 5/9 x 3 adalah ...",
                "options": {"A": "5/3", "B": "15/9", "C": "5/27", "D": "15/27"},
                "answer": "A"
            })
            questions.append({
                "question": "Hasil dari 1/3 x 2/5 adalah ...",
                "options": {"A": "2/15", "B": "4/15", "C": "6/15", "D": "10/15"},
                "answer": "A"
            })
            questions.append({
                "question": "Hasil dari 1/2 x 3/5 adalah ...",
                "options": {"A": "3/10", "B": "6/5", "C": "2/5", "D": "5/6"},
                "answer": "A"
            })
            questions.append({
                "question": "Hasil dari 2/3 + 7/9 adalah ...",
                "options": {"A": "13/9", "B": "11/9", "C": "1", "D": "14/9"},
                "answer": "A"
            })
            questions.append({
                "question": "Hasil dari 3/7 x 1/2 adalah ...",
                "options": {"A": "3/14", "B": "6/14", "C": "9/14", "D": "12/14"},
                "answer": "A"
            })
            questions.append({
                "question": "Hasil dari 4/9 x 3/2 adalah ...",
                "options": {"A": "2/3", "B": "4/6", "C": "12/18", "D": "8/27"},
                "answer": "A"
            })
            questions.append({
                "question": "0,75 dalam bentuk pecahan adalah ...",
                "options": {"A": "3/5", "B": "3/4", "C": "75/1000", "D": "7/10"},
                "answer": "B"
            })
            questions.append({
                "question": "Hasil dari 1/2 + 2/3 adalah ...",
                "options": {"A": "12/18", "B": "13/12", "C": "7/6", "D": "15/12"},
                "answer": "C"
            })

            questions.append({
                "question": "√64 = ...",
                "options": {"A": "6", "B": "7", "C": "8", "D": "9"},
                "answer": "C"
            })
            questions.append({
                "question": "√81 = ...",
                "options": {"A": "8", "B": "9", "C": "7", "D": "6"},
                "answer": "B"
            })
            questions.append({
                "question": "√50 disederhanakan menjadi ...",
                "options": {"A": "5√2", "B": "25√2", "C": "√25 × √2", "D": "10√5"},
                "answer": "A"
            })
            questions.append({
                "question": "√72 = ...",
                "options": {"A": "6√2", "B": "8√2", "C": "12√2", "D": "4√3"},
                "answer": "A"
            })
            questions.append({
                "question": "√(49/9) = ...",
                "options": {"A": "7/9", "B": "9/7", "C": "7/3", "D": "3/7"},
                "answer": "C"
            })
            questions.append({
                "question": "2√3 + 5√3 = ...",
                "options": {"A": "7√6", "B": "10√3", "C": "7√3", "D": "3√3"},
                "answer": "C"
            })
            questions.append({
                "question": "6√5 − 2√5 = ...",
                "options": {"A": "4√5", "B": "3√5", "C": "8√5", "D": "12√5"},
                "answer": "A"
            })
            questions.append({
                "question": "√18 = ...",
                "options": {"A": "3√2", "B": "2√3", "C": "6√3", "D": "9√2"},
                "answer": "A"
            })
            questions.append({
                "question": "(√7)² = ...",
                "options": {"A": "14", "B": "7", "C": "√14", "D": "49"},
                "answer": "B"
            })
            questions.append({
                "question": "√125 = ...",
                "options": {"A": "25√5", "B": "5√5", "C": "5√25", "D": "25√2"},
                "answer": "B"
            })
            questions.append({
                "question": "√(16 × 25) = ...",
                "options": {"A": "20", "B": "40", "C": "10", "D": "400"},
                "answer": "A"
            })
            questions.append({
                "question": "3√2 × 2√2 = ...",
                "options": {"A": "12", "B": "6", "C": "12√2", "D": "6√2"},
                "answer": "A"
            })
            questions.append({
                "question": "√98 = ...",
                "options": {"A": "7√2", "B": "14√2", "C": "49√2", "D": "9√2"},
                "answer": "A"
            })
            questions.append({
                "question": "√(1/16) = ...",
                "options": {"A": "1/4", "B": "4", "C": "1/8", "D": "2"},
                "answer": "A"
            })
            questions.append({
                "question": "4√3 + √3 = ...",
                "options": {"A": "4√6", "B": "5√3", "C": "4√9", "D": "3√4"},
                "answer": "B"
            })

            questions.append({
                "question": "2³ = ...",
                "options": {"A": "6", "B": "8", "C": "9", "D": "12"},
                "answer": "B"
            })
            questions.append({
                "question": "5² = ...",
                "options": {"A": "10", "B": "15", "C": "25", "D": "20"},
                "answer": "C"
            })
            questions.append({
                "question": "3⁴ = ...",
                "options": {"A": "64", "B": "27", "C": "81", "D": "12"},
                "answer": "C"
            })
            questions.append({
                "question": "10³ = ...",
                "options": {"A": "100", "B": "1000", "C": "10000", "D": "300"},
                "answer": "B"
            })
            questions.append({
                "question": "4² × 4³ = ...",
                "options": {"A": "4⁵", "B": "16", "C": "4⁶", "D": "64"},
                "answer": "A"
            })
            questions.append({
                "question": "6⁴ ÷ 6² = ...",
                "options": {"A": "6²", "B": "6⁶", "C": "6³", "D": "36"},
                "answer": "A"
            })
            questions.append({
                "question": "(2³)² = ...",
                "options": {"A": "2⁵", "B": "2⁶", "C": "2⁹", "D": "2¹"},
                "answer": "B"
            })
            questions.append({
                "question": "7⁰ = ...",
                "options": {"A": "7", "B": "1", "C": "0", "D": "70"},
                "answer": "B"
            })
            questions.append({
                "question": "9½ = ...",
                "options": {"A": "3", "B": "√9", "C": "81", "D": "1/9"},
                "answer": "A"
            })
            questions.append({
                "question": "16½ = ...",
                "options": {"A": "8", "B": "2", "C": "4", "D": "16"},
                "answer": "C"
            })
            questions.append({
                "question": "2⁴ × 2² = ...",
                "options": {"A": "2⁶", "B": "2⁸", "C": "4⁶", "D": "2²"},
                "answer": "A"
            })
            questions.append({
                "question": "3³ ÷ 3 = ...",
                "options": {"A": "3²", "B": "3³", "C": "3", "D": "9"},
                "answer": "A"
            })
            questions.append({
                "question": "(5²)³ = ...",
                "options": {"A": "5⁵", "B": "5⁶", "C": "25⁶", "D": "5⁹"},
                "answer": "B"
            })
            questions.append({
                "question": "8¹/³ = ...",
                "options": {"A": "2", "B": "4", "C": "8", "D": "16"},
                "answer": "A"
            })
            questions.append({
                "question": "27¹/³ = ...",
                "options": {"A": "3", "B": "9", "C": "6", "D": "1"},
                "answer": "A"
            })
            questions.append({
                "question": "2⁵ = ...",
                "options": {"A": "10", "B": "16", "C": "32", "D": "64"},
                "answer": "C"
            })
            questions.append({
                "question": "3² + 4² = ...",
                "options": {"A": "7", "B": "12", "C": "25", "D": "49"},
                "answer": "C"
            })
            questions.append({
                "question": "5³ − 5² = ...",
                "options": {"A": "100", "B": "75", "C": "25", "D": "50"},
                "answer": "A"
            })
            questions.append({
                "question": "(√5)² = ...",
                "options": {"A": "10", "B": "25", "C": "5", "D": "√10"},
                "answer": "C"
            })
            questions.append({
                "question": "4⁻¹ = ...",
                "options": {"A": "4", "B": "-4", "C": "1/4", "D": "1"},
                "answer": "C"
            })
        else: #level 3
            questions.append({
                "question": "Nilai cos 0° adalah …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 30° adalah …",
                "options": {"A": "1/2", "B": "√2/2", "C": "√3/2", "D": "0"},
                "answer": "C"
            })
            questions.append({
                "question": "Nilai cos 45° adalah …",
                "options": {"A": "√3/2", "B": "√2/2", "C": "1/2", "D": "0"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 60° adalah …",
                "options": {"A": "1/2", "B": "√3/2", "C": "0", "D": "1"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 90° adalah …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 120° adalah …",
                "options": {"A": "1/2", "B": "-1/2", "C": "√3/2", "D": "-√3/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 180° adalah …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "1/2"},
                "answer": "C"
            })
            questions.append({
                "question": "Nilai cos 270° adalah …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "Tidak terdefinisi"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 360° adalah …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Jika cos θ = 3/5 (θ lancip), maka sin θ = …",
                "options": {"A": "4/5", "B": "3/4", "C": "5/4", "D": "2/5"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos θ = 4/5 (θ lancip), maka tan θ = …",
                "options": {"A": "3/4", "B": "4/3", "C": "5/4", "D": "1"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos (30° + 60°) adalah …",
                "options": {"A": "1", "B": "0", "C": "1/2", "D": "-1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos (60° − 30°) adalah …",
                "options": {"A": "1/2", "B": "√3/2", "C": "0", "D": "-1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos (45° + 45°) adalah …",
                "options": {"A": "1", "B": "0", "C": "-1", "D": "1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos (45° − 45°) adalah …",
                "options": {"A": "1", "B": "0", "C": "-1", "D": "1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Identitas yang benar adalah …",
                "options": {"A": "sin²x − cos²x = 1", "B": "sin²x + cos²x = 1", "C": "cos²x − sin²x = 1", "D": "tan²x = 1 + sec²x"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos (−60°) adalah …",
                "options": {"A": "-1/2", "B": "1/2", "C": "0", "D": "-1"},
                "answer": "B"
            })
            questions.append({
                "question": "Jika sin θ = 1/2 (θ lancip), maka cos θ = …",
                "options": {"A": "1/2", "B": "√3/2", "C": "√2/2", "D": "0"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 150° adalah …",
                "options": {"A": "√3/2", "B": "-√3/2", "C": "1/2", "D": "-1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 210° adalah …",
                "options": {"A": "-√3/2", "B": "-1/2", "C": "√3/2", "D": "1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 240° adalah …",
                "options": {"A": "-1/2", "B": "-√3/2", "C": "√3/2", "D": "1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 300° adalah …",
                "options": {"A": "1/2", "B": "-1/2", "C": "√3/2", "D": "-√3/2"},
                "answer": "C"
            })
            questions.append({
                "question": "Jika cos x = 1/2, maka x (0°–360°) adalah …",
                "options": {"A": "60° dan 300°", "B": "30° dan 150°", "C": "45° dan 315°", "D": "90° dan 270°"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos x = −1/2, maka x (0°–360°) adalah …",
                "options": {"A": "60° dan 300°", "B": "120° dan 240°", "C": "30° dan 210°", "D": "45° dan 225°"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos²45° adalah …",
                "options": {"A": "1", "B": "1/2", "C": "√2/2", "D": "2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai 2cos30°sin30° adalah …",
                "options": {"A": "√3/2", "B": "1/2", "C": "√2/2", "D": "1"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos²60° adalah …",
                "options": {"A": "1/4", "B": "1/2", "C": "3/4", "D": "1"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos A = 5/13 (A lancip), maka sin A = …",
                "options": {"A": "12/13", "B": "5/12", "C": "13/12", "D": "8/13"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos (90° − x) adalah …",
                "options": {"A": "cos x", "B": "sin x", "C": "-sin x", "D": "-cos x"},
                "answer": "B"
            })
            questions.append({
                "question": "Jika cos θ = 0, maka θ adalah …",
                "options": {"A": "0°", "B": "90°", "C": "180°", "D": "360°"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 135° adalah …",
                "options": {"A": "√2/2", "B": "-√2/2", "C": "1/2", "D": "-1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 225° adalah …",
                "options": {"A": "-√2/2", "B": "√2/2", "C": "1/2", "D": "-1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 315° adalah …",
                "options": {"A": "√2/2", "B": "-√2/2", "C": "1/2", "D": "-1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos θ = -1, maka θ = …",
                "options": {"A": "90°", "B": "180°", "C": "270°", "D": "360°"},
                "answer": "B"
            })
            questions.append({
                "question": "Jika cos θ = 1, maka θ = …",
                "options": {"A": "0°", "B": "90°", "C": "180°", "D": "270°"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos²x + sin²x = …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "2"},
                "answer": "B"
            })
            questions.append({
                "question": "Jika cos θ = 1/√2, maka θ = …",
                "options": {"A": "30°", "B": "45°", "C": "60°", "D": "90°"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 75° adalah …",
                "options": {"A": "(√6 + √2)/4", "B": "(√6 − √2)/4", "C": "(√3)/2", "D": "1/2"},
                "answer": "B"
            })
            questions.append({
                "question": "Nilai cos 15° adalah …",
                "options": {"A": "(√6 + √2)/4", "B": "(√6 − √2)/4", "C": "√3/2", "D": "1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos θ = 2/√5, maka sin θ = …",
                "options": {"A": "1/√5", "B": "√3/√5", "C": "√5/2", "D": "2/5"},
                "answer": "A"
            })
            questions.append({
                "question": "Dalam segitiga, jika a=3, b=4, C=90°, maka c = …",
                "options": {"A": "5", "B": "6", "C": "7", "D": "4"},
                "answer": "A"
            })
            questions.append({
                "question": "Dalam segitiga, jika a=5, b=5, C=60°, maka c = …",
                "options": {"A": "5", "B": "√50", "C": "√25", "D": "√75"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos 2θ = 1, maka θ = …",
                "options": {"A": "0°", "B": "45°", "C": "90°", "D": "180°"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos²30° adalah …",
                "options": {"A": "3/4", "B": "1/2", "C": "1/4", "D": "1"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 330° adalah …",
                "options": {"A": "√3/2", "B": "-√3/2", "C": "1/2", "D": "-1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos θ = 1/2 dan θ lancip, maka θ = …",
                "options": {"A": "30°", "B": "45°", "C": "60°", "D": "90°"},
                "answer": "C"
            })
            questions.append({
                "question": "Nilai cos 210° + cos 330° adalah …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "1/2"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 0° + cos 180° adalah …",
                "options": {"A": "0", "B": "1", "C": "-1", "D": "2"},
                "answer": "A"
            })
            questions.append({
                "question": "Jika cos θ = -√2/2, maka θ = …",
                "options": {"A": "135°", "B": "45°", "C": "60°", "D": "30°"},
                "answer": "A"
            })
            questions.append({
                "question": "Nilai cos 360° − cos 180° adalah …",
                "options": {"A": "0", "B": "1", "C": "2", "D": "-1"},
                "answer": "C"
            })

    elif subject == "Geografi":
        if level == 1:
            questions.append({
                "question": "Ibukota Indonesia adalah?",
                "options": {"A": "Bandung", "B": "Jakarta", "C": "Surabaya", "D": "Medan"},
                "answer": "B"
            })
            questions.append({
                "question": "Jakarta adalah ibukota dari negara",
                "options": {"A": "Malaysia", "B": "Timor leste", "C": "Indonesia", "D": "Philipines"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari negara UK",
                "options": {"A": "London", "B": "Wachington,D.C", "C": "Dublin", "D": "Ottawa"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari negara Russia",
                "options": {"A": "Ottawa", "B": "Minsk", "C": "Tallinn", "D": "Moscow"},
                "answer": "D"
            })

            questions.append({
                "question": "Negara indonesia termasuk dalam benua",
                "options": {"A": "Amerika", "B": "Eropa", "C": "Asia", "D": "Antartika"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa nama Gunung yang tertinggi di dunia?",
                "options": {"A": "Gunung Kilimanjaro", "B": "Gunung Everest", "C": "Gunung Elbrus", "D": "Gunung Jaya Wijaya"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Dili",
                "options": {"A": "Timor Leste", "B": "Papua Nugini", "C": "Brunei Darussalam", "D": "Filipina"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Manila",
                "options": {"A": "Thailand", "B": "Vietnam", "C": "Filipina", "D": "Malaysia"},
                "answer": "C"
            })

            questions.append({
                "question": "di negara mana ada bangunan ka'bah yang digunakan oleh orang muslim untuk haji?",
                "options": {"A": "Mesir", "B": "Arab Saudi", "C": "Turki", "D": "Uni Emirat Arab"},
                "answer": "B"
            })

            questions.append({
                "question": "Lautan apa yang membelah pulau kalimantan dan jawa?",
                "options": {"A": "Laut Sulawesi", "B": "Laut Banda", "C": "Laut Jawa", "D": "Laut Natuna"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari negara Jepang?",
                "options": {"A": "Beijing", "B": "Seoul", "C": "Tokyo", "D": "Bangkok"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari negara Korea Selatan?",
                "options": {"A": "Pyongyang", "B": "Seoul", "C": "Tokyo", "D": "Taipei"},
                "answer": "B"
            })

            questions.append({
                "question": "Kuala Lumpur adalah ibukota dari negara...",
                "options": {"A": "Thailand", "B": "Malaysia", "C": "Singapura", "D": "Brunei"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari negara Amerika Serikat?",
                "options": {"A": "New York", "B": "Los Angeles", "C": "Washington, D.C.", "D": "Chicago"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari negara Australia?",
                "options": {"A": "Sydney", "B": "Canberra", "C": "Melbourne", "D": "Perth"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari negara Jerman?",
                "options": {"A": "Munchen", "B": "Berlin", "C": "Frankfurt", "D": "Hamburg"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari negara Perancis?",
                "options": {"A": "London", "B": "Paris", "C": "Madrid", "D": "Roma"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari negara China?",
                "options": {"A": "Shanghai", "B": "Beijing", "C": "Hong Kong", "D": "Taipei"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari negara India?",
                "options": {"A": "Mumbai", "B": "New Delhi", "C": "Bangalore", "D": "Kolkata"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Tokyo?",
                "options": {"A": "Korea Selatan", "B": "Jepang", "C": "China", "D": "Vietnam"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Seoul?",
                "options": {"A": "Korea Utara", "B": "Korea Selatan", "C": "Jepang", "D": "Taiwan"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Canberra?",
                "options": {"A": "Austria", "B": "Australia", "C": "Selandia Baru", "D": "Amerika Serikat"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Beijing?",
                "options": {"A": "China", "B": "Jepang", "C": "Korea Utara", "D": "Vietnam"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Paris?",
                "options": {"A": "Italia", "B": "Spanyol", "C": "Perancis", "D": "Belgia"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Berlin?",
                "options": {"A": "Austria", "B": "Jerman", "C": "Swiss", "D": "Belanda"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Roma?",
                "options": {"A": "Perancis", "B": "Italia", "C": "Spanyol", "D": "Yunani"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Madrid?",
                "options": {"A": "Meksiko", "B": "Spanyol", "C": "Argentina", "D": "Portugal"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah Cairo?",
                "options": {"A": "Maroko", "B": "Mesir", "C": "Libya", "D": "Sudan"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa negara yang ibukotanya adalah New Delhi?",
                "options": {"A": "Pakistan", "B": "India", "C": "Bangladesh", "D": "Nepal"},
                "answer": "B"
            })

            questions.append({
                "question": "Negara Jepang termasuk dalam benua...",
                "options": {"A": "Eropa", "B": "Asia", "C": "Afrika", "D": "Amerika"},
                "answer": "B"
            })

            questions.append({
                "question": "Negara Amerika Serikat termasuk dalam benua...",
                "options": {"A": "Asia", "B": "Amerika Utara", "C": "Eropa", "D": "Amerika Selatan"},
                "answer": "B"
            })

            questions.append({
                "question": "Negara Brasil termasuk dalam benua...",
                "options": {"A": "Amerika Utara", "B": "Amerika Selatan", "C": "Afrika", "D": "Eropa"},
                "answer": "B"
            })

            questions.append({
                "question": "Negara Jerman termasuk dalam benua...",
                "options": {"A": "Eropa", "B": "Asia", "C": "Amerika", "D": "Australia"},
                "answer": "A"
            })

            questions.append({
                "question": "Negara Mesir termasuk dalam benua...",
                "options": {"A": "Asia", "B": "Afrika", "C": "Eropa", "D": "Amerika"},
                "answer": "B"
            })

            questions.append({
                "question": "Lautan apa yang terbesar di dunia?",
                "options": {"A": "Lautan Atlantik", "B": "Lautan Pasifik", "C": "Lautan Hindia", "D": "Lautan Arktik"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa nama sungai terpanjang di dunia?",
                "options": {"A": "Sungai Amazon", "B": "Sungai Nil", "C": "Sungai Mississippi", "D": "Sungai Yangtze"},
                "answer": "B"
            })

            questions.append({
                "question": "Di negara mana Menara Eiffel berada?",
                "options": {"A": "Italia", "B": "Perancis", "C": "Inggris", "D": "Jerman"},
                "answer": "B"
            })

            questions.append({
                "question": "Di negara mana Tembok Besar (Great Wall) berada?",
                "options": {"A": "China", "B": "Jepang", "C": "Korea", "D": "India"},
                "answer": "A"
            })

            questions.append({
                "question": "Di negara mana Colosseum berada?",
                "options": {"A": "Yunani", "B": "Italia", "C": "Turki", "D": "Spanyol"},
                "answer": "B"
            })

            questions.append({
                "question": "Di negara mana Taj Mahal berada?",
                "options": {"A": "Pakistan", "B": "India", "C": "Bangladesh", "D": "Nepal"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa mata uang resmi negara Indonesia?",
                "options": {"A": "Dollar", "B": "Rupiah", "C": "Ringgit", "D": "Yen"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa mata uang resmi negara Amerika Serikat?",
                "options": {"A": "Dollar", "B": "Euro", "C": "Pound", "D": "Peso"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa mata uang resmi negara Jepang?",
                "options": {"A": "Won", "B": "Yen", "C": "Yuan", "D": "Ringgit"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa mata uang resmi negara Malaysia?",
                "options": {"A": "Rupiah", "B": "Dollar", "C": "Ringgit", "D": "Baht"},
                "answer": "C"
            })

            questions.append({
                "question": "Hewan Kangguru adalah hewan khas dari negara?",
                "options": {"A": "Indonesia", "B": "Australia", "C": "Papua Nugini", "D": "Selandia Baru"},
                "answer": "B"
            })

            questions.append({
                "question": "Hewan Panda adalah hewan khas dari negara?",
                "options": {"A": "Jepang", "B": "China", "C": "Korea", "D": "India"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa nama selat yang memisahkan Pulau Sumatra dan Pulau Jawa?",
                "options": {"A": "Selat Malaka", "B": "Selat Sunda", "C": "Selat Bali", "D": "Selat Lombok"},
                "answer": "B"
            })

            questions.append({
                "question": "Negara yang terkenal dengan Patung Liberty adalah...",
                "options": {"A": "Perancis", "B": "Amerika Serikat", "C": "Inggris", "D": "Brasil"},
                "answer": "B"
            })

            questions.append({
                "question": "Negara yang terkenal dengan Menara Pisa adalah...",
                "options": {"A": "Perancis", "B": "Italia", "C": "Yunani", "D": "Spanyol"},
                "answer": "B"
            })

        elif level == 2:
            questions.append({
                "question": "Geo Medium: Gunung tertinggi di Indonesia?",
                "options": {"A": "Semeru", "B": "Rinjani", "C": "Puncak Jaya", "D": "Kerinci"},
                "answer": "C"
            }) 
            questions.append({
                "question": "Gunung tertinggi di pulau jawa adalah?",
                "options": {"A": "Kerinci", "B": "Rinjani", "C": "Slamet", "D": "Semeru"},
                "answer": "D"
            })

            questions.append({
                "question": "Wilayah indonesia bagian apa yang letaknya berada di ujung barat indonesia?",
                "options": {"A": "Sabang", "B": "Merauke", "C": "Jayapura", "D": "Miangas"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi jawa barat?",
                "options": {"A": "Bandung", "B": "Semarang", "C": "Bekasi", "D": "Badung"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Riau?",
                "options": {"A": "Palembang", "B": "Pekanbaru", "C": "Batam", "D": "Padang"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi kalimantan timur?",
                "options": {"A": "Pontianak", "B": "Palangkaraya", "C": "Samarinda", "D": "Banjarmasin"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Jawa Timur?",
                "options": {"A": "Bandung", "B": "Surabaya", "C": "Jakarta", "D": "Semarang"},
                "answer": "B"
            })

            questions.append({
                "question": "Gunung tertinggi di pulau lombok adalah...",
                "options": {"A": "Kerinci", "B": "Rinjani", "C": "Slamet", "D": "Semeru"},
                "answer": "B"
            })

            questions.append({
                "question": "Wilayah Indonesia bagian apa yang letaknya berada di ujung timur Indonesia?",
                "options": {"A": "Sabang", "B": "Merauke", "C": "Jayapura", "D": "Miangas"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Jawa Barat?",
                "options": {"A": "Bandung", "B": "Semarang", "C": "Bekasi", "D": "Badung"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Riau?",
                "options": {"A": "Palembang", "B": "Pekanbaru", "C": "Batam", "D": "Padang"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Kalimantan Timur?",
                "options": {"A": "Pontianak", "B": "Palangkaraya", "C": "Samarinda", "D": "Banjarmasin"},
                "answer": "C"
            })

            questions.append({
                "question": "Gunung tertinggi di Indonesia yang terletak di Provinsi Papua adalah...",
                "options": {"A": "Gunung Kerinci", "B": "Gunung Semeru", "C": "Puncak Jaya", "D": "Gunung Rinjani"},
                "answer": "C"
            })

            questions.append({
                "question": "Laut yang terletak di sebelah utara Pulau Jawa adalah...",
                "options": {"A": "Laut Jawa", "B": "Laut Banda", "C": "Laut Arafuru", "D": "Laut Flores"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Jawa Tengah?",
                "options": {"A": "Surakarta", "B": "Yogyakarta", "C": "Semarang", "D": "Purwokerto"},
                "answer": "C"
            })

            questions.append({
                "question": "Gunung yang terkenal dengan keindahan Danau Toba di sekitarnya adalah...",
                "options": {"A": "Gunung Sinabung", "B": "Gunung Merapi", "C": "Gunung Slamet", "D": "Gunung Agung"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Sulawesi Selatan?",
                "options": {"A": "Manado", "B": "Makassar", "C": "Kendari", "D": "Palu"},
                "answer": "B"
            })

            questions.append({
                "question": "Laut yang berada di antara Pulau Kalimantan dan Pulau Sulawesi adalah...",
                "options": {"A": "Laut Jawa", "B": "Laut Makassar", "C": "Laut Banda", "D": "Laut Sulawesi"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Sumatera Utara?",
                "options": {"A": "Padang", "B": "Medan", "C": "Pekanbaru", "D": "Palembang"},
                "answer": "B"
            })

            questions.append({
                "question": "Gunung tertinggi di Pulau Sumatera adalah...",
                "options": {"A": "Gunung Kerinci", "B": "Gunung Sinabung", "C": "Gunung Dempo", "D": "Gunung Leuser"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Bali?",
                "options": {"A": "Mataram", "B": "Denpasar", "C": "Singaraja", "D": "Kuta"},
                "answer": "B"
            })

            questions.append({
                "question": "Laut yang terletak di sebelah selatan Pulau Nusa Tenggara adalah...",
                "options": {"A": "Laut Jawa", "B": "Laut Banda", "C": "Laut Sawu", "D": "Laut Arafuru"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Nusa Tenggara Barat (NTB)?",
                "options": {"A": "Denpasar", "B": "Kupang", "C": "Mataram", "D": "Bima"},
                "answer": "C"
            })

            questions.append({
                "question": "Gunung yang sering disebut sebagai 'Gunung Api Terbesar di Asia Tenggara' dan terletak di Jawa Timur adalah...",
                "options": {"A": "Gunung Semeru", "B": "Gunung Bromo", "C": "Gunung Kelud", "D": "Gunung Lawu"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Nusa Tenggara Timur (NTT)?",
                "options": {"A": "Kupang", "B": "Mataram", "C": "Ende", "D": "Maumere"},
                "answer": "A"
            })

            questions.append({
                "question": "Laut yang terletak di sebelah timur Pulau Sulawesi dan barat Pulau Maluku adalah...",
                "options": {"A": "Laut Jawa", "B": "Laut Banda", "C": "Laut Arafuru", "D": "Laut Seram"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Kalimantan Selatan?",
                "options": {"A": "Banjarmasin", "B": "Samarinda", "C": "Palangkaraya", "D": "Pontianak"},
                "answer": "A"
            })

            questions.append({
                "question": "Gunung tertinggi di Pulau Kalimantan (wilayah Indonesia) adalah...",
                "options": {"A": "Gunung Bukit Raya", "B": "Gunung Kinabalu", "C": "Gunung Liangpran", "D": "Gunung Nyiut"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Sulawesi Utara?",
                "options": {"A": "Manado", "B": "Gorontalo", "C": "Palu", "D": "Makassar"},
                "answer": "A"
            })

            questions.append({
                "question": "Laut yang berada di ujung selatan Pulau Papua berbatasan dengan Australia adalah...",
                "options": {"A": "Laut Banda", "B": "Laut Seram", "C": "Laut Arafuru", "D": "Laut Timor"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Maluku?",
                "options": {"A": "Ternate", "B": "Ambon", "C": "Sofifi", "D": "Saumlaki"},
                "answer": "B"
            })

            questions.append({
                "question": "Gunung tertinggi di Pulau Sulawesi adalah...",
                "options": {"A": "Gunung Lokon", "B": "Gunung Mahawu", "C": "Gunung Rantemario", "D": "Gunung Klabat"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Papua?",
                "options": {"A": "Jayapura", "B": "Merauke", "C": "Manokwari", "D": "Sorong"},
                "answer": "A"
            })

            questions.append({
                "question": "Laut yang terletak di sebelah barat Pulau Sumatera adalah...",
                "options": {"A": "Laut Jawa", "B": "Samudra Hindia", "C": "Laut Andaman", "D": "Laut Cina Selatan"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Sumatera Barat?",
                "options": {"A": "Bengkulu", "B": "Jambi", "C": "Lampung", "D": "Padang"},
                "answer": "D"
            })

            questions.append({
                "question": "Gunung yang meletus dahsyat pada tahun 1883 dan menimbulkan gelombang tsunami besar adalah...",
                "options": {"A": "Gunung Krakatau", "B": "Gunung Tambora", "C": "Gunung Merapi", "D": "Gunung Kelud"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Kalimantan Tengah?",
                "options": {"A": "Banjarmasin", "B": "Samarinda", "C": "Palangkaraya", "D": "Pontianak"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Sulawesi Tengah?",
                "options": {"A": "Makassar", "B": "Kendari", "C": "Palu", "D": "Gorontalo"},
                "answer": "C"
            })

            questions.append({
                "question": "Laut yang terletak di sebelah utara Pulau Papua adalah...",
                "options": {"A": "Laut Pasifik", "B": "Laut Banda", "C": "Laut Arafuru", "D": "Laut Seram"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Aceh?",
                "options": {"A": "Medan", "B": "Padang", "C": "Banda Aceh", "D": "Sabang"},
                "answer": "C"
            })

            questions.append({
                "question": "Gunung tertinggi di Kepulauan Nusa Tenggara adalah...",
                "options": {"A": "Gunung Agung", "B": "Gunung Rinjani", "C": "Gunung Tambora", "D": "Gunung Egon"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Sumatera Selatan?",
                "options": {"A": "Palembang", "B": "Jambi", "C": "Bengkulu", "D": "Pangkal Pinang"},
                "answer": "A"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Bengkulu?",
                "options": {"A": "Bengkulu", "B": "Curup", "C": "Kepahiang", "D": "Lebong"},
                "answer": "A"
            })

            questions.append({
                "question": "Laut yang terkenal dengan kekayaan baharinya dan terletak di tengah wilayah Indonesia bagian timur adalah...",
                "options": {"A": "Laut Jawa", "B": "Laut Makassar", "C": "Laut Banda", "D": "Laut Flores"},
                "answer": "C"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Lampung?",
                "options": {"A": "Palembang", "B": "Bandar Lampung", "C": "Metro", "D": "Lampung Tengah"},
                "answer": "B"
            })

            questions.append({
                "question": "Gunung yang dianggap suci oleh umat Hindu di Bali dan merupakan gunung tertinggi di pulau tersebut adalah...",
                "options": {"A": "Gunung Batur", "B": "Gunung Agung", "C": "Gunung Rinjani", "D": "Gunung Semeru"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Jambi?",
                "options": {"A": "Sungai Penuh", "B": "Jambi", "C": "Muara Bungo", "D": "Sarolangun"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa ibukota dari provinsi Maluku Utara?",
                "options": {"A": "Ambon", "B": "Sofifi", "C": "Ternate", "D": "Bacan"},
                "answer": "B"
            })

            questions.append({
                "question": "Pulau terluar di ujung Utara Indonesia yang berbatasan dengan Filipina adalah...",
                "options": {"A": "Pulau Rote", "B": "Pulau Sabang", "C": "Pulau Miangas", "D": "Pulau Biak"},
                "answer": "C"
            })
            

        else:
            questions.append({
                "question": "Apa nama kabupaten di ujung timur Pulau Jawa?",
                "options": {"A": "Sumenep", "B": "Banyuwangi", "C": "Surabaya", "D": "Jember"},
                "answer": "B"
            })
            questions.append({
                "question": "Geo Hard: Letak Candi Borobudur?",
                "options": {"A": "Sleman", "B": "Magelang", "C": "Yogyakarta", "D": "Klaten"},
                "answer": "B"
            })
            questions.append({
                "question": "Dimanakah letak candi borobudur?",
                "options": {"A": "Kabupaten Sleman", "B": "Kabupaten Magelang", "C": "Kota Yogyakarta", "D": "Kabupaten Klaten"},
                "answer": "B"
            })

            questions.append({
                "question": "Kabupaten apa yang mengayomi kepulauan karimun jawa?",
                "options": {"A": "Kabupaten Jepara", "B": "Kabupaten Semarang", "C": "Kabupaten Demak", "D": "Kabupaten Karimun"},
                "answer": "A"
            })

            questions.append({
                "question": "Dimanakah letak dari Waduk Gajah Mungkur berada?",
                "options": {"A": "Kabupaten Gunungkidul", "B": "Kabupaten Kebumen", "C": "Kabupaten Pacitan", "D": "Kabupaten Wonogiri"},
                "answer": "D"
            })

            questions.append({
                "question": "Danau Limboto termasuk ke dalam wilayah",
                "options": {"A": "Kabupaten Gorontalo", "B": "Kota Medan", "C": "Kabupaten Bone Bolango", "D": "Kota Makassar"},
                "answer": "A"
            })

            questions.append({
                "question": "(1)Kabupaten Mahakam Ulu (2)Kabupaten Penajam Paser Utara (3)Kota Pontianak (4)Kabupaten Sintang. Dari wilayah wilayah indonesia diatas manakah yang berbatasan langsung dengan negara malaysia?",
                "options": {"A": "1 dan 2", "B": "1 dan 4", "C": "1 dan 3", "D": "3 dan 2"},
                "answer": "B"
            })

            questions.append({
                "question": "Kabupaten apa yang berbatasan dengan provinsi jawa tengah?",
                "options": {"A": "Kabupaten Indramayu", "B": "Kabupaten Subang", "C": "Kabupaten Bandung", "D": "Kabupaten Ciamis"},
                "answer": "D"
            })

            questions.append({
                "question": "(1)Kabupaten Pelalawan (2)Kota Padang (3)Kota Palembang (4)Kota Medan (5)Kabupaten Deli serdang. Dari Wilayah wilayah indonesia diatas manakah yang berbatasan langsung dengan selat malaka?",
                "options": {"A": "1,2,3", "B": "1,3,4", "C": "2,3,4", "D": "1,4,5"},
                "answer": "D"
            })

            questions.append({
                "question": "Manakah kabupaten yang bukan berada dalam provinsi Sulawesi Tengah?",
                "options": {"A": "Banggai", "B": "Poso", "C": "Morowali", "D": "Enrekang"},
                "answer": "D"
            })

            questions.append({
                "question": "Kabupaten apa yang letaknya berada di ujung utara dari provinsi sulawesi utara?",
                "options": {"A": "Kepulauan Talaud", "B": "Pulau Morotai", "C": "Minahasa Utara", "D": "Kepulauan Siau Tagulandang Biaro"},
                "answer": "A"
            })

            questions.append({
                "question": "(1)Kabupaten Purwakarta (2)Kabupaten Cilacap (3)Kabupaten Kuningan (4)Kabupaten Sumedang. Dari daftar wilayah wilayah indonesia di atas manakah yang bukan kabupaten dari provinsi jawa barat?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "answer": "B"
            })

            questions.append({
                "question": "Manakah wilayah di indonesia yang berbatasan dengan selat sunda?",
                "options": {"A": "Kota Serang", "B": "Kota Bandar Lampung", "C": "Kabupaten tangerang", "D": "Kota Cilegon"},
                "answer": "D"
            })

            questions.append({
                "question": "(1)Danau Rawa Pening (2)Danau Ranau (3)Danau Toba (4)Danau Maninjau (5)Danau Singkarak. Dari daftar danau danau di wilayah indonesia di atas, manakah danau yang terletak di pulau jawa?",
                "options": {"A": "1", "B": "2,4 dan 5", "C": "3", "D": "Tidak ada"},
                "answer": "A"
            })

            questions.append({
                "question": "Pura Tanah Lot termasuk dalam wilayah?",
                "options": {"A": "Tabanan", "B": "Denpasar", "C": "Buleleng", "D": "Badung"},
                "answer": "A"
            })

            questions.append({
                "question": "(1)Kabupaten Wonosobo (2)Kabupaten Banjarnegara (3)Kabupaten Pekalongan (4)Kabupaten Wonogiri. Dari Daftar wilayah wilayah diatas manakah yang jaraknya paling jauh ke dataran tinggi dieng?",
                "options": {"A": "2", "B": "1", "C": "4", "D": "3"},
                "answer": "C"
            })

            questions.append({
                "question": "Manakah wilayah yang paling jauh dari Kota Palembang?",
                "options": {"A": "Kabupaten Ogan ilir", "B": "Kabupaten Musi Rawas", "C": "Kabupaten Penukal Abab Lematang Ilir", "D": "Kota Prabumulih"},
                "answer": "B"
            })

            questions.append({
                "question": "Manakah Wilayah yang paling dekat dari Gunung Rinjani?",
                "options": {"A": "Kabupaten Bogor", "B": "Kabupaten Sumbawa Barat", "C": "Kabupaten Lombok Timur", "D": "Kota Mataram"},
                "answer": "C"
            })

            questions.append({
                "question": "Manakah Kabupaten yang bukan berada di dalam provinsi Banten?",
                "options": {"A": "Kota Tangerang", "B": "Kabupaten Pandeglang", "C": "Kabupaten Lebak", "D": "Kabupaten Ketapang"},
                "answer": "D"
            })

            questions.append({
                "question": "Manakah Kabupaten yang berada di dalam provinsi Jawa Timur?",
                "options": {"A": "Kabupaten Sampang", "B": "Kabupaten Karangasem", "C": "Kabupaten Rembang", "D": "Kabupaten Gunung Mas"},
                "answer": "A"
            })

            questions.append({
                "question": "Manakah wilayah di indonesia yang menyentuh selat makassar?",
                "options": {"A": "Kabupaten Sinjai", "B": "Kota Banjarbaru", "C": "Kabupaten Paser", "D": "Kota Palopo"},
                "answer": "C"
            })

            questions.append({
                "question": "(1)Kabupaten Semarang (2)Kabupaten Grobogan (3)Kabupaten Boyolali (4)Kota Salatiga. Dari daftar wilayah di indonesia di atas manakah yang letaknya paling timur dari 4 teritori tersebut?",
                "options": {"A": "4", "B": "3", "C": "2", "D": "1"},
                "answer": "C"
            })

            questions.append({
                "question": "(1)Kabupaten Sukabumi (2)Kabupaten Bogor (3)Kabupaten Cianjur (4)Kabupaten Bandung (5)Kabupaten Garut (6)Kabupaten Tasikmalaya. Dari Daftar wilayah di indonesia di atas manakah yang berbatasan dengan laut selatan?",
                "options": {"A": "1,3,5,6", "B": "2,3,4,5", "C": "1,2,3,4", "D": "1,2,5,6"},
                "answer": "A"
            })

            questions.append({
                "question": "Manakah wilayah yang termasuk dalam Provinsi Sumatera Barat?",
                "options": {"A": "Kabupaten Mukomuko", "B": "Kabupaten Indragiri Hulu", "C": "Kabupaten Mandailing Natal", "D": "Kabupaten Sijunjung"},
                "answer": "D"
            })

            questions.append({
                "question": "Apa nama wilayah yang berbatasan dengan sisi utara kabupaten Blora?",
                "options": {"A": "Kabupaten Jepara", "B": "Kabupaten Rembang", "C": "Kabupaten Kudus", "D": "Kabupaten Ngawi"},
                "answer": "B"
            })

            questions.append({
                "question": "Apa nama wilayah yang berbatasan dengan sisi barat Kota Surabaya?",
                "options": {"A": "Kabupaten Mojokerto", "B": "Kabupaten Sidoarjo", "C": "Kabupaten Madiun", "D": "Kabupaten Malang"},
                "answer": "A"
            })

            questions.append({
                "question": "Manakah wilayah yang termasuk dalam provinsi Bali?",
                "options": {"A": "Kabupaten Karangasem", "B": "Kota Mataram", "C": "Kabupaten Balangan", "D": "Kabupaten Situbondo"},
                "answer": "A"
            })

            questions.append({
                "question": "(1)Kota Banda Aceh (2)Kota Banjar (3)Kota Kotamobagu. Dari daftar wilayah diatas manakah wilayah yang letaknya di Pulau Kalimantan?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "Tidak ada"},
                "answer": "D"
            })

            questions.append({
                "question": "(1)Kabupaten Gayo Lues berbatasan dengan Kabupaten Nagan Raya (2)Kota Subulussalam Berbatasan dengan Kabupaten Aceh Singkil (3)Kabupaten Langkat berbatasan dengan Kabupaten Aceh Tamiang. Dari Pernyataan di atas ,manakah pernyataan yang benar?",
                "options": {"A": "1 dan 2", "B": "2 dan 3", "C": "Semua Benar", "D": "Tidak ada"},
                "answer": "C"
            })

            questions.append({
                "question": "(1)Berbatasan dengan kabupaten Cilacap (2)Berada di selatan provinsi jawa tengah (3)tidak memiliki pantai (4)Dilewati sungai bengawan solo. Apa salah satu ciri ciri yang tepat yang bukan menggambarkan kabupaten brebes, kecuali?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "answer": "A"
            })

            questions.append({
                "question": "Berikut ini wilayah yang memiliki teritori bernama “Kabupaten Alor” berada dalam provinsi?",
                "options": {"A": "Papua Selatan", "B": "NTT", "C": "Maluku Utara", "D": "Maluku"},
                "answer": "B"
            })

            questions.append({
                "question": "(1)Berbatasan dengan laut jawa (2)Berbatasan dengan provinsi kalimantan tengah. Apa nama wilayah yang tepat dari ciri ciri diatas?",
                "options": {"A": "Kabupaten Kotawaringin barat", "B": "Kota Banjarmasin", "C": "Kabupaten Kotawaringin Timur", "D": "Kabupaten Barito Kuala"},
                "answer": "D"
            })

            questions.append({
                "question": "(1)Kabupaten Sumba Barat Daya berada di pulau sumba (2)Taman Nasional Komodo berada di kabupaten Manggarai Barat (3)Kabupaten Dompu berada di provinsi NTT. Dari pernyataan pernyataan di atas, manakah pernyataan yang salah?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "Semua salah"},
                "answer": "C"
            })

            questions.append({
                "question": "(1)Kabupaten Temanggung (2)Kabupaten Wonosobo (3)Kabupaten Banjarnegara (4)Kabupaten Banyumas. Dari daftar daftar diatas, urutkan dari wilayah yang terjauh hingga terdekat untuk menuju ibukota jawa tengah?",
                "options": {"A": "4,2,1,3", "B": "2,1,4,3", "C": "4,3,2,1", "D": "1,2,3,4"},
                "answer": "C"
            })

            questions.append({
                "question": "(1)Kota Pangkalpinang (2)Kota Pagar Alam (3)Kabupaten Sukamara (4)Kabupaten Bengkayang. Dari Daftar daftar diatas, manakah wilayah yang lebih dekat ke Negara Malaysia?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "answer": "D"
            })

            questions.append({
                "question": "Manakah kabupaten yang saling berbatasan?",
                "options": {"A": "Kabupaten Tapin–Kabupaten Hulu Sungai Selatan", "B": "Kabupaten Magelang–Kabupaten Gunung Mas", "C": "Kabupaten Garut–Kabupaten Sukabumi", "D": "Kabupaten Aceh Barat–Kabupaten Aceh Barat Daya"},
                "answer": "A"
            })

            questions.append({
                "question": "(1)Kabupaten Pesisir Barat (2)Kabupaten Pesisir Selatan (3)Kabupaten Nunukan (4)Kabupaten Banyuwangi. Manakah wilayah yang lebih dekat ke provinsi DKI Jakarta?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "answer": "A"
            })

            questions.append({
                "question": "Pulau Tinjil berada di dalam wilayah?",
                "options": {"A": "Kabupaten Banggai Kepulauan", "B": "Kabupaten Karimun", "C": "Kabupaten Polewali Mandar", "D": "Kabupaten Pandeglang"},
                "answer": "D"
            })

            questions.append({
                "question": "Manakah Kabupaten yang berbatasan dengan Kota?",
                "options": {"A": "Kabupaten Tanggamus", "B": "Kabupaten Tulang Bawang", "C": "Kabupaten Bojonegoro", "D": "Kabupaten Kuningan"},
                "answer": "D"
            })

            questions.append({
                "question": "Manakah wilayah yang termasuk ke dalam provinsi Riau?",
                "options": {"A": "Kabupaten Labuhan Batu Selatan", "B": "Kabupaten Lima Puluh Kota", "C": "Kabupaten Tebo", "D": "Kabupaten Rokan Hilir"},
                "answer": "D"
            })

            questions.append({
                "question": "Manakah Wilayah yang termasuk ke dalam provinsi Jawa Tengah?",
                "options": {"A": "Kabupaten Probolinggo", "B": "Kabupaten Purbalingga", "C": "Kabupaten Bojonegoro", "D": "Kabupaten Batang"},
                "answer": "B"
            })

            questions.append({
                "question": "(1)Kabupaten Lembata (2)Kota Kupang (3)Kabupaten Pangandaran (4)Kabupaten Landak. Manakah wilayah yang lebih dekat ke ibukota Provinsi Jawa Timur?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "answer": "C"
            })

            questions.append({
                "question": "Manakah Wilayah yang termasuk ke dalam provinsi Jawa Barat, kecuali?",
                "options": {"A": "Kabupaten Cilacap", "B": "Kabupaten Ciamis", "C": "Kabupaten Cianjur", "D": "Kabupaten Cirebon"},
                "answer": "A"
            })

            questions.append({
                "question": "Manakah wilayah dengan jarak Terjauh ke ibukota provinsi Banten?",
                "options": {"A": "Kabupaten Pamekasan", "B": "Kota Denpasar", "C": "Kabupaten Bulukumba", "D": "Kabupaten Serang"},
                "answer": "C"
            })

            questions.append({
                "question": "Manakah Wilayah Dengan Jarak Terdekat ke Ibukota Provinsi DIY (daerah istimewa yogyakarta)?",
                "options": {"A": "Kabupaten Sukamara", "B": "Kabupaten Gunung Mas", "C": "Kabupaten Wajo", "D": "Kabupaten Tuban"},
                "answer": "D"
            })

            questions.append({
                "question": "Manakah Wilayah Dengan Jarak Terjauh dari Ibukota Provinsi Sumatera Utara?",
                "options": {"A": "Kabupaten Sijunjung", "B": "Kabupaten Rokan Hilir", "C": "Kabupaten Karo", "D": "Kabupaten Simalungun"},
                "answer": "A"
            })

            questions.append({
                "question": "Manakah Wilayah Dengan Jarak Terjauh dari Kota Surakarta?",
                "options": {"A": "Kota Surabaya", "B": "Kabupaten Boyolali", "C": "Kabupaten Kulon Progo", "D": "Kota Pekalongan"},
                "answer": "A"
            })

            questions.append({
                "question": "Manakah Wilayah dengan jarak terdekat dari Kota Malang?",
                "options": {"A": "Kabupaten Situbondo", "B": "Kabupaten Sragen", "C": "Kota Surakarta", "D": "Kabupaten Pacitan"},
                "answer": "A"
            })

            questions.append({
                "question": "Manakah Wilayah dengan jarak terjauh dari Kota Surakarta?",
                "options": {"A": "Kabupaten Boyolali", "B": "Kabupaten Tegal", "C": "Kabupaten Bangka Tengah", "D": "Kabupaten Sigi"},
                "answer": "D"
            })

            questions.append({
                "question": "Berapa total jumlah kabupaten dan kota yang ada di Negara Indonesia?",
                "options": {"A": "493 Kabupaten/Kota", "B": "497 Kabupaten/Kota", "C": "505 Kabupaten/Kota", "D": "514 Kabupaten/Kota"},
                "answer": "D"
            })

    else:  # Inggris
        if level == 1:
            questions.append({
                "question": "“Good morning” is used in the …",
                "options": {"A": "afternoon", "B": "evening", "C": "morning", "D": "night"},
                "answer": "C"
            })
            questions.append({
                "question": "A: Hello!\nB: ______",
                "options": {"A": "Goodbye", "B": "Hi!", "C": "Thank you", "D": "Sorry"},
                "answer": "B"
            })
            questions.append({
                "question": "I ______ a student.",
                "options": {"A": "is", "B": "am", "C": "are", "D": "be"},
                "answer": "B"
            })
            questions.append({
                "question": "She ______ my friend.",
                "options": {"A": "is", "B": "am", "C": "are", "D": "be"},
                "answer": "A"
            })
            questions.append({
                "question": "They ______ students.",
                "options": {"A": "is", "B": "am", "C": "are", "D": "be"},
                "answer": "C"
            })
            questions.append({
                "question": "I go to school ______ Monday.",
                "options": {"A": "in", "B": "on", "C": "at", "D": "by"},
                "answer": "B"
            })
            questions.append({
                "question": "We ______ English every day.",
                "options": {"A": "study", "B": "studies", "C": "studying", "D": "studied"},
                "answer": "A"
            })
            questions.append({
                "question": "She ______ milk.",
                "options": {"A": "like", "B": "likes", "C": "liking", "D": "liked"},
                "answer": "B"
            })
            questions.append({
                "question": "The opposite of “big” is …",
                "options": {"A": "tall", "B": "small", "C": "long", "D": "fast"},
                "answer": "B"
            })
            questions.append({
                "question": "My mother works in a hospital. She is a …",
                "options": {"A": "teacher", "B": "doctor", "C": "farmer", "D": "driver"},
                "answer": "B"
            })
            questions.append({
                "question": "I have ______ cat.",
                "options": {"A": "a", "B": "an", "C": "the", "D": "some"},
                "answer": "A"
            })
            questions.append({
                "question": "There ______ one book on the table.",
                "options": {"A": "is", "B": "are", "C": "am", "D": "be"},
                "answer": "A"
            })
            questions.append({
                "question": "We ______ playing football now.",
                "options": {"A": "is", "B": "am", "C": "are", "D": "be"},
                "answer": "C"
            })
            questions.append({
                "question": "Yesterday, I ______ to school.",
                "options": {"A": "go", "B": "goes", "C": "went", "D": "going"},
                "answer": "C"
            })
            questions.append({
                "question": "The synonym of “happy” is …",
                "options": {"A": "sad", "B": "angry", "C": "glad", "D": "tired"},
                "answer": "C"
            })
            questions.append({
                "question": "“Thank you” is used to express …",
                "options": {"A": "apology", "B": "greeting", "C": "gratitude", "D": "command"},
                "answer": "C"
            })
            questions.append({
                "question": "She is ______ than me.",
                "options": {"A": "tall", "B": "taller", "C": "tallest", "D": "more tall"},
                "answer": "B"
            })
            questions.append({
                "question": "I will ______ my homework tonight.",
                "options": {"A": "do", "B": "does", "C": "did", "D": "doing"},
                "answer": "A"
            })
            questions.append({
                "question": "______ you like ice cream?",
                "options": {"A": "Do", "B": "Does", "C": "Are", "D": "Is"},
                "answer": "A"
            })
            questions.append({
                "question": "My father ______ a car.",
                "options": {"A": "have", "B": "has", "C": "having", "D": "had"},
                "answer": "B"
            })
            questions.append({
                "question": "The correct negative form of “I like tea” is …",
                "options": {"A": "I not like tea", "B": "I don’t like tea", "C": "I doesn’t like tea", "D": "I didn’t like tea"},
                "answer": "B"
            })
            questions.append({
                "question": "“Close the door!” is a …",
                "options": {"A": "question", "B": "command", "C": "greeting", "D": "apology"},
                "answer": "B"
            })
            questions.append({
                "question": "She is reading ______ book.",
                "options": {"A": "a", "B": "an", "C": "the", "D": "some"},
                "answer": "A"
            })
            questions.append({
                "question": "We live ______ Indonesia.",
                "options": {"A": "in", "B": "on", "C": "at", "D": "by"},
                "answer": "A"
            })
            questions.append({
                "question": "“See you tomorrow” means …",
                "options": {"A": "Goodbye", "B": "Hello", "C": "Thank you", "D": "Sorry"},
                "answer": "A"
            })
            questions.append({
                "question": "She ___ to school every day.",
                "options": {"A": "go", "B": "goes", "C": "going", "D": "gone"},
                "answer": "B"
            })

            questions.append({
                "question": "They ___ playing football now.",
                "options": {"A": "is", "B": "am", "C": "are", "D": "be"},
                "answer": "C"
            })

            questions.append({
                "question": "My father ___ a car.",
                "options": {"A": "have", "B": "has", "C": "having", "D": "had"},
                "answer": "B"
            })

            questions.append({
                "question": "I ___ not like spicy food.",
                "options": {"A": "do", "B": "does", "C": "am", "D": "is"},
                "answer": "A"
            })

            questions.append({
                "question": "We ___ English on Monday.",
                "options": {"A": "has", "B": "have", "C": "having", "D": "had"},
                "answer": "B"
            })

            questions.append({
                "question": "___ you like milk?",
                "options": {"A": "Do", "B": "Does", "C": "Is", "D": "Are"},
                "answer": "A"
            })

            questions.append({
                "question": "There ___ a book on the table.",
                "options": {"A": "are", "B": "am", "C": "is", "D": "be"},
                "answer": "C"
            })

            questions.append({
                "question": "She is ___ than her sister.",
                "options": {"A": "tall", "B": "taller", "C": "tallest", "D": "more tall"},
                "answer": "B"
            })

            questions.append({
                "question": "I was born ___ 2010.",
                "options": {"A": "in", "B": "on", "C": "at", "D": "by"},
                "answer": "A"
            })

            questions.append({
                "question": "They ___ TV when I arrived.",
                "options": {"A": "watch", "B": "watches", "C": "were watching", "D": "watched"},
                "answer": "C"
            })

            questions.append({
                "question": "She ___ to the market yesterday.",
                "options": {"A": "go", "B": "goes", "C": "went", "D": "going"},
                "answer": "C"
            })

            questions.append({
                "question": "We ___ studying English right now.",
                "options": {"A": "is", "B": "am", "C": "are", "D": "be"},
                "answer": "C"
            })

            questions.append({
                "question": "This is ___ book.",
                "options": {"A": "I", "B": "me", "C": "my", "D": "mine"},
                "answer": "C"
            })

            questions.append({
                "question": "He can ___ very fast.",
                "options": {"A": "runs", "B": "run", "C": "running", "D": "ran"},
                "answer": "B"
            })

            questions.append({
                "question": "There are many ___ in the classroom.",
                "options": {"A": "student", "B": "students", "C": "student’s", "D": "students’"},
                "answer": "B"
            })

            questions.append({
                "question": "She ___ breakfast at 7 a.m.",
                "options": {"A": "eat", "B": "eats", "C": "eating", "D": "ate"},
                "answer": "B"
            })

            questions.append({
                "question": "The cat is ___ the table.",
                "options": {"A": "in", "B": "on", "C": "at", "D": "under"},
                "answer": "D"
            })

            questions.append({
                "question": "I ___ very happy today.",
                "options": {"A": "am", "B": "is", "C": "are", "D": "be"},
                "answer": "A"
            })

            questions.append({
                "question": "They ___ to Bali last holiday.",
                "options": {"A": "go", "B": "goes", "C": "went", "D": "going"},
                "answer": "C"
            })

            questions.append({
                "question": "___ she your sister?",
                "options": {"A": "Do", "B": "Does", "C": "Is", "D": "Are"},
                "answer": "C"
            })

            questions.append({
                "question": "This movie is ___ than that one.",
                "options": {"A": "interesting", "B": "more interesting", "C": "most interesting", "D": "interest"},
                "answer": "B"
            })

            questions.append({
                "question": "We usually ___ to school by bus.",
                "options": {"A": "go", "B": "goes", "C": "went", "D": "going"},
                "answer": "A"
            })

            questions.append({
                "question": "He ___ playing guitar now.",
                "options": {"A": "is", "B": "are", "C": "am", "D": "be"},
                "answer": "A"
            })

            questions.append({
                "question": "There ___ two apples on the table.",
                "options": {"A": "is", "B": "are", "C": "am", "D": "be"},
                "answer": "B"
            })

            questions.append({
                "question": "She doesn’t ___ coffee.",
                "options": {"A": "likes", "B": "like", "C": "liking", "D": "liked"},
                "answer": "B"
            })
            
        elif level == 2:
            questions.append({
                "question": "The correct response to “How do you do?” is …",
                "options": {"A": "I’m fine", "B": "How do you do?", "C": "Nice to meet you", "D": "Good morning"},
                "answer": "B"
                })
            questions.append({
                "question": "She __ to school by bus every day.",
                "options": {"A": "go", "B": "goes", "C": "going", "D": "went"},
                "answer": "B"
                })
            questions.append({
                "question": "They __ studying when I arrived.",
                "options": {"A": "is", "B": "are", "C": "were", "D": "was"},
                "answer": "C"
                })
            questions.append({
                "question": "The comparative form of “beautiful” is …",
                "options": {"A": "beautifuller", "B": "more beautiful", "C": "most beautiful", "D": "beautifulest"},
                "answer": "B"
                })
            questions.append({
                "question": "If I have enough money, I __ buy a new phone.",
                "options": {"A": "will", "B": "would", "C": "am", "D": "did"},
                "answer": "A"
                })
            questions.append({
                "question": "My brother is interested __ music.",
                "options": {"A": "on", "B": "at", "C": "in", "D": "with"},
                "answer": "C"
                })
            questions.append({
                "question": "The antonym of “polite” is …",
                "options": {"A": "kind", "B": "rude", "C": "honest", "D": "friendly"},
                "answer": "B"
                })
            questions.append({
                "question": "“Would you like some tea?” The sentence expresses …",
                "options": {"A": "Suggestion", "B": "Offering", "C": "Command", "D": "Opinion"},
                "answer": "B"
                })
            questions.append({
                "question": "There __ many students in the classroom.",
                "options": {"A": "is", "B": "was", "C": "are", "D": "has"},
                "answer": "C"
                })
            questions.append({
                "question": "The correct passive form of “They clean the room” is …",
                "options": {"A": "The room cleans them", "B": "The room is cleaned by them", "C": "The room cleaned by them", "D": "The room was cleaned them"},
                "answer": "B"
                })
            questions.append({
                "question": "We have lived here __ 2020.",
                "options": {"A": "since", "B": "for", "C": "from", "D": "at"},
                "answer": "A"
                })
            questions.append({
                "question": "I was tired, __ I went to bed early.",
                "options": {"A": "because", "B": "but", "C": "so", "D": "although"},
                "answer": "C"
                }) 
            questions.append({
                "question": "She speaks English __ than her sister.",
                "options": {"A": "fluent", "B": "more fluent", "C": "most fluent", "D": "fluently"},
                "answer": "B"
                })
            questions.append({
                "question": "He asked me where I __ from.",
                "options": {"A": "am", "B": "was", "C": "were", "D": "be"},
                "answer": "B"
                })
            questions.append({
                "question": "The correct question form is …",
                "options": {"A": "Where you are going?", "B": "Where are you going?", "C": "Where you going are?", "D": "You are going where?"},
                "answer": "B"
                })
            questions.append({
                "question": "My father doesn’t allow me __ out at night.",
                "options": {"A": "go", "B": "to go", "C": "going", "D": "went"},
                "answer": "B"
                })
            questions.append({
                "question": "She has finished her homework, __?",
                "options": {"A": "hasn’t she", "B": "has she", "C": "doesn’t she", "D": "didn’t she"},
                "answer": "A"
                })
            questions.append({
                "question": "The synonym of “begin” is …",
                "options": {"A": "end", "B": "stop", "C": "start", "D": "close"},
                "answer": "C"
                })
            questions.append({
                "question": "I am looking forward to __ you soon.",
                "options": {"A": "see", "B": "seeing", "C": "saw", "D": "seen"},
                "answer": "B"
                })
            questions.append({
                "question": "The correct sentence is …",
                "options": {"A": "He don’t like coffee", "B": "He doesn’t likes coffee", "C": "He doesn’t like coffee", "D": "He not like coffee"},
                "answer": "C"
                }) 
            questions.append({
                "question": "We have lived here __ 1945.",
                "options": {"A": "since", "B": "for", "C": "from", "D": "at"},
                "answer": "A"
                })
            questions.append({
                "question": "We were watching TV when the lights __ off.",
                "options": {"A": "go", "B": "goes", "C": "went", "D": "going"},
                "answer": "C"
                })
            questions.append({
                "question": "The superlative form of “far” is …",
                "options": {"A": "farther", "B": "farthest", "C": "more far", "D": "most far"},
                "answer": "B"
                })
            questions.append({
                "question": "She bought __ umbrella because it was raining.",
                "options": {"A": "a", "B": "an", "C": "the", "D": "some"},
                "answer": "B"
                })
            questions.append({
                "question": "“You should study harder.” The sentence expresses …",
                "options": {"A": "Obligation", "B": "Suggestion", "C": "Permission", "D": "Apology"},
                "answer": "B"
                })
            questions.append({
                "question": "She ____ to the library every Saturday.",
                "options": {"A": "go", "B": "goes", "C": "went", "D": "going"},
                "answer": "B"
                })
            questions.append({
                "question": "If I ____ rich, I would travel around the world.",
                "options": {"A": "am", "B": "was", "C": "were", "D": "be"},
                "answer": "C"
                })
            questions.append({
                "question": "The homework ____ by the students yesterday.",
                "options": {"A": "is done", "B": "was done", "C": "were done", "D": "did"},
                "answer": "B"
                })
            questions.append({
                "question": "They have studied English ____ three years.",
                "options": {"A": "since", "B": "for", "C": "from", "D": "at"},
                "answer": "B"
                })
            questions.append({
                "question": "This problem is ____ than the previous one.",
                "options": {"A": "difficult", "B": "more difficult", "C": "most difficult", "D": "difficultly"},
                "answer": "B"
                })
            questions.append({
                "question": "While I ____ my homework, my sister was watching TV.",
                "options": {"A": "do", "B": "did", "C": "was doing", "D": "am doing"},
                "answer": "C"
                })
            questions.append({
                "question": "She sings very ____.",
                "options": {"A": "beautiful", "B": "beautifully", "C": "beauty", "D": "more beautiful"},
                "answer": "B"
                })
            questions.append({
                "question": "There aren't ____ chairs in the room.",
                "options": {"A": "much", "B": "many", "C": "little", "D": "a little"},
                "answer": "B"
                })
            questions.append({
                "question": "He asked me where I ____ the book.",
                "options": {"A": "buy", "B": "bought", "C": "buying", "D": "buys"},
                "answer": "B"
                })
            questions.append({
                "question": "The man ____ is wearing a blue jacket is my uncle.",
                "options": {"A": "who", "B": "which", "C": "where", "D": "whose"},
                "answer": "A"
                })
            questions.append({
                "question": "If it rains, we ____ at home.",
                "options": {"A": "stay", "B": "stayed", "C": "will stay", "D": "staying"},
                "answer": "C"
                })
            questions.append({
                "question": "My sister is interested ____ painting.",
                "options": {"A": "in", "B": "on", "C": "at", "D": "with"},
                "answer": "A"
                })
            questions.append({
                "question": "The movie was so ____ that everyone cried.",
                "options": {"A": "sad", "B": "sadly", "C": "sadness", "D": "saddest"},
                "answer": "A"
                })
            questions.append({
                "question": "I have never ____ to Singapore.",
                "options": {"A": "go", "B": "went", "C": "gone", "D": "going"},
                "answer": "C"
                })
            questions.append({
                "question": "He is the ____ student in the class.",
                "options": {"A": "smart", "B": "smarter", "C": "smartest", "D": "more smart"},
                "answer": "C"
                })
            questions.append({
                "question": "The word 'unforgettable' means ____.",
                "options": {"A": "Easy to forget", "B": "Hard to remember", "C": "Impossible to forget", "D": "Boring"},
                "answer": "C"
                })
            questions.append({
                "question": "She ____ finished her project before the deadline.",
                "options": {"A": "have", "B": "has", "C": "had", "D": "having"},
                "answer": "C"
                })
            questions.append({
                "question": "There ____ a lot of water in the bottle.",
                "options": {"A": "are", "B": "were", "C": "is", "D": "be"},
                "answer": "C"
                })
            questions.append({
                "question": "He runs ____ than me.",
                "options": {"A": "fast", "B": "faster", "C": "fastest", "D": "more fast"},
                "answer": "B"
                })
            questions.append({
                "question": "The teacher told us ____ quiet.",
                "options": {"A": "be", "B": "to be", "C": "being", "D": "been"},
                "answer": "B"
                })
            questions.append({
                "question": "If she studies hard, she ____ pass the exam.",
                "options": {"A": "will", "B": "would", "C": "can", "D": "could"},
                "answer": "A"
                })
            questions.append({
                "question": "The sun ____ in the east.",
                "options": {"A": "rise", "B": "rises", "C": "rose", "D": "rising"},
                "answer": "B"
                })
            questions.append({
                "question": "An antonym of 'expensive' is ____.",
                "options": {"A": "cheap", "B": "high", "C": "costly", "D": "price"},
                "answer": "A"
                })
            questions.append({
                "question": "I have been studying English ____ three years.",
                "options": {"A": "since", "B": "for", "C": "from", "D": "at"},
                "answer": "B"
                })
            questions.append({
                "question": "She enjoys ____ novels in her free time.",
                "options": {"A": "read", "B": "to read", "C": "reading", "D": "reads"},
                "answer": "C"
                })
        else: #Level 3
            questions.append({
                "question": "'She has gone' adalah tense?",
                "options": {"A": "Simple Past", "B": "Present Continuous", "C": "Present Perfect", "D": "Future"},
                "answer": "C"
            })
            questions.append({
                "question": "The committee _______ revisions to the draft before it was ultimately submitted for approval.",
                "options": {"A": "had the legal advisor made", "B": "got the legal advisor make", "C": "had the legal advisor to make", "D": "made the legal advisor"},
                "answer": "A"
            })
            questions.append({
                "question": "By the time the rescue team arrived, the injured hiker _______ by a group of experienced climbers.",
                "options": {"A": "has already been evacuated", "B": "was already evacuated", "C": "had already been evacuated", "D": "was already being evacuated"},
                "answer": "C"
            })
            questions.append({
                "question": "The ancient artifact _______ to have originated from the pre-Columbian era, though some experts remain skeptical.",
                "options": {"A": "is believed", "B": "believes", "C": "is believing", "D": "has believed"},
                "answer": "A"
            })
            questions.append({
                "question": "Should more stringent regulations _______ next fiscal year, companies will need to adjust their compliance strategies.",
                "options": {"A": "be enacted", "B": "are enacted", "C": "have enacted", "D": "enact"},
                "answer": "A"
            })
            questions.append({
                "question": "The CEO insisted that the confidential report _______ to any external parties under any circumstances.",
                "options": {"A": "must not be disclosed", "B": "not be disclosed", "C": "be not disclosed", "D": "is not disclosed"},
                "answer": "B"
            })
            questions.append({
                "question": "This unique painting technique, _______ by Italian masters of the 16th century, fell into obscurity for nearly three hundred years.",
                "options": {"A": "being perfected", "B": "perfected", "C": "having perfected", "D": "was perfected"},
                "answer": "B"
            })
            questions.append({
                "question": "Rather than _______ the blame for the security breach, the manager chose to conduct an internal investigation.",
                "options": {"A": "being assigned", "B": "be assigned", "C": "having assigned", "D": "assigning"},
                "answer": "D"
            })
            questions.append({
                "question": "It is imperative that the origin of the contaminated samples _______ before the health inspection deadline.",
                "options": {"A": "trace", "B": "be traced", "C": "is traced", "D": "will be traced"},
                "answer": "B"
            })
            questions.append({
                "question": "The laboratory equipment, _______ meticulously for decades, is still considered state-of-the-art.",
                "options": {"A": "having been maintained", "B": "maintained", "C": "being maintained", "D": "to have maintained"},
                "answer": "B"
            })
            questions.append({
                "question": "The diplomat's statements were deliberately ambiguous, but they _______ as a tacit admission of failure.",
                "options": {"A": "were widely interpreted", "B": "widely interpreted", "C": "were widely interpreting", "D": "had widely interpreted"},
                "answer": "A"
            })
            questions.append({
                "question": "While the auditorium _______ for the commencement ceremony, the faculty met in a separate chamber.",
                "options": {"A": "was being prepared", "B": "was prepared", "C": "being prepared", "D": "prepared"},
                "answer": "A"
            })
            questions.append({
                "question": "The new encryption protocol is designed to ensure that sensitive user data _______ even in the event of a server breach.",
                "options": {"A": "does not compromise", "B": "is not compromised", "C": "be not compromised", "D": "will not compromise"},
                "answer": "B"
            })
            questions.append({
                "question": "Never before _______ such a flagrant disregard for the established diplomatic protocols.",
                "options": {"A": "has shown by the ambassador", "B": "has it been shown by the ambassador", "C": "has the ambassador shown", "D": "has been the ambassador shown"},
                "answer": "C"
            })
            questions.append({
                "question": "The board of directors recommended that the merger _______ until a more thorough financial audit could be conducted.",
                "options": {"A": "be postponed", "B": "is postponed", "C": "will be postponed", "D": "postpones"},
                "answer": "A"
            })
            questions.append({
                "question": "The candidate's reputation, _______ by years of public service, was irreparably damaged by a single unsubstantiated allegation.",
                "options": {"A": "having been built", "B": "being built", "C": "building", "D": "to build"},
                "answer": "A"
            })
            questions.append({
                "question": "Far from _______ by the criticism, the artist found it to be an affirmation of her work's impact.",
                "options": {"A": "being discouraged", "B": "having discouraged", "C": "discouraging", "D": "be discouraged"},
                "answer": "A"
            })
            questions.append({
                "question": "Only after the treaty was ratified _______ the full extent of the economic concessions.",
                "options": {"A": "the public did realize", "B": "realized the public", "C": "did the public realize", "D": "was the public realized"},
                "answer": "C"
            })
            questions.append({
                "question": "The manuscript was so densely annotated by its previous owner that the original text _______ beneath the marginalia.",
                "options": {"A": "could barely be discerned", "B": "could barely discern", "C": "could be barely discerned", "D": "could discern barely"},
                "answer": "A"
            })
            questions.append({
                "question": "The proposal, which _______ for months, was finally rejected due to lack of funding.",
                "options": {"A": "had been deliberated on", "B": "had deliberated on", "C": "was deliberated", "D": "had been deliberated"},
                "answer": "A"
            })
            questions.append({
                "question": "Should the device _______ to be defective, consumers are entitled to a full refund under the warranty.",
                "options": {"A": "finds", "B": "be found", "C": "is found", "D": "found"},
                "answer": "B"
            })
            questions.append({
                "question": "The intricate carvings on the cathedral doors are thought _______ by an anonymous Flemish artisan.",
                "options": {"A": "to create", "B": "to have been created", "C": "to be creating", "D": "to have created"},
                "answer": "B"
            })
            questions.append({
                "question": "This rare genetic mutation, _______ in only a few isolated populations, confers resistance to certain pathogens.",
                "options": {"A": "documenting", "B": "documented", "C": "being documented", "D": "having documented"},
                "answer": "B"
            })
            questions.append({
                "question": "Not until the final quarter of the fiscal year _______ to address the glaring inefficiencies in the supply chain.",
                "options": {"A": "did any serious attempt make", "B": "was any serious attempt made", "C": "any serious attempt was made", "D": "made any serious attempt"},
                "answer": "B"
            })
            questions.append({
                "question": "The terms of the contract were so vaguely worded that they _______ to multiple interpretations.",
                "options": {"A": "were susceptible", "B": "were susceptible of being", "C": "were susceptible for being", "D": "susceptible"},
                "answer": "A"
            })
            questions.append({
                "question": "_______ for his controversial policies, the former prime minister remains a highly influential figure in political theory.",
                "options": {"A": "While widely criticized", "B": "Widely criticized", "C": "Having widely criticized", "D": "While being widely criticized"},
                "answer": "A"
            })
            questions.append({
                "question": "The CEO’s memoirs, ghostwritten by a prominent journalist, _______ as a frank account of corporate intrigue.",
                "options": {"A": "are long being regarded", "B": "have long regarded", "C": "have long been regarded", "D": "are long regarded"},
                "answer": "C"
            })
            questions.append({
                "question": "Had the dam _______ prior to the monsoon season, the devastation downstream could have been mitigated.",
                "options": {"A": "been reinforced", "B": "reinforced", "C": "being reinforced", "D": "have been reinforced"},
                "answer": "A"
            })
            questions.append({
                "question": "The defendant’s alibi was initially corroborated, but it later _______ by several witnesses.",
                "options": {"A": "was contradicted", "B": "contradicted", "C": "has contradicted", "D": "were contradicted"},
                "answer": "A"
            })
            questions.append({
                "question": "The software’s architecture is so arcane that any further modifications _______ only with extreme caution.",
                "options": {"A": "ought to make", "B": "ought to be made", "C": "ought be made", "D": "are ought to be made"},
                "answer": "B"
            })
            questions.append({
                "question": "The archeologist avoided _______ directly about the provenance of the looted artifacts.",
                "options": {"A": "being asked", "B": "be asked", "C": "asking", "D": "to be asked"},
                "answer": "A"
            })
            questions.append({
                "question": "This particular dialect, _______ in only three remote villages, is on the verge of extinction.",
                "options": {"A": "still spoken", "B": "still speaking", "C": "being still spoken", "D": "still being spoken"},
                "answer": "A"
            })
            questions.append({
                "question": "It is highly desirable that the perimeter fence _______ before the inspection next week.",
                "options": {"A": "will be repaired", "B": "is repaired", "C": "be repaired", "D": "repairs"},
                "answer": "C"
            })
            questions.append({
                "question": "The contract, despite _______ meticulously by both legal teams, contained a single fatal ambiguity.",
                "options": {"A": "having reviewed", "B": "being reviewed", "C": "having been reviewed", "D": "reviewed"},
                "answer": "C"
            })
            questions.append({
                "question": "For years, the true cost of the project _______ from the public, buried deep in obscure appendices.",
                "options": {"A": "hid", "B": "was hiding", "C": "was hidden", "D": "has hidden"},
                "answer": "C"
            })
            questions.append({
                "question": "The newly unearthed scrolls are believed _______ during the political purges of the first century.",
                "options": {"A": "to hide", "B": "to have hidden", "C": "to have been hidden", "D": "to be hiding"},
                "answer": "C"
            })
            questions.append({
                "question": "The panel determined that the error _______ earlier if the testing protocol had been more rigorous.",
                "options": {"A": "would discover", "B": "would have discovered", "C": "would be discovered", "D": "would have been discovered"},
                "answer": "D"
            })
            questions.append({
                "question": "Such behavior, which _______ from junior staff, will not be tolerated from senior management.",
                "options": {"A": "might overlook", "B": "might be overlooked", "C": "might have overlooked", "D": "might have been overlooked"},
                "answer": "B"
            })
            questions.append({
                "question": "The laboratory’s findings are striking, yet they resist _______ into simple policy recommendations.",
                "options": {"A": "being translated", "B": "translating", "C": "to translate", "D": "to be translated"},
                "answer": "A"
            })
            questions.append({
                "question": "The diplomat’s passport was confiscated, effectively _______ persona non grata.",
                "options": {"A": "to render him", "B": "rendering him", "C": "him rendered", "D": "having rendered him"},
                "answer": "B"
            })
            questions.append({
                "question": "Never in the history of the institution _______ such a contentious debate.",
                "options": {"A": "has witnessed", "B": "has been witnessed", "C": "it has witnessed", "D": "has it witnessed"},
                "answer": "B"
            })
            questions.append({
                "question": "The orator’s speech, though carefully crafted, came across as _______ rather than sincere.",
                "options": {"A": "rehearsed", "B": "having rehearsed", "C": "being rehearsed", "D": "to be rehearsed"},
                "answer": "A"
            })
            questions.append({
                "question": "It is essential that the wildlife corridor _______ by any new residential development.",
                "options": {"A": "is not encroached upon", "B": "not be encroached upon", "C": "does not encroach upon", "D": "be not encroached"},
                "answer": "B"
            })
            questions.append({
                "question": "The manuscript was written in such an archaic script that it _______ only by a handful of scholars.",
                "options": {"A": "could decipher", "B": "could be deciphered", "C": "can decipher", "D": "was able to decipher"},
                "answer": "B"
            })
            questions.append({
                "question": "The ambassador is accustomed to _______ with deference, making this public rebuke all the more shocking.",
                "options": {"A": "treat", "B": "be treated", "C": "being treated", "D": "having treated"},
                "answer": "C"
            })
            questions.append({
                "question": "Far from _______ by the setback, the team redoubled its efforts.",
                "options": {"A": "being discouraged", "B": "having discouraged", "C": "discouraging", "D": "be discouraged"},
                "answer": "A"
            })
            questions.append({
                "question": "The internal audit revealed that funds _______ for unauthorized purposes over a period of several years.",
                "options": {"A": "had systematically been diverted", "B": "had systematically diverted", "C": "had been systematically diverted", "D": "systematically had been diverted"},
                "answer": "C"
            })
            questions.append({
                "question": "The painting was in such poor condition that it required extensive restoration before it _______ to the public.",
                "options": {"A": "could display", "B": "could be displayed", "C": "can display", "D": "was displaying"},
                "answer": "B"
            })
            questions.append({
                "question": "At the press conference, the senator evaded _______ on the controversial provision in the bill.",
                "options": {"A": "questioning", "B": "to be questioned", "C": "being questioned", "D": "to question"},
                "answer": "C"
            })
            questions.append({
                "question": "This is the first time that a sitting monarch _______ under the provisions of this obscure statute.",
                "options": {"A": "has prosecuted", "B": "has been prosecuted", "C": "is prosecuting", "D": "prosecutes"},
                "answer": "B"
            })
            questions.append({
                "question": "The negotiations broke down after it became clear that neither side was willing _______.",
                "options": {"A": "to compromise", "B": "to be compromised", "C": "to have compromised", "D": "compromising"},
                "answer": "A"
            })
    return questions


# Struktur data QUESTIONS
QUESTIONS = {
    "MTK": {
        1: generate_questions("MTK", 1),
        2: generate_questions("MTK", 2),
        3: generate_questions("MTK", 3)
    },
    "Geografi": {
        1: generate_questions("Geografi", 1),
        2: generate_questions("Geografi", 2),
        3: generate_questions("Geografi", 3)
    },
    "Inggris": {
        1: generate_questions("Inggris", 1),
        2: generate_questions("Inggris", 2),
        3: generate_questions("Inggris", 3)
    }
}