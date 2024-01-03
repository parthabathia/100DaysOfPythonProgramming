from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_operating = True
cafe_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
while machine_operating:
    print("Welcome to PAB coin operated Coffee Service!")
    order = input(f"Kindly select your order? ({cafe_menu.get_items()}): ").lower()
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        machine_operating = False
    else:
        drink = cafe_menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
else:
    print("Sorry to see you go.")
