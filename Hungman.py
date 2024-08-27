import random
import hangman_words
import hangman_arts

print(hangman_arts.logo)
random_word=random.choice(hangman_words.word_list)
print(random_word)

word_len=len(random_word)
print(word_len)


display_dash= []
for i in range(word_len):
    display_dash += "_"

print(display_dash)
lives = 6
while True:
    guess = input("Give your guess letter :")
    if guess in display_dash:
        print("You have already have guess this character")

    for i in range(word_len):
        letter = random_word[i]
        if letter == guess:
            print(f"Your guess is correct ,you have {lives} lives left ")
            print(hangman_arts.stages[lives])
            display_dash[i]=guess


    if guess not in random_word:
        lives-=1
        print("You have guess wrong ,the letter is not present in give word ,you have {lives} lives left ")
        print(hangman_arts.stages[lives])

        if lives == 0:
            print(f"You have loss the game ,you have {lives} live")
            print(hangman_arts.stages[lives])
            break

    display = ""
    for i in display_dash:
        display=display_dash

    print(display)
    if "_" not in display_dash:
        print("you have win the game ")
        print(hangman_arts.stages[lives])
        print(f"Your correct word is {display_dash}")
        break