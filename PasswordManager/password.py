import random

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
MIN_LETTERS = 2
MIN_NUMBERS = 0
MIN_SYMBOLS = 2

class Password():
    def __init__(self, password=""):
        self.password = password

    def generator(self):
        self.password = ""
        for n in range(15):
            pass


    def verify(self):
        min_num_letters = 3
        min_num_numbers = 3
        min_num_symbols = 2

        password_list = [l for l in self.password]
        for l in password_list:
            if l.upper() in ALPHABET:
                min_num_letters -= 1
            elif l in NUMBERS:
                min_num_numbers -= 1
            else:
                min_num_symbols -= 1

        if min_num_letters <= 0 and min_num_numbers <= 0 and min_num_symbols <= 0:
            return True
        else:
            return False