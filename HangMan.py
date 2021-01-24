import random
from hangman_art import hangman_art, stages
from hangman_words import word_list
from os import system

print(hangman_art)  # printing hangman logo
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

num_blanks = len(chosen_word)
blanks = []

# inserting blanks equal to number of letters in chosen word
for i in range(num_blanks):
    blanks.append("_")
    print(blanks[i],end=" ")
print()
end_game = False

while not end_game:

    guess = input("Guess a letter: ")
    #system('cls')

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("Game Over!")
            end_game = True
        print(f"You guessed {guess}, thats not a correct word.You lose a life")
        print(stages[lives])

    if "_" in blanks:

        for index in range(num_blanks):
            letter = chosen_word[index]

            if letter == guess:
                blanks[index] = letter

    if "_" not in blanks:
        print("You win")
        end_game = True
    for j in blanks:
        print(j,end=" ")
    print()