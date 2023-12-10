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
- Contain at least 2 non-alphabetical characters (e.g., numbers of special characters)
'''
ALPHABET = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
ALPHABET = ALPHABET.split(", ")
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
LENGTH_PASSWORD = 15
MIN_LETTERS = 2
MIN_NUMBERS = 0
MIN_SYMBOLS = 2

class Password():
    def __init__(self, entry_widget):
        self.password = ''
        self.widget = entry_widget

    def generator(self):
        self.password = ""

        for n in range(LENGTH_PASSWORD):
            rand_value = random.randint(0,2)
            if rand_value == 0:
                value = ALPHABET[random.randint(0, len(ALPHABET)-1)]
                rand_case = random.randint(0, 1)
                if rand_case == 0:
                    value = value.lower()
            elif rand_value == 1:
                value = NUMBERS[random.randint(0, len(NUMBERS)-1)]
            else:
                value = SYMBOLS[random.randint(0, len(SYMBOLS)-1)]
            self.password += value

        self.widget.delete(0, 'end')
        self.widget.insert(0, self.password)


    def verify(self):
        min_num_letters = MIN_LETTERS
        min_num_numbers = MIN_NUMBERS
        min_num_symbols = MIN_SYMBOLS

        password_list = [l for l in self.password]
        for l in password_list:
            if l.isalpha() and l.upper() in ALPHABET:
                min_num_letters -= 1
            elif l in NUMBERS:
                min_num_numbers -= 1
            else:
                min_num_symbols -= 1

        if min_num_letters <= 0 and min_num_numbers <= 0 and min_num_symbols <= 0:
            return True
        else:
            return False
    
    def set_password(self):
        self.password = self.widget.get()
