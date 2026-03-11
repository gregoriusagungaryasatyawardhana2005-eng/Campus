#Python Qui
questions = ("How many elements are in periodic table?: ", 
            "Wich animal lays eggs?: ", 
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet is the hottest in solar system?: ")

options = ((" A.116 "," B.117 "," C.118 "," D.118 "),
           (" A.Whale "," B.Crocodile "," C.Elephant "," D.Osrthich "),
           (" A.CO "," B.O "," C.N "," D.CH2 ",),
           (" A.206 "," B.207 "," C.208 "," D.209 "),
           (" A.Mercury "," B.Venus "," C.Earth "," D.Mars "))


answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for i in range (len(questions)):
    print("-"*8)
    print(questions[i])
    for option in options[i]:
        print(f"{option}")
    guess = input("Enter (A , B , C , D): ").upper()
    guesses.append(guess)
    if guess == answers [i]:
        score += 1
        print("Answer Correct")
    else:
        print("Answer Incorrect")
        print(f"{answers[i]} is the corrext answer")
    question_num += 1
print(score)
