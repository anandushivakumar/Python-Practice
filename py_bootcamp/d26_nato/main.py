import pandas

alphabet_df = pandas.read_csv(r"py_bootcamp\d26_nato\nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}

# ask user for word
user_input = input("Enter a word: ").upper()

output = [alphabet_dict[l] for l in user_input]
print(output)