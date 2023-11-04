from caesar_cipher_art import logo

print(logo)

alphabet_str = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z".lower()
number_str = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
alphabet_list = alphabet_str.split(", ")
number_str_list = number_str.split(", ")

def encoder(message, shift):
	answer = ""
	for n in message:
		if n.isalpha():
			index = alphabet_list.index(n) + shift_num
			while index > len(alphabet_list)-1:
				index = index - len(alphabet_list)
			answer += alphabet_list[index]

		elif n.isnumeric():
			index_n = number_str_list.index(n) + shift_num
			while index_n > len(number_str_list)-1:
				index_n = index_n - len(number_str_list)
			answer += number_str_list[index_n]
		else:
			answer += n
	return answer

def decoder(message, shift):
	answer = ""
	for n in message:
		if n.isalpha():
			index = alphabet_list.index(n) - shift_num
			while index  < 0 and (len(alphabet_list)-1) + index < 0:
				index = (len(alphabet_list)) + index
			answer += alphabet_list[index]

		elif n.isnumeric():
			index_n = number_str_list.index(n) - shift_num
			while index_n < 0 and (len(number_str_list)-1) + index_n < 0:
				index_n = (len(number_str_list)) + index_n
			answer += number_str_list[index_n]
		else:
			answer += n
	return answer

working = True
while working:
	encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

	if encode_decode != "encode":
		if encode_decode != 'decode':
			print("Enter a valid response.")
			continue

	message = input("Type your message:\n").lower()
	getting_shift = True
	while getting_shift:
		shift_num = input("Type the shift number:\n")
		if shift_num.isnumeric() and int(shift_num) <= 1000000: 
			shift_num = int(shift_num)
			break
		else:
			print("Shift can only be a number from 0 to 1,000,000. (Without any additional characters such as commas.)\n Please input a valid number.")

	response = ""
	if encode_decode == 'encode':
		response = encoder(message=message, shift=shift_num)

		print(f"Here's the encoded result:  {response}")
	else:
		response = decoder(message=message, shift=shift_num)

		print(f"Here's the encoded result:  {response}")
	while working:
		continue_working = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
		if continue_working != 'yes' and continue_working != 'no':
			print("That is not a valid response.")
			continue
		elif continue_working == 'no':
			working = False
		else:
			break