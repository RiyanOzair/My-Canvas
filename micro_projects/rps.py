import random

def play():
    user = input("Pick your choice : 'r' for rock 's' for scissors 'p' for paper : ")
    computer= random.choice(['r','s','p'])

    if user == computer:
        print(f"you picked {user} and computer picked {computer} so it's a tie!!")
    if winin(user , computer):
        return f"you picked {user} and computer picked {computer} so You win!!"
    return f"you picked {user} and computer picked {computer} so You lose!!"

def winin(player , opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())