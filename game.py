from random import randrange
from PIL import Image


def randomGenerator():
    wheel = {
        0: "green",
        1: "red",
        2: "black",
        3: "red",
        4: "black",
        5: "red",
        6: "black",
        7: "red",
        8: "black",
        9: "red",
        10: "black",
        11: "black",
        12: "red",
        13: "black",
        14: "red",
        15: "black",
        16: "red",
        17: "black",
        18: "red",
        19: "red",
        20: "black",
        21: "red",
        22: "black",
        23: "red",
        24: "black",
        25: "red",
        26: "black",
        27: "red",
        28: "black",
        29: "black",
        30: "red",
        31: "black",
        32: "red",
        33: "black",
        34: "red",
        35: "black",
        36: "red"
    }
    winning_number = randrange(0, len(wheel)-1)
    winning_total = [winning_number] + [wheel[winning_number]]
    return(winning_total)



class Roulette:
    def __init__(self, money, chips):
        self.chips = chips
        self.money = money
        self.bet_list = []
    
    def make_a_bet(self):
        bet = {}
        position = input("Would you like to make a inside bet or outside bet? ")
        position = position.lower()
        if position == "inside":
            number_of_chips = input("You can make a minimum of $1 in chips per bet. How many chips would you like to place on this bet? " )
            specific_bet = input("What would you like to bet on? ")
            specific_bet = self.list_maker(specific_bet)
        elif position == "outside":
            number_of_chips = input("You can make a minimum of $5 in chips per bet. How many chips would you like to place on this bet? ")
            if number_of_chips < '5':
                number_of_chips = input("You need to have more than $5 worth in chips to bet outside. How many chips would you like to place on this bet? ") 
                specific_bet = input("What would you like to bet on? ")
            else:
                specific_bet = input("What would you like to bet on? ")
        else:
            print("That is not a valid entry")
            self.make_a_bet()

        number_of_chips = int(number_of_chips)

        if self.chips < number_of_chips:
            print("You do not have enough chips to make that bet")
            self.buy_determine()
        
        self.chips -= number_of_chips
        bet[number_of_chips] = specific_bet
        self.bet_list.append(bet)

        retry = input("would you like to add another bet? ")
        redo = retry.lower()
        if redo == "yes":
            self.make_a_bet()
            self.get_chips()
        else:
            print("Ok this is your bet")
            print(self.bet_list)
            

    def board(self):
        im = Image.open("image.jpg")
        im.show()
    
    def buy_chips(self):
        self.chips = int(input(f"Each chip is worth 1$ at our casino how many chips would you like to buy? You currently have ${self.money}: "))
        self.money -= self.chips
        self.get_money()

    def get_money(self):
        print(f"You currently have ${self.money}")
    
    def get_chips(self):
        print(f"You currently have {self.chips} chips")

    def buy_determine(self):
        buy = input("Would you like to buy some chips? ")
        buy = str(buy)
        if buy == "yes":
            self.buy_chips()
            self.make_a_bet()
        elif buy == "no":
            still_bet = input("Would you like to still make a bet?")
            if still_bet == "yes":
                self.make_a_bet()
            else:
                print("Ok")
        else:
            print("that is not a valid entry")
            self.buy_determine()

    def list_maker(self, string):
        string = string.split("," " ")
        for i in range(len(string)):
            string[i] = int(string[i])
        return string
        


print(randomGenerator())
round = Roulette(100, 0)

round.buy_chips()
round.make_a_bet()

