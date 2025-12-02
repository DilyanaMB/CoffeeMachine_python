from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
should_continue = True
menu = Menu()

while should_continue:
    options =menu.get_items()
    print(f'What would you like? ({options}):')
    user_input = input().lower()

    if user_input == 'off':
        should_continue = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if  money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
