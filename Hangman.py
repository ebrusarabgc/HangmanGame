import random

word_list = ["blue", "black", "white", "red", "yellow", "green", "orange", "violet", "cyan", "gray", "purple"]

the_word = word_list[random.randint(0, len(word_list) - 1)]
letter_num = len(the_word)
lives = 6

hangman = [" _______\n |     |\n |\n |\n |\n |\n |\n---", " _______\n |     |\n |     O\n |\n |\n |\n |\n---",
           " _______\n |     |\n |     O\n |     |  \n |     | \n |\n |\n---",
           " _______\n |     |\n |     O\n |    /|  \n |     | \n |\n |\n---",
           " _______\n |     |\n |     O\n |    /|\ \n |     | \n |\n |\n---",
           " _______\n |     |\n |     O\n |    /|\ \n |     | \n |    /   \n |\n---",
           " _______\n |     |\n |     O\n |    /|\ \n |     | \n |    / \ \n |\n---"]

blanks = []
first = ""
for i in range(letter_num):
    blanks += "_"
    first += "_"

print("Let's play hangman game!")
print("(Hint: This is a colour.)")
print(first)

# The game ends when there's no life left or when the player finds the word.
while lives > 0 and "_" in blanks:
    letter = input("Guess a letter: ").lower()
    # The letter is in the word.
    if letter in the_word:
        # Replacing the blank(s) with the letter.
        for i in range(letter_num):
            if the_word[i] == letter:
                blanks[i] = letter
    # The letter is not in the word.
    else:
        lives -= 1

    # To print the list as a string
    word = ""
    for num in range(letter_num):
        word += blanks[num]

    print(f"The word: {word}\n{lives} lives left.")
    print(hangman[6 - lives])

if lives == 0:
    print(f"The word was {the_word}. You lose...")
else:
    print(f"The word was {the_word}. You won!")
