import time
import msvcrt  # Modul khusus Windows untuk deteksi tombol keyboard

# 1. Input Waktu
waktu_input = input("Masukkan Waktu (Jam:Menit:Detik): ")
jam, menit, detik = map(int, waktu_input.split(":"))

# Simpan total detik awal untuk keperluan Reset
total_awal = (jam * 3600) + (menit * 60) + detik
sisa_waktu = total_awal

print("\n--- Tekan 'y' untuk STOP | Tekan 'n' untuk RESET ---")

# 2. Gunakan While Loop agar fleksibel
while sisa_waktu >= 0:
    # Konversi detik kembali ke Jam:Menit:Detik
    h = sisa_waktu // 3600
    m = (sisa_waktu % 3600) // 60
    s = sisa_waktu % 60
    
    # Tampilkan Waktu
    print(f"{h:02}:{m:02}:{s:02}   ", end="\r", flush=True)
    
    # 3. Logika Deteksi Tombol
    # msvcrt.kbhit() mengecek apakah ada tombol yang sedang ditekan
    if msvcrt.kbhit():
        # msvcrt.getch() mengambil tombol yang ditekan tersebut
        tombol = msvcrt.getch().decode('utf-8').lower()
        
        if tombol == 'y':  # STOP
            print("\nProgram Dihentikan oleh User.")
            break
        elif tombol == 'n':  # RESET
            print("\nTimer Direset ke Awal!   ")
            sisa_waktu = total_awal  # Kembalikan waktu ke awal
            time.sleep(1) # Jeda sebentar agar user lihat tulisan reset
            continue  # Ulangi loop dari atas tanpa mengurangi detik dulu

    time.sleep(1)
    sisa_waktu -= 1

if sisa_waktu < 0:
    print("\nWaktu Habis!             ")