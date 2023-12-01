import pandas as pd
import time

name = input("What is your name? : ").upper()
letters = [letter for letter in name]
nato_df = pd.read_csv("NATO_transformer/nato_phonetic_alphabet.csv")
start = time.perf_counter()
nato_name = [row.code for letter in letters for (index, row) in nato_df.iterrows() if row.letter == letter]
end = time.perf_counter()
# for letter in letters:
#     for (index, row) in nato_df.iterrows():
#         if row.letter == letter:
#             nato_name.append(row.code)
elapsed_time = (end - start) * 10**6
print(nato_name)
print(f"Took {elapsed_time} ms to run")
#Can't be run with spaces
start = time.perf_counter()
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
nato_answer = [nato_dict[letter] for letter in letters]
end = time.perf_counter()
elapsed_time = (end - start) * 10**6
print(nato_answer)
print(f"Took {elapsed_time} ms to run")