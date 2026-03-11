# Weight Converter
Class1 = input("Masukkan Kelas, Kilogram (K), Pound (P), Ounce (O): ")
Class2 = input("Masukkan Kelas, Kilogram (K), Pound (P), Ounce (O): ")
Weight = float(input("Masukkan Berat"))

if Class1 == "K" :
    if Class2 == "P":
        print("Nilai Konversi =",(round(Weight*2.20462,3)))
    elif Class2 == "K":
        print("Nilai Konversi =",(round(Weight,3)))
    elif Class2 == "O":
        print("Nilai Konversi =",(round(Weight*35.274,3)))
    else:
        print("Masukkan Class Yang Tepat")
elif Class1 == "P":
    if Class2 == "P":
        print("Nilai Konversi =",(round(Weight,3)))
    elif Class2 == "K":
        print("Nilai Konversi =",(round(Weight*0.453592,3)))
    elif Class2 == "O":
        print("Nilai Konversi =",(round(Weight*16,3)))
    else:
        print("Masukkan Class Yang Tepat")
elif Class1 == "O":
    if Class2 == "P":
        print("Nilai Konversi =",(round(Weight),0.0625,3))
    elif Class2 == "K":
        print("Nilai Konversi =",(round(Weight*0.0283495,3)))
        print("Nilai Konversi =",(round(Weight,3)))
    elif Class2 == "O":
        print("Nilai Konversi =",(round(Weight,3)))
    else:
        print("Masukkan Class Yang Tepat")
else:
    print("Masukkan Class Yang Tepat")



