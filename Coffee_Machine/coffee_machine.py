from coffee_machine_data import COFFEES
from coffee_machine_art import logo

resources = {
	"Water" : 600,
	"Milk" : 400,
	"Coffee" : 200,
	"Money" : 0
}
measure = ["ml", "g", "$"]

#Function to process coins given
def process_coins(quarters=0, dimes=0, nickels=0, pennies=0):
	''' 
	Gets the quarters, dimes, nickels and pennies and returns its sum.
	parameters are set to 0 by default
	'''
	total = (quarters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01)
	return total


#Function to verify coins were suficient and we had enough resources
def transaction(drink, resources):
	'''
	Takes the beverage type and resources and updates the resources accordingly
	'''
	ingredients = drink['ingredients']
	for ingredient in ingredients:
		resources[ingredient] -= ingredients[ingredient]
	resources["Money"] += drink["cost"]


#Function to verify that we have enough resources
def resource_checker(drink, resources):
	'''Takes a dictionary with the type of drink and checks resources dictionary to make
	sure there is enough. Return True if there is and False with printed error message.
	'''
	ingredients = drink['ingredients']
	for ingredient in ingredients:
		if resources[ingredient] < ingredients[ingredient]:
			print(f"Sorry there is not enough {ingredient.lower()}.")
			return False
	return True


#Function to print resources available
def report(resources, measure):
	for key in resources.keys():
		if key == "Water" or key == "Milk":
			print(f"{key}:  {resources[key]}{measure[0]}")
		elif key == "Coffee":
			print(f"{key}:  {resources[key]}{measure[1]}")
		else:
			print(f"{key}:  {measure[2]}{resources[key]}")

print(logo)

running = True
#main part
while running:
	type_coffee = input("What would you like? (espresso/ latte/ cappuccino):  ").lower()
	if type_coffee == "off":
		running = False
		money = resources["Money"]
		print(f"We made ${money}.")
		continue
	elif type_coffee == "report":
		report(resources, measure)
	elif type_coffee == "espresso" or type_coffee == "latte" or type_coffee == "cappuccino":
		drink = COFFEES[type_coffee]
		if not resource_checker(drink, resources):
			continue

		cost = drink["cost"]
		print(f"That would be: ${cost}")
		getting_money = True
		quarters = 0
		dimes = 0
		nickels = 0
		pennies = 0

		while getting_money:
			print("Please insert coins.")
			try:
				quarters = int(input("How many quarters?: "))
				dimes = int(input("How many dimes?: "))
				nickels = int(input("How many nickels?: "))
				pennies = int(input("How many pennies?: "))
				getting_money = False
			except ValueError:
				print("That is not a valid response.")

		money_given = process_coins(quarters, dimes, nickels, pennies)
		if money_given < cost:
			print("Sorry that's not enough money. Money refunded.")
			continue

		change = round(money_given - drink['cost'], 2)
		if change == 0:
			print("That was the exact amount.")
		else:
			print(f"Here is ${change} dollars in change.")

		transaction(drink, resources)
		
		print(f"Here is your {type_coffee}. Enjoy!")

	else:
		print("That is not a valid option.")


