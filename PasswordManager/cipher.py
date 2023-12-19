alphabet_str = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alphabet_lower = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z".lower()
number_str = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
ALPHABET = alphabet_str.split(", ")
ALPHABET_LOWER = alphabet_lower.split(", ")
NUMBERS = number_str.split(", ")

class Cipher:
	
    def __init__(self, message):
        self.message = message
        self.shift = 0
	
    def encoder(self, shift):
        self.shift = shift
        answer = ""
        for n in self.message:
            if n.isalpha():
                if n.isupper():
                    index = ALPHABET.index(n) + self.shift
                else:
                    index = ALPHABET_LOWER.index(n) + self.shift
                while index > len(ALPHABET)-1:
                    index = index - len(ALPHABET)
                if n.isupper():
                    answer += ALPHABET_LOWER[index]
                else:
                    answer += ALPHABET[index]

            elif n.isnumeric():
                index_n = NUMBERS.index(n) + self.shift
                while index_n > len(NUMBERS)-1:
                    index_n = index_n - len(NUMBERS)
                answer += NUMBERS[index_n]
            else:
                answer += n
        return answer

    def decoder(self, shift):
        self.shift = shift
        answer = ""
        for n in self.message:
            if n.isalpha():
                if n.isupper():
                    index = ALPHABET.index(n) - self.shift
                else:
                    index = ALPHABET_LOWER.index(n) - self.shift
                while index  < 0 and (len(ALPHABET)-1) + index < 0:
                    index = (len(ALPHABET)) + index
                if n.isupper():
                    answer += ALPHABET_LOWER[index]
                else:
                    answer += ALPHABET[index]

            elif n.isnumeric():
                index_n = NUMBERS.index(n) - self.shift
                while index_n < 0 and (len(NUMBERS)-1) + index_n < 0:
                    index_n = (len(NUMBERS)) + index_n
                answer += NUMBERS[index_n]
            else:
                answer += n
        return answer

