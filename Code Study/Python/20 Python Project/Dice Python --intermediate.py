import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

#● ┌ ─ ┐ │ └ ┘



Dice_art = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│ ●       │",
       "│         │",
       "│       ● │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│ ●       │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘")}

Dice = []
total = 0
num_of_dice = int (input("How Many Dice?: "))

for die in range (num_of_dice):
    Dice.append(random.randint(1,6))
  #  for line in Dice_art.get(Dice[die]):
   #     print(line)

for line in range (5):
    for die in Dice:
        print(Dice_art.get(die)[line],end="")
    print()
    
for die in Dice:
    total += die
print(f"total: {total}")

