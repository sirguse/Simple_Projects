import random
from words import words


def Hangman():
    attempts = 6
    choice_word = random.choice(words) # wybieram losowe słowo
    word_display = ['_' for _ in choice_word] # powoduje wstawienie "_" w miejsca słów, dzięki wykorzystaniu pustego stringa _ i iteracji po słowach


    while attempts > 0 and "_" in word_display:
        print('\n'+ ' '.join(word_display))
        guess = input("Wybierz litere") 
        if guess in choice_word:
            for index,letter in enumerate(choice_word):
                if guess == letter:
                    word_display[index] = guess

    
    
    
Hangman()
