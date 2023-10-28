print("Welcome to the tip calculator")
total = int(input("What is the total amount of your bill?  "))
tip = total * int(input("What percentage tip would you like to give?  "))/100
num_of_people = int(input("How many people to split the bill?  "))

amount_per_person = round((total+tip)/num_of_people, 2)

print(f"Amount that needs to be paid per person is {amount_per_person}")
