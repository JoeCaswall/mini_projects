from random_number import random_number

def computer_choice():
    num = random_number()
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    else:
        return "scissors"
