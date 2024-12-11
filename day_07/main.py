import random
from hangman_art import stages, logo2, logo3
from hangman_words import word_list

chosen_word = random.choice(word_list)
#print(chosen_word)
print(logo3)
print("\nTo win, guess the word before you run out of lives.\n")

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"

game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"*********************** {lives}/6 LIVES LEFT ***********************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed: '{guess}'")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("\x1b[6;30;42m" + " Word to guess: " + "\x1b[0m" + " " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou guessed '{guess}', that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("\n*********************** GAME OVER. YOU LOSE! ***********************")
            print(f"The word is: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("\n*********************** YOU WIN! ***********************")
        print(logo2)
    
    print(stages[lives])