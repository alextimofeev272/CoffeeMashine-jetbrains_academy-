class CofeeMashine:
    def __init__(self, water, milk, beans, disposable_cups, money):
        self.machine_state = {
            "water": water,
            "milk": milk,
            "beans": beans,
            "cups": disposable_cups,
            "money": money}

    def __str__(self):
        return f"The coffee machine has:\n{self.machine_state['water']} of water" \
               f"\n{self.machine_state['milk']} of milk" \
               f"\n{self.machine_state['beans']} of coffee beans" \
               f"\n{self.machine_state['cups']} of disposable cups" \
               f"\n${self.machine_state['money']} of money"

    def take(self):
        print(f"I gave you ${self.machine_state['money']}")
        self.machine_state['money'] = 0

    def fill(self):
        self.machine_state['water'] += int(input("Write how many ml of water do you want to add: "))
        self.machine_state['milk'] += int(input("Write how many ml of milk do you want to add: "))
        self.machine_state['beans'] += int(input("Write how many grams of coffee beans do you want to add: "))
        self.machine_state['cups'] += int(input("Write how many disposable cups of coffee do you want to add: "))

    def buy(self):
        coffee = {
            1: ["espresso", 250, 0, 16, 1, 4],
            2: ["latte", 350, 75, 20, 1, 7],
            3: ["cappuccino", 200, 100, 12, 1, 6]
        }
        type_coffee = input(f"What do you want to buy? 1 - {coffee[1][0]}, "
                            f"2 - {coffee[2][0]}, 3 - {coffee[3][0]}, back - to main menu: ")
        if type_coffee != "back":
            type_coffee = int(type_coffee)
            for i in range(4):
                if list(self.machine_state.items())[i][1] < coffee[type_coffee][i + 1]:
                    print(f"Sorry, not enough {list(self.machine_state.items())[i][0]}!")
                    ex = False
                    break
                else:
                    ex = True
            if ex:
                print("I have enough resources, making you a coffee!")
                self.machine_state['water'] -= coffee[type_coffee][1]
                self.machine_state['milk'] -= coffee[type_coffee][2]
                self.machine_state['beans'] -= coffee[type_coffee][3]
                self.machine_state['cups'] -= coffee[type_coffee][4]
                self.machine_state['money'] += coffee[type_coffee][5]


def action(coffeemashine):
    action_ = input("Write action (buy, fill, take, remaining, exit): ")
    if action_ == "buy":
        coffeemashine.buy()
    elif action_ == "fill":
        coffeemashine.fill()
    elif action_ == "take":
        coffeemashine.take()
    elif action_ == "remaining":
        print(coffeemashine)
    elif action_ == "exit":
        return 0


nespresso = CofeeMashine(400, 540, 120, 9, 550)
while action(nespresso) != 0:
    pass
