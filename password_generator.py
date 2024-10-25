import random
import string

def Password_Generator(lenght): #Pseudo randomowe generowanie hasła.
    password = ''
    random_strings = string.ascii_letters + string.digits + string.punctuation

    while lenght > 0:
        random_choice = random.choice(random_strings)
        password += random_choice
        lenght -= 1

    return password
    

    
def Password_Save(x,y):
    lenght = y
    with open('Simple_Projects/passwords.txt', 'a') as plik:
        while x > 0:
            haslo = Password_Generator(y)
            plik.write(f"{haslo}\n")
            x -= 1



print("1. Generowanie hasła wraz z zapisem")
print("2. Pokazanie zapisanych haseł")
print("3 Usuwanie zawartosci")

action = int(input("Wybierz akcje którą chcesz rozpocząć: "))

if action == 1:
    action_number = int(input("Podaj długość haseł: "))
    Password_Generator(action_number)

    action_number_second = int(input("Podaj ile haseł mam zapisać: "))
    Password_Save(action_number_second, action_number)

elif action == 2:
    
    with open('Simple_Projects/passwords.txt', 'r') as file:
        for line in file:
            print(line.strip())

elif action == 3:
    action_com = input("Czy napewno chcesz usunac całą zawartość? 1: Yes / 2: No").lower # do naprawy
    if action_com == 'yes':
        with open("Simple_Projects/passwords.txt", 'w') as fw:
            pass