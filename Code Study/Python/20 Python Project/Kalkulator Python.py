#Kalkulator Python
operator = input("Masukkan Operasi(+ - * /): ")
num1 = float(input("Masukkan Angka:"))
num2 = float(input("Masukkan Angka:"))

if operator == "+":
    result_plus = num1 + num2
    print(result_plus)
elif operator == "-":
     result_min = num1-num2
     print(result_min)
elif operator == "*":
    result_times = num1 * num2
    print(result_times)
elif operator == "/":
    result_split = num1/num2
    print(result_split)
else:
    print("Masukkan operasi yang benar")

