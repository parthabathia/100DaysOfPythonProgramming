from resource import MENU, resources


def get_report():
    print("Available resources:")
    print(f"Milk: {resources['milk']}ml")
    print(f"Water: {resources['water']}ml")
    print(f"Coffee: {resources['coffee']}gms")
    print(f"Money: ${profit}")


def check_resources(drink_ingredients):
    """Returns bool value based on availability of sufficient ingredients"""
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from inserted coins"""
    print("Please insert coins.")
    total = int(input("Enter the number of quarters: ")) * 0.25
    total += int(input("Enter the number of dimes: ")) * 0.1
    total += int(input("Enter the number of nickels: ")) * 0.05
    total += int(input("Enter the number of pennies: ")) * 0.01
    return total


def transaction_success(money_received, drink_cost):
    """Returns bool value based on the status of the transaction"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} as change.")
        return True
    else:
        print("Sorry the amount paid is insufficient. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


profit = 0
machine_operating = True
while machine_operating:
    print("Welcome to PAB coin operated Coffee Service!")
    order = input("Kindly select your order?\n1. Espresso\n2. Latte\n3. Cappuccino\n").lower()
    if order == 'report':
        get_report()
    elif order == 'off':
        machine_operating = False
    else:
        drink = MENU[order]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_success(payment, drink['cost']):
                make_drink(order, drink['ingredients'])
