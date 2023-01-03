import oop_menu
import oop_coffee_maker
import oop_money_machine

# Create the necessary objects.
menu = oop_menu.Menu()
coffee_maker = oop_coffee_maker.CoffeeMaker()
money_machine = oop_money_machine.MoneyMachine()
# Create a list of the menu items.
options = menu.get_items()
# Create a variable to toggle the coffee machine off.
is_on = True

while is_on:
    choice = input(f'What would you like? ({options}): ').lower()

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report = coffee_maker.report()

        print(report)
    else:
        # Searches the menu for a particular drink by name.
        # Returns a MenuItem object if exists, otherwise returns None.
        drink = menu.find_drink(choice)
        # Returns True when the drink order can be made.
        # Returns False if ingredients are insufficient.
        if coffee_maker.is_resource_sufficient(drink):
            cost = drink.cost
            # Returns True when payment is accepted, or False if insufficient.
            if money_machine.make_payment(cost):
                # Deducts the required ingredients from the resources.
                coffee_maker.make_coffee(drink)