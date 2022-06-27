import pandas as pd

name = input("Whats your name?\n")
file = pd.read_csv("nato_phonetic_alphabet.csv")
name_list = [alphabet for alphabet in name.upper()]

for x in range(len(name_list)):
    ans = [f"{row.letter} for {row.code}" for (index, row) in file.iterrows() if row.letter == name_list[x]]
    print(ans[0])
