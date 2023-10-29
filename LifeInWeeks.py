print("Optimistically most humans can live up to 90 years which equals to around 4680 weeks.")
print("This calculator will help you find out how many weeks you have left.\n")

age = int(input("What is your age?"))

time_left = 90 - age
weeks_left = time_left*52

print("You have {weeks_left} weeks left.")
print("Spend your time wisely!")