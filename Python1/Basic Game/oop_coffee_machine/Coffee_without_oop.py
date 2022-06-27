MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_updater(drink_ans):
    if drink_ans == "espresso":
        resources['water'] = resources['water'] - 50
        resources['coffee'] = resources['coffee'] - 18
        WATER = resources['water']
        MILK = resources['milk']
        COFFEE = resources['coffee']
        print(f"WATER:{WATER} ml\nCOFFEE:{COFFEE}g\nMILK:{MILK} ml")

    elif drink_ans == "latte":
        resources['water'] = resources['water'] - 200
        resources['milk'] = resources['milk'] - 150
        resources['coffee'] = resources['coffee'] - 24
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        print(f"WATER:  {water}ml \nMILK:   {milk}g\nCOFFEE: {coffee} ml")

    elif drink_ans == "cappuccino":
        resources['water'] = resources['water'] - 250
        resources['milk'] = resources['milk'] - 100
        resources['coffee'] = resources['coffee'] - 24
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        print(f"WATER:  {water} ml\nMILK:   {milk} ml\nCOFFEE: {coffee}g")
    else:
        print("This drink is in hell! Wanna GO!")


def resources_sufficient(drink_ans):
    if drink_ans == "espresso" and resources['water'] >= 50 and resources['coffee'] >= 18:
        return 1
    elif drink_ans == "latte" and resources['water'] >= 200 and resources['coffee'] >= 24 and resources['milk'] >= 150:
        return 2
    elif drink_ans == "cappuccino" and resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >= 100:
        return 3
    else:
        return 0


def sufficient_coins(drink_ans):
    total_value = int(quaters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)
    if drink_ans == "espresso" and total_value >= MENU['espresso']['cost']:
        return 1
    if drink_ans == "latte" and total_value >= MENU['latte']['cost']:
        return 2
    if drink_ans == "cappuccino" and total_value >= MENU['cappuccino']['cost']:
        return 3


def game():
    nxt_customer = True
    while nxt_customer:
        global drink
        drink = input("What would you like? (espresso/latte/cappuccino):")
        if resources_sufficient(drink) != 0:
            global quaters
            global dimes
            global nickles
            global pennies
            quaters = int(input("Please insert coins.\nHow many quaters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            total_value = int(quaters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)
            change = total_value - MENU[drink]['cost']
            if drink == "espresso" and sufficient_coins(drink) == 1 and resources_sufficient(drink) == 1:
                print("Here is your espresso!☕️ ENJOY")
                print("Here is your change", change)
                resources_updater(drink)
                wanna_continue = input("Is here any next customer? y or n")
                if wanna_continue == "n":
                    nxt_customer = False
                else:
                    nxt_customer = True
            elif drink == "latte" and sufficient_coins(drink) == 2 and resources_sufficient(drink) == 2:
                print("Here is your latte!☕️ ENJOY")
                print("Here is your change", change)
                resources_updater(drink)
                wanna_continue = input("Is here any next customer? y or n")
                if wanna_continue == "n":
                    nxt_customer = False
                else:
                    nxt_customer = True
            elif drink == "cappuccino" and sufficient_coins(drink) == 3 and resources_sufficient(drink) == 3:
                print("Here is your cappuccino!☕️ ENJOY")
                print("Here is your change", change)
                resources_updater(drink)
                wanna_continue = input("Is here any next customer? y or n")
                if wanna_continue == "n":
                    nxt_customer = False
                else:
                    nxt_customer = True
            else:
                print("ERROR 404")
                nxt_customer = False
        elif drink == "report":
            WATER = resources['water']
            COFFEE = resources['coffee']
            MILK = resources['milk']
            print(f"WATER:{WATER} ml\nCOFFEE:{COFFEE}g\nMILK:{MILK} ml")
        else:
            print("Not Enough Resources")
            nxt_customer = False


game()
