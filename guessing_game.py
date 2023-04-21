#imports
import random

#getting word list
word_file = open("word_list.txt", "r")

words = word_file.read()

word_list = words.split("\n")

strikes = 0

#main loop
loop = True
while loop:
    play = input("This is a guessing game! All you have to do is guess the word one letter at a time, but you have 3 strikes. Want to play? (y/n) - ")

    if play == 'y':
        #word to guess
        word = word_list[random.randint(0, len(word_list)-1)]

        #blanks for the word
        guess_word = ''

        for letter in range(len(word)):
            guess_word = guess_word + '_ '

        guess_word = guess_word.split()
        guess_word_string = ''
        
        #guessing loop
        while guess_word_string != word and strikes < 3:

            guess_word_string = ''
            for i in range(len(guess_word)):
                guess_word_string = guess_word_string + guess_word[i]
                guess_word_string = guess_word_string + ' '
            
            print(f"guess the word: {guess_word_string}")

            letter_guess = input("Guess a letter - ")

            if letter_guess in word:
                for letter in range(len(word)):
                    if letter_guess == word[letter]:
                        guess_word[letter] = letter_guess

            #strikes
            else:
                print('')
                print('STRIKE')
                print('')
                strikes += 1
                if strikes > 2:
                    print('you lost :(')
                    print('')
                    strikes = 0
                    play = input("Do you want to play again? (y/n) - ")
                    if play == 'y':
                        pass
                    elif play == 'n':
                        print('fine')
                        loop = False


            guess_word_string = ''
            for i in range(len(guess_word)):
                guess_word_string = guess_word_string + guess_word[i]

        if guess_word_string == word:
            print("you won!")
            print('')

    elif play == 'n':
        print("Whatever. ")
        loop = False

    else:
        while play != 'y' or play != 'n':
            play = input("I can't understand you, would you like to play? (y/n) - ")

word_file.close()