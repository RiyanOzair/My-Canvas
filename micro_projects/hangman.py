import random
from micro_projects.words import words
from micro_projects.stickk import lives_visual_dict
import string

def valid_selection(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
         word = random.choice(words)

    return word.upper()

def hangman():
     word = valid_selection(words)# here
     word_letters = set(word)
     alphabet = set(string.ascii_uppercase)#here
     used_letters = set()

     lives = 7

     while len(word_letters) > 0 and lives > 0:
        print("You have", lives,"lives left""  You have guessed these letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "_" for letter in word ]
        print(lives_visual_dict[lives])
        print("the Current Word is :", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()# here
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives = lives - 1 
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print("ttry again")
        else:
            print("invalid")
     if lives == 0:
         print(lives_visual_dict[lives])
         print("you have lost the word was:", word)
     else:
         print("you won you guess the word:", word)
if __name__ == '__main__':        
    hangman()         
        
        

     
         