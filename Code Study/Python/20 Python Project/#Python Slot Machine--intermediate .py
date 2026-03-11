#Python Slot Machine

import random
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐'] 
    return [random.choice(symbols) for _ in range(3)] 

def print_row(row):
    print("*"*10)
    print(" | ".join(row))
    print("*"*10)

def get_payout(row,bet):
    if row[0] == row [1] == row[2]:
        if row[0] ==  "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 6
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0


def main():
    balance = 100
    print("*"*10) 
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐ ") 
    print("*"*10)

    while balance > 0:
        print(f"Current Balance: {balance}")
        while True:
            try:
                bet = float(input("Place your bet amount:"))
                break
            except ValueError:
                print("Please enter a valid number")

        if bet > balance:
            print("Insufficient funds")
            continue
        if bet<= 0:
            print("Bet must be greater than 0")
            continue
        balance -= bet 

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won {payout}")
        else:
            print(f"Sorry you lost this round")
        
        balance += payout
 
if __name__ == '__main__':
    main()