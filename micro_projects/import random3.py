import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if high!=low:
            guess = random.randint(low , high)
        else:
            guess = low
        feedback= input(f"Give {guess} if guess is high (H), low (l) or correct (c): ".lower())
        if feedback == 'h':
            high= guess - 1
        elif feedback=='l':
            low= guess + 1
    print(f"YAY!the computer guessed your number: {guess}")

computer_guess(20)
