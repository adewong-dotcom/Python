from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

running = True

while running:
# TODO 1: Get User input
    user_answer = input("What would you like? (espresso/ latte/cappuccino/):").lower()

# TODO 2: Turn off if 'off' is input
    if user_answer == 'off':
        running = False
        continue

# TODO 3: Return report if 'report' is input
    elif user_answer == 'report':
        coffee_maker.report()
        money_machine.report()
        continue

# TODO 4: Check if there are sufficient resources
    else:
        item = menu.find_drink(user_answer)
        if item is None:
            continue
        else:
            sufficient_resources = coffee_maker.is_resource_sufficient((item))

        if not sufficient_resources:
            continue

# TODO 5: Process coins
# TODO 6: Verify that coins are sufficient for transaction.
# Print 'Here is $2.45 in change.' if sufficient and complete transaction.
    cost = item.cost
    valid_transaction = money_machine.make_payment(cost)

# TODO 7: Make coffee and print 'Here is your {drink}. Enjoy!'
    if valid_transaction:
        coffee_maker.make_coffee(item)

