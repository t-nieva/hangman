import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
placeholder = ''

print(logo)
print(chosen_word)
for letter in chosen_word:
    placeholder += '_'
print(f"Word to gues: {placeholder}")
game_over = False
correct_letters = []
lives = 5

while not game_over:
    print(f"************************************** {lives} LIVES LEFT **************************************")
    display = ''
    guess = input("Guess a letter: ").lower().strip()

    if guess in correct_letters:
        print(f"You are already gues the letter: {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("************************************** You win. **************************************")
    if lives == 0:
        game_over = True
        print(f'************************************** IT WAS {chosen_word}! YOU LOSE! **************************************')
