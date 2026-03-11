#Python Compound Interest
Initial_Amount = 0
#int(input("Masukkan Nominal Awal: %i Rp"))
Interest = 0
#float(input("Masukkan Interest: %f %"))
time = 0
#int(input("Masukkan Waktu: %i Bulan"))
while True:
    Initial_Amount = float(input(f"Masukkan Nominal Awal: "))
    if Initial_Amount < 0:
        print(F"Nilai Tidak Valid")
    else:
        break

while True:
    Interest = float(input("Masukkan Interest : "))
    if Interest < 0:
        print(F"Nilai Tidak Valid")
    else:
        break

while True:
    time = int(input("Masukkan Waktu : "))
    if Initial_Amount < 0:
        print(f"Nilai Tidak Valid")
    else:
        break

Value = Initial_Amount * pow((1+Interest/100),time)
print(f"Nilai setelah {time} year/s: {Value:.2f}")