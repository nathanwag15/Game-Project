from random import randrange
from PIL import Image




class Roulette:
    def __init__(self, money, chips):
        self.chips = chips
        self.money = money
        self.bet_list = []
        self.winning_total = []
        
    
    def make_a_bet(self):
        position = input("\nWould you like to make a inside bet or outside bet? ")
        position = position.lower()
        if position == "inside":
            number_of_chips = self.inside_chips()
            specific_bet = self.inside_bet()
        elif position == "outside":
            number_of_chips = self.outside_chips()
            specific_bet = self.outside_bet()
        else:
            print("\nThat is not a valid entry\n")
            self.make_a_bet()

        number_of_chips = int(number_of_chips)
        print(specific_bet)
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
            print("\nYou do not have enough chips to make that bet\n")
            self.buy_determine()

    def inside_chips(self):
        number_of_chips = input("\nYou can make a minimum of $1 in chips per bet. How many chips would you like to place on this bet? " )
        number_of_chips_list = self.list_maker(number_of_chips)
        if len(number_of_chips_list) > 1:
            print("\nThat is an invalid entry\n")
            number_of_chips = self.inside_chips()      
        number_of_chips = int(number_of_chips)
        return number_of_chips

    def inside_bet(self):
        specific_bet = input("\nWhat would you like to bet on? ")
        specific_bet = self.list_maker(specific_bet)
        return specific_bet

    def outside_chips(self):
        number_of_chips = input("\nYou can make a minimum of $5 in chips per bet. How many chips would you like to place on this bet? ")
        number_of_chips_list = self.list_maker(number_of_chips)
        number_of_chips = int(number_of_chips)
        if len(number_of_chips_list) > 1:
            print("\nThat is an invalid entry\n")
            number_of_chips = self.inside_chips()
        elif number_of_chips < 5:
            print("\nThat is not enough chips for a outside bet\n")
            self.outside_chips()
        return number_of_chips
    
    def outside_bet(self):
        specific_bet = input("\nWhat would you like to bet on? ")
        specific_bet = specific_bet.lower()
        
        if specific_bet == "red" or specific_bet == "black" or specific_bet == "odd" or specific_bet == "even" or specific_bet == "first half" or specific_bet == "last half" or specific_bet == "first 12" or specific_bet == "second 12" or specific_bet == "third 12":
            return specific_bet
        elif specific_bet != "red" or specific_bet != "black" or specific_bet != "odd" or specific_bet != "even" or specific_bet != "first half" or specific_bet != "last half" or specific_bet != "first 12" or specific_bet != "second 12" or specific_bet != "third 12":
            print("\nThat is not a vald entry you can say red or black or odd or even or first half or last half or first 12 or second 12 or third 12\n")
            self.make_a_bet()
       

    def redo(self):
        retry = input("\nwould you like to add another bet? ")
        redo = retry.lower()
        if redo == "yes":
            self.make_a_bet()
        elif redo =="no":
            print("Ok this is your bet")
            print(self.bet_list)
            self.find_win()
        else:
            print("That is a invalid entry")
            self.redo()


    def board(self):
        im = Image.open("image.jpg")
        im.show()
    
    def buy_chips(self):
        self.chips = int(input(f"\nEach chip is worth 1$ at our casino how many chips would you like to buy? You currently have ${self.money}: "))
        self.money -= self.chips
        self.get_money()

    def get_money(self):
        print(f"\nYou currently have ${self.money}")
    
    def get_chips(self):
        print(f"\nYou currently have {self.chips} chips")

    def buy_determine(self):
        buy = input("\nWould you like to buy some chips? ")
        buy = str(buy)
        if buy == "yes":
            self.buy_chips()
            self.make_a_bet()
        elif buy == "no":
            still_bet = input("\nWould you like to still make a bet?")
            if still_bet == "yes":
                self.make_a_bet()
            else:
                print("Ok")
        else:
            print("\nthat is not a valid entry")
            self.buy_determine()

    def list_maker(self, string):
        string = string.split("," " ")
        for i in range(len(string)):
            string[i] = int(string[i])
        return string
        

    def find_win(self):
        for bet in self.bet_list:
            for i in bet.keys():
                values = bet.get(i)
                chips = i
                for i in values:
                    if i == self.winning_total[0]:
                        self.winning_calculator_inside(values, chips)
                if values == self.winning_total[1]:
                    self.winning_calculator_color(chips)
                elif self.winning_total[0] % 2 == 0:
                    if values == "even":
                        self.winning_calculator_outside(chips)
                elif self.winning_total[0] % 2 != 0:
                    if values == "odd":
                        self.winning_calculator_outside(chips)
                elif self.winning_total[0] <= 18:
                    if values == "first half":
                        self.winning_calculator_outside(chips)
                elif self.winning_total[0] >= 19:
                    if values == "last half":
                        self.winning_calculator_outside(chips)
                elif self.winning_total[0] <= 12:
                    if values == "first 12":
                        self.winning_calculator_dozen(chips)
                elif self.winning_total[0] >= 13 and self.winning_total[0] <= 24:
                    if values == "second 12":
                        self.winning_calculator_dozen(chips)
                elif self.winning_total[0] >= 25:
                    if values == "third 12":
                        self.winning_calculator_dozen(chips)
                else:
                    print("\nYou Didn't Win Better Luck next time")
                    
        self.spin_again()
    
    def spin_again(self):
        try_again = input("Would you like to try again? ")
        try_again = try_again.lower()
        if try_again == "yes":
            self.bet_list = []
            self.randomGenerator()
            self.make_a_bet()

    def winning_calculator_dozen(self, chips):
        won_chips = chips * 3
        self.chips += won_chips
        print("You won!")
        self.get_chips()

    def winning_calculator_outside(self, chips):
        won_chips = chips * 2
        self.chips += won_chips
        print("You won!")
        self.get_chips()

    def winning_calculator_inside(self, values_list, chips):
        if len(values_list) == 1:
            won_chips = chips * 30
            self.chips += won_chips
            print("You won!")
            self.get_chips()
        elif len(values_list) == 2:
            won_chips = chips * 17
            self.chips += won_chips
            print("You won!")
            self.get_chips()
        elif len(values_list) == 3: 
            won_chips = chips * 11
            self.chips += won_chips
            print("You won!")
            self.get_chips()
        elif len(values_list) == 4:
            won_chips = chips * 8
            self.chips += won_chips
            print("You won!")
            self.get_chips()

    def randomGenerator(self):
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
        self.winning_total = [winning_number] + [wheel[winning_number]]
        return(self.winning_total)


round = Roulette(100, 0)

round.randomGenerator()
round.board()

round.buy_chips()
round.make_a_bet()


