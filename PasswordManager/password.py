import random
from typing import Any

''''
Enables user to create HawkID password with the following rules:
- Not be the same as your previous 10 HawkID passwords
- Not be similar to your current HawkID password
- Not be similar to your HawkID login name
- Not be similar to your actual name
- Contain at least 15 characters
- Contain at least 2 alphabetical characters
- Contain at least 2 non-alphabetical characters (e.g., NUMBERS of special characters)
'''
ALPHABET = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
ALPHABET = ALPHABET.split(", ")
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
LENGTH_PASSWORD = 15
MIN_ALPHABET = 8
MIN_NUMBERS = 4
MIN_SYMBOLS = 3

class Password():
    def __init__(self, entry_widget):
        self.password = ''
        self.widget = entry_widget

    def generator(self):
        self.password = ""

        # for n in range(LENGTH_PASSWORD):
        #     rand_value = random.randint(0,2)
        #     if rand_value == 0:
        #         value = ALPHABET[random.randint(0, len(ALPHABET)-1)]
        #         rand_case = random.randint(0, 1)
        #         if rand_case == 0:
        #             value = value.lower()
        #     elif rand_value == 1:
        #         value = NUMBERS[random.randint(0, len(NUMBERS)-1)]
        #     else:
        #         value = SYMBOLS[random.randint(0, len(SYMBOLS)-1)]
        #     self.password += value

        nr_digits = MIN_ALPHABET + MIN_NUMBERS + MIN_SYMBOLS
        nr_ALPHABET = MIN_ALPHABET
        nr_numbers = MIN_NUMBERS
        nr_symbols = MIN_SYMBOLS

        password_hard = []
        for num in range(0, nr_digits):
            if nr_ALPHABET > 0 and nr_numbers > 0 and nr_symbols > 0:
                rand_digit = random.choice([ALPHABET, SYMBOLS, NUMBERS])
                rand_value = random.choice(rand_digit)
                if rand_value.isalpha():
                    rand_case = random.randint(0, 1)
                    if rand_case == 0:
                        rand_value = rand_value.lower()
                    nr_ALPHABET -= 1
                elif rand_value.isnumeric():
                    nr_numbers -= 1
                else:
                    nr_symbols -= 1
                password_hard.append(rand_value)
            elif nr_ALPHABET > 0 and nr_numbers > 0:
                rand_digit = random.choice([ALPHABET, NUMBERS])
                rand_value = random.choice(rand_digit)
                if rand_value.isalpha():
                    rand_case = random.randint(0, 1)
                    if rand_case == 0:
                        rand_value = rand_value.lower()
                    nr_ALPHABET -= 1
                else:
                    nr_numbers -= 1
                password_hard.append(rand_value)
            elif nr_ALPHABET > 0 and nr_symbols > 0:
                rand_digit = random.choice([ALPHABET, SYMBOLS])
                rand_value = random.choice(rand_digit)
                if rand_value.isalpha():
                    rand_case = random.randint(0, 1)
                    if rand_case == 0:
                        rand_value = rand_value.lower()
                    nr_ALPHABET -= 1
                else:
                    nr_symbols -= 1
                password_hard.append(rand_value)
            elif nr_numbers > 0 and nr_symbols > 0:
                rand_digit = random.choice([NUMBERS, SYMBOLS])
                rand_value = random.choice(rand_digit)
                password_hard.append(rand_value)
                if rand_value.isnumeric():
                    nr_numbers -= 1
                else:
                    nr_symbols -= 1
            elif nr_numbers > 0:
                rand_value = random.choice(NUMBERS)
                password_hard.append(rand_value)
                nr_numbers -= 1
            elif nr_ALPHABET > 0:
                rand_value = random.choice(ALPHABET)
                rand_case = random.randint(0, 1)
                if rand_case == 0:
                    rand_value = rand_value.lower()
                password_hard.append(rand_value)
                nr_ALPHABET -= 1
            else:
                rand_value = random.choice(SYMBOLS)
                password_hard.append(rand_value)
                nr_symbols -= 1
            
        password_hard = ''.join(password_hard)
        self.password = password_hard

        self.widget.delete(0, 'end')
        self.widget.insert(0, self.password)


    def verify(self):
        min_num_ALPHABET = MIN_ALPHABET
        min_num_numbers = MIN_NUMBERS
        min_num_symbols = MIN_SYMBOLS

        password_list = [l for l in self.password]
        for l in password_list:
            if l.isalpha() and l.upper() in ALPHABET:
                min_num_ALPHABET -= 1
            elif l in NUMBERS:
                min_num_numbers -= 1
            else:
                min_num_symbols -= 1

        if min_num_ALPHABET <= 0 and min_num_numbers <= 0 and min_num_symbols <= 0:
            return True
        else:
            return False
    
    def set_password(self):
        self.password = self.widget.get()
