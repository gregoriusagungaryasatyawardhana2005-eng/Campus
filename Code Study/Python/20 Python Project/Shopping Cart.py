#Shopping Cart

foods = []
prices = []
total = 0
while True:
    food = input(f"Masukkan Makanan:")
    if food.lower() == "q":
        break
    else:
        price = float(input("Harga Makanan: "))
        foods.append(food)
        prices.append(price)

print("----Shopping Cart----")
for i in range (len(foods)):
    current_food = foods[i]
    current_price = prices[i]
    total += prices[i]
    print(f"{current_food}---- Rp{current_price}")
print(f"Total Harga {total}")

    
    
