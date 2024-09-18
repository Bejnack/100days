# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

nato_alphabet_raw = pandas.read_csv(r'100DaysofPython\Intermediate\11_List_Comprehension\NATO-alphabet-start\nato_phonetic_alphabet.csv')

nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet_raw.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input('Enter a name: ').upper()
nato_name = [nato_alphabet_dict[letter] for letter in name.upper() if letter in nato_alphabet_dict]
print(nato_name)
