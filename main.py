import random
from random import shuffle


def countz(list, value):
    x = 0
    for yeet in list:
        if yeet == value:
            x += 1
    return int(x)


class game:
    def __init__(self):
        self.values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        self.suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        self.deck = [[v + ' of ' + s] for s in self.suites for v in self.values]
        #self.number = input("How many players?")
        self.rounds = ["33","34","44","333","334","344","444"]
        self.deal_numbers = [6,7,8,9,10,11,12]
        self.hand = []
        self.round_num = 1
        self.round = self.rounds[self.round_num]
        self.card_showing = ""
        self.win = False

    def deal(self):
        random.shuffle(self.deck)
        x = 0
        while x <= self.deal_numbers[self.round_num]-1:
            card = self.deck[x]
            card = card[0]
            self.hand.append(card)
            x += 1
        print("Your hand is:")
        print(self.hand)
        print("")

    def turn(self):
        random.shuffle(self.deck)
        print("The card showing is " + self.card_showing)
        choice = input("What would you like to do? (draw or pick)")
        if choice == "draw":
            self.hand.append(self.deck[0][0])
            print("You picked up "+str(self.deck[0]))
        else:
            self.hand.append(self.card_showing)
            print("You picked up "+self.card_showing)
        print(self.hand)
        print("")
        discard = input("What would you like to discard? (which number of card)")
        discard = self.hand[int(discard)-1]
        self.card_showing = discard
        self.hand.remove(discard)
        print("You discarded "+ str(discard))
        print(self.hand)
        print("")
        random.shuffle(self.deck)

    def buy(self):
        buy = input("The card showing is "+self.card_showing+". Would you like to buy it? (yes or no)")
        if buy == "yes":
            self.hand.append(self.card_showing)
            self.card_showing = ""
            self.hand.append(self.deck[0][0])
            self.hand.append(self.deck[1][0])
            print("You also picked up "+str(self.deck[0][0])+" and "+str(self.deck[1][0]))
            print("")
            print("Your current hand is")
            print(self.hand)

    def winning_check(self):
        roundz = list(self.rounds[self.round_num])
        card_values = []
        check = []
        for element in self.hand:
            element = element.split()
            value = element[0]
            if value == "Jack":
                value = 11
            if value == "Queen":
                value = 12
            if value == "King":
                value = 13
            if value == "Ace":
                value = 14
            value = int(value)
            card_values.append(value)
        card_values.sort()
        for value in roundz:
            if value == "3":
                for element in card_values:
                    count = card_values.count(element)
                    if count == 3:
                        card_values.remove(element)
                        check.append("yes")
                    elif count > 3:
                        difference = count - 3
                        card_values.remove(element)
                        x = 0
                        while x < difference:
                            card_values.append(element)
                            x += 1
                        check.append("yes")
                    else:
                        check.append("no")
            if value == "4":
                print(card_values.count(5))
                check_duplicates = card_values[:]
                print(check_duplicates.count(5))
                for element in check_duplicates:
                    z = int(check_duplicates.count(element))
                    if z > 1:
                        check_duplicates.remove(element)
                        check_duplicates.append(element)
                        check_duplicates.sort()
                for element in check_duplicates:
                    index = card_values.index(element)
                    print(check_duplicates)
                    if check_duplicates[index+3] == element+3:
                        if check_duplicates[index+1] == element + 1 and check_duplicates[index+2] == element + 2:
                            check.append("yes")
                            x = 0
                            while x <= 3:
                                card_values.pop(index(element+x))
                                x += 1
                        else:
                            check.append("no")

        if check.count("yes") == 2:
            self.win = True
        else:
            self.win = False






games = game()
games.deal()
while not games.win:
    games.turn()
    games.winning_check()








