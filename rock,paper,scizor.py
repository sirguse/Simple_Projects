import random
def RockPaperScizor():
    list = ['Rock', 'Paper', 'Scizor']
    x = random.choice(list).lower()
    
    z = input("Rock, Paper, Scizor").lower()

    if (z == 'rock' and x == 'scizor') or (z == "paper" and x == "rock") or (z == "scizor" and x== 'paper'):
        print("You won")
        print(f"Opponent choice {x}")
    elif (z == 'rock' and x == 'rock') or (z == 'paper' and x == 'paper') or (z =='scizor' and x == 'scizor'):
        print("Draw")
        print(f"Opponend choice: {x}")
    else:
        print("You lost")

        print(f"Opponend choice: {x}")


RockPaperScizor()
