#Author: Shivansh joshi
import sys
water,milk,coffeebeans,cups,balance=400,540,120,9,550
class coffeeMachine:
    def display_remain(self):
        print("The coffee machine has:")
        print(water, "of water")
        print(milk, "of milk")
        print(coffeebeans, "of coffee beans")
        print(cups, "of disposable cups")
        print("${0} of money".format(balance))
    def espresso(self):
        global water
        water -= 250
        global coffeebeans
        coffeebeans -= 16
        global balance
        balance += 4
        global cups
        cups -= 1
    def latte(self):
        global water
        water -= 350
        global milk
        milk -= 75
        global coffeebeans
        coffeebeans -= 20
        global balance
        balance += 7
        global cups
        cups -= 1
    def cappuccino(self):
        global water
        water -= 200
        global milk
        milk -= 100
        global coffeebeans
        coffeebeans -= 12
        global balance
        balance += 6
        global cups
        cups -= 1
    def checkpresent(self,x):
        global milk;global coffeebeans;global cups;global water;global balance
        if (x == 1):
            if water < 250:
                return 1
            elif coffeebeans < 16:
                return 3
            elif balance < 4:
                return 4
            elif cups < 1:
                return 5
            else:
                return 0
        elif (x == 2):
            if water < 350:
                return 1
            elif milk < 75:
                return 2
            elif coffeebeans < 20:
                return 3
            elif balance < 7:
                return 4
            elif cups < 1:
                return 5
            else:
                return 0
        else:
            if water < 200:
                return 1
            elif milk < 100:
                return 2
            elif coffeebeans < 12:
                return 3
            elif balance < 6:
                return 4
            elif cups < 1:
                return 5
            else:
                return 0
while(1):
    print()
    obj=coffeeMachine()
    firstoption=input("Write action (buy, fill, take, remaining, exit):")
    print()
    if(firstoption=='buy'):
        choise=input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choise=='1':
            cond=obj.checkpresent(1)
            if(cond==0):
                print("I have enough resources, making you a coffee!")
                obj.espresso()
            elif(cond==1):
                print("Sorry, not enough water!")
            elif(cond==2):
                print("Sorry, not enough milk!")
            elif(cond==3):
                print("Sorry, not enough coffee beans!")
            elif(cond==4):
                print("Sorry, not enough money!")
            else:
                print("Sorry, not enough disposable cups!")
        elif choise=='2':
            cond=obj.checkpresent(2)
            if(cond==0):
                print("I have enough resources, making you a coffee!")
                obj.latte()
            elif(cond==1):
                print("Sorry, not enough water!")
            elif(cond==2):
                print("Sorry, not enough milk!")
            elif(cond==3):
                print("Sorry, not enough coffee beans!")
            elif(cond==4):
                print("Sorry, not enough money!")
            else:
                print("Sorry, not enough disposable cups!")
        elif choise=='3':
            cond = obj.checkpresent(3)
            if (cond == 0):
                print("I have enough resources, making you a coffee!")
                obj.cappuccino()
            elif (cond == 1):
                print("Sorry, not enough water!")
            elif (cond == 2):
                print("Sorry, not enough milk!")
            elif (cond == 3):
                print("Sorry, not enough coffee beans!")
            elif (cond == 4):
                print("Sorry, not enough money!")
            else:
                print("Sorry, not enough disposable cups!")
        else:
            pass
    elif(firstoption=='fill'):
        wateradd=int(input("Write how many ml of water do you want to add:"))
        milkadd=int(input("Write how many ml of milk do you want to add:"))
        coffeebeansadd=int(input("Write how many grams of coffee beans do you want to add:"))
        cupsadd=int(input("Write how many disposable cups of coffee do you want to add:"))
        water+=wateradd
        milk+=milkadd
        cups+=cupsadd
        coffeebeans+=coffeebeansadd
    elif(firstoption=='take'):
        print("I gave you ${0}".format(balance))
        balance=0
    elif(firstoption=='remaining'):
        obj.display_remain()
    else:
        sys.exit()   
        
#Author: Ashutosh vyas
"""
class CoffeeMaker:
    def __init__(self):
        self.machine = [400, 540, 120, 9, 550]

    def __str__(self):
        return '''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money'''.format (self.machine[0], self.machine[1], self.machine[2], self.machine[3], self.machine[4] if self.machine[4] == 0 else "$"+str(self.machine[4]))

    def can_make(self, needed):
        items = ["water", "milk", "coffee beans", "disposable cups"]
        for item, have, need in zip(items, self.machine[0:4], needed):
            if need > have:
                print("Sorry, not enough " + item + "!")
                return False
        print("I have enough resources, making you a coffee!")
        return True

    def buy(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:\n")
        if coffee_type == '1':
            if self.can_make([250, 0, 16, 1]):
                self.machine = [self.machine[0] - 250, self.machine[1], self.machine[2] - 16, self.machine[3] - 1,
                                self.machine[4] + 4]
        elif coffee_type == '2':
            if self.can_make([350, 75, 20, 1]):
                self.machine = [self.machine[0] - 350, self.machine[1] - 75, self.machine[2] - 20, self.machine[3] - 1,
                                self.machine[4] + 7]
        elif coffee_type == '3':
            if self.can_make([200, 100, 12, 1]):
                self.machine = [self.machine[0] - 200, self.machine[1] - 100, self.machine[2] - 12, self.machine[3] - 1,
                                self.machine[4] + 6]
        elif coffee_type == "back":
            pass

    def fill(self):
        self.machine[0] += int(input("\nWrite how many ml of water do you want to add:\n"))
        self.machine[1] += int(input("Write how many ml of milk do you want to add:\n"))
        self.machine[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.machine[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print("\nI gave you $" + str(self.machine[4]))
        self.machine[4] = 0


user = CoffeeMaker()
while True:
    input_ = input("\nWrite action (buy, fill, take, remaining, exit):\n")
    if input_ == "buy":
        user.buy()
    elif input_ == "fill":
        user.fill()
    elif input_ == "take":
        user.take()
    elif input_ == "remaining":
        print("\n" + str(user))
    elif input_ == "exit":
        break
"""