#game rock, scissors, paper
import random

choice = ["rock", "scissors", "paper"]
coin = ["obverse", "reverse"]

def nachalo():
    print("What game do you want to play: rock paper scissors or coin tossing. To exit, write: 0 or exit.")
    res = input(str("the first(1) or the second(2): "))
    if res == "1":
        return game()
    elif res == "2":
        return game_two()
    elif str(res) == "0" or str(res) == "exit":
            print("Thanks for playing!")


def game_two():
    print("In this game, you choose a side, after that a coin is thrown and the result falls out. To exit, write: 0 or exit.")
    while True:
        res = random.choice(coin)
        value_user = input(str("Enter obverse or reverse: "))
        if str(value_user) == str(res):
            print("You Lucky;)")
        elif str(value_user) == "0" or str(value_user) == "exit":
            print("Thanks for playing!")
            return nachalo()
        else:
            print(f"You Lose! Fall: {res}")
        


def game():
    print("Play with these three items: rock, scissors, paper. To exit, write: 0 or exit.")
    while True:
        res = random.choice(choice)
        try:
            value_user = input(str("Enter the gesture: "))
            if str(res) == str(value_user.lower()) and str(value_user) != "0" and str(value_user) != "exit":
                print("You Win!")
            elif str(value_user) == "0" or str(value_user) == "exit":
                print("Thanks for playing!")
                return nachalo()
            else:
                print(f"You Lose! Bot threw: {res}")
        except:
            print("You entered the wrong characters! Play with these three items: rock, scissors, paper.")


if __name__ == "__main__":
    nachalo()
    