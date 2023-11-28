#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

file = open("Mail Merge Project/Input/Letters/starting_letter.txt", mode="r")
content = file.read()
names_file = open("Mail Merge Project/Input/Names/invited_names.txt", mode="r")
names = names_file.readlines()

for name in names:
    temp_name = name.strip()
    temp_file = content.replace("[name]", temp_name)
    print(temp_file)
    with open(f"Mail Merge Project/Output/ReadyToSend/Letter_for_{temp_name}.txt", mode="w") as doc:
        doc.write(temp_file)
file.close()
names_file.close()