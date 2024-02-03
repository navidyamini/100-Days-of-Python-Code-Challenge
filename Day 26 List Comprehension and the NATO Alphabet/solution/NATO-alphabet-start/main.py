import pandas as pd

# Read csv as pandas dataframe
nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
# Cconvert dataframe to dictionary
nato_alphabet_dic = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}
# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
# Search for each letter in dictionary and extract the value
output = [nato_alphabet_dic[letter] for letter in user_input]
print(output)
