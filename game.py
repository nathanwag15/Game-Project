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
        position = input("Would you like to make a inside bet or outside bet? ")
        position = position.lower()
        if position == "inside":
            number_of_chips = self.inside_chips()
            specific_bet = self.inside_bet()
        elif position == "outside":
            number_of_chips = self.outside_chips()
            specific_bet = self.outside_bet()
        else:
            print("That is not a valid entry")
            self.make_a_bet()

        number_of_chips = int(number_of_chips)
        print(specific_bet10)
        self.chip_checker(number_of_chips)        
        self.chip_subtracter(number_of_chips)
        self.bet_list_maker(number_of_chips, specific_bet)
        self.redo()
        

    def bet_list_maker(self, number_of_chips, specific_bet):
        bet = {}
        bet[number_of_chips] = specific_bet
        self.bet_list.append(bet)

    def chip_subtracter(self, number_of_chips):
        self.chips -= number_of_chips

    def chip_checker(self, number_of_chips):
        if self.chips < number_of_chips:
            print("You do not have enough chips to make that bet")
            self.buy_determine()

    def inside_chips(self):
        number_of_chips = input("You can make a minimum of $1 in chips per bet. How many chips would you like to place on this bet? " )
        number_of_chips_list = self.list_maker(number_of_chips)
        number_of_chips = int(number_of_chips)
        if len(number_of_chips_list) > 1:
            print("That is an invalid entry")
            self.inside_chips()      
        return number_of_chips

    def inside_bet(self):
        specific_bet = input("What would you like to bet on? ")
        specific_bet = self.list_maker(specific_bet)
        return specific_bet

    def outside_chips(self):
        number_of_chips = input("You can make a minimum of $5 in chips per bet. How many chips would you like to place on this bet? ")
        number_of_chips_list = self.list_maker(number_of_chips)
        number_of_chips = int(number_of_chips)
        if len(number_of_chips_list) > 1:
            print("That is an invalid entry")
            self.inside_chips()
        elif number_of_chips < 5:
            print("That is not enough chips for a outside bet")
            self.outside_chips()
        return number_of_chips
    
    def outside_bet(self):
        specific_bet = input("What would you like to bet on? ")
        specific_bet = specific_bet.lower()
        if specific_bet == "red" or specific_bet == "black" or specific_bet == "odd" or specific_bet == "even" or specific_bet == "first half" or specific_bet == "last half" or specific_bet == "first 12" or specific_bet == "second 12" or specific_bet == "third 12":
            return specific_bet
        elif specific_bet != "red" or specific_bet != "black" or specific_bet != "odd" or specific_bet != "even" or specific_bet != "first half" or specific_bet != "last half" or specific_bet != "first 12" or specific_bet != "second 12" or specific_bet != "third 12":
            print("That is not a vald entry you can say red or black or odd or even or first half or last half or first 12 or second 12 or third 12")
            self.outside_bet()

    def redo(self):
        retry = input("would you like to add another bet? ")
        redo = retry.lower()
        if redo == "yes":
            self.make_a_bet()
        elif redo =="no":
            print("Ok this is your bet")
            print(self.bet_list)
        else:
            print("That is a invalid entry")
            self.redo()


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
        

    def find_win(self):
        for bet in self.bet_list:
            print(bet)

print(randomGenerator())
round = Roulette(100, 0)

round.board()

round.buy_chips()
round.make_a_bet()

round.find_win()
round.board()