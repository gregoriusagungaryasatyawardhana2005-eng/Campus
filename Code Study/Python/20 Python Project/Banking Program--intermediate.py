import os  # <--- 1. WAJIB IMPORT INI

balance = 0
is_running = True

# Fungsi bantuan untuk membersihkan layar
def clear_screen():
    # 'cls' untuk Windows, 'clear' untuk Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def show_balance():
    clear_screen() # Bersihkan menu utama dulu
    print("--- INFO SALDO ---")
    print(f"Saldo Anda saat ini: ${balance:.2f}")
    # Kita butuh jeda supaya user bisa baca sebelum layar dihapus lagi
    input("\nTekan Enter untuk kembali ke menu...")

def deposit():
    clear_screen() # Bersihkan menu utama
    print("--- DEPOSIT ---")
    try:
        amount = float(input("Masukkan jumlah deposit: "))
        if amount <= 0:
            print("Jumlah tidak valid!")
            input("\nTekan Enter untuk kembali...")
            return 0
        else:
            print(f"Berhasil deposit ${amount:.2f}")
            input("\nTekan Enter untuk kembali...")
            return amount
    except ValueError:
        print("Input harus angka!")
        input("\nTekan Enter untuk kembali...")
        return 0

def withdraw():
    clear_screen() # Bersihkan menu utama
    print("--- PENARIKAN ---")
    try:
        amount = float(input("Masukkan jumlah penarikan: "))
        
        # Cek saldo di sini agar logic aman
        if balance < amount:
            print("Saldo tidak cukup!")
            input("\nTekan Enter untuk kembali...")
            return 0
        elif amount <= 0:
            print("Jumlah tidak valid!")
            input("\nTekan Enter untuk kembali...")
            return 0
        else:
            print(f"Berhasil menarik ${amount:.2f}")
            input("\nTekan Enter untuk kembali...")
            return amount
    except ValueError:
        print("Input harus angka!")
        input("\nTekan Enter untuk kembali...")
        return 0

# --- PROGRAM UTAMA ---

while is_running:
    # 2. HAPUS LAYAR SETIAP KALI LOOP DIMULAI (BALIK KE MENU)
    clear_screen()
    
    print("========================")
    print("    BANKING PROGRAM     ")
    print("========================")
    print("1. Cek Saldo")
    print("2. Deposit")
    print("3. Tarik Tunai")
    print("4. Keluar")
    print("========================")

    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        # Logic pengurangan dipindah ke sini
        # Note: fungsi withdraw di atas saya ubah sedikit agar return 0 kalau gagal
        temp_withdraw = withdraw()
        balance -= temp_withdraw
    elif choice == "4":
        is_running = False
        print("Terima kasih telah bertransaksi!")
    else:
        print("Pilihan salah!")
        input("Tekan Enter...")