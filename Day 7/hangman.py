import random
import hangman_words
import hangman_arts

placeholder = ""
game_over = False
correct_letters = []
#all_guessed_letters = []
lives = 6

print("Welcome to Hangman")

chosen_word = random.choice(hangman_words.word_list)
length_of_chosen_word = len(chosen_word)


for position in range(length_of_chosen_word):
    placeholder += "_"
print(placeholder)


while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed letter: \"{guess}\" Guess another letter: ")
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"************************ LIFE REMAINIG: {lives} ************************")
        if lives == 0:
            game_over = True
            print(hangman_arts.stages[lives])
            print("************************ YOU LOSE ************************")
            print(f"************************ The word is {chosen_word} ************************")

    if "_" not in display:
        game_over = True 
        print("************************ YOU WIN ************************.")

    print(hangman_arts.stages[lives])
    #all_guessed_letters = all_guessed_letters.append(guess)

