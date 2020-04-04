import random
from random import shuffle


def straight_check(list, run_count=1):
    list.sort()
    if len(list) == 1:
        if run_count == 4:
            return True
        else:
            return False
    elif run_count == 4:
        return True
    elif list[0] + 1 == list[1]:
        return straight_check(list[1:], run_count + 1)
    else:
        return straight_check(list[1:], 1)

def countz(list, value):
    x = 0
    for yeet in list:
        if yeet == value:
            x += 1
    return int(x)

class player:
    def __init__(self):
        self.hand = []
        self.ask_name = input("What is your name?")
        self.name = self.ask_name

    def deal(self, core):
        random.shuffle(core.deck)
        x = 0
        while x <= core.deal_numbers[core.round_num] - 1:
            card = core.deck[x]
            card = card[0]
            self.hand.append(card)
            x += 1
        print("Your hand is:")
        print(self.hand)
        print("")

    def turn(self, core):
        random.shuffle(core.deck)
        print("The card showing is " + core.card_showing)
        choice = input("What would you like to do? (draw or pick)")
        if choice == "draw":
            self.hand.append(core.deck[0][0])
            print("You picked up "+str(core.deck[0]))
        else:
            self.hand.append(core.card_showing)
            print("You picked up "+core.card_showing)
        print(self.hand)
        print("")
        discard = input("What would you like to discard? (which number of card)")
        discard = self.hand[int(discard)-1]
        core.card_showing = discard
        self.hand.remove(discard)
        print("You discarded "+ str(discard))
        print(self.hand)
        print("")
        random.shuffle(core.deck)

    def buy(self, core):
        if not core.card_showing == "''":
            buy = input("The card showing is " + core.card_showing + ". Would you like to buy it? (yes or no)")
            if buy == "yes":
                self.hand.append(core.card_showing)
                core.card_showing = ""
                self.hand.append(core.deck[0][0])
                self.hand.append(core.deck[1][0])
                print("You also picked up " + str(core.deck[0][0]) + " and " + str(core.deck[1][0]))
                print("")
                print("Your current hand is")
                print(self.hand)

    def winning_check(self, core):
        roundz = list(core.rounds[core.round_num])
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
                check_duplicates = card_values[:]
                for element in check_duplicates:
                    z = int(check_duplicates.count(element))
                    if z > 1:
                        check_duplicates.remove(element)
                        check_duplicates.append(element)
                        check_duplicates.sort()
                run_check = straight_check(check_duplicates, 1)
                if run_check:
                    check.append("yes")
                else:
                    check.append("no")

        if check.count("yes") == 2:
            print("Yippee")
            core.win = True
        else:
            core.win = False


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

def main():
    core = game()
    number = int(input("How many players?"))
    players = []
    x = 0
    while x < number:
        players.append(player())
        x += 1
    for element in players:
        element.deal(core)
    while not core.win:
        turn = 0
        while turn <= number:
            players[turn].turn(core)
            players[turn].winning_check(core)
            next_player = turn + 1
            if next_player > number:
                next_player = 0
            players[next_player].buy(core)
            for thing in players:
                thing.buy(core)
            turn += 1

main()














