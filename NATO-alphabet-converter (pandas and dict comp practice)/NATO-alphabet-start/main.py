import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
# # this is equivalent to the dict comprehension below it
# for(index, row) in df.iterrows():
#     print(row.letter)
#     print(row.code)

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Type your word: ").upper()# turning the user input into a list of uppercased letters
#later removed the wrapping list() in the above line as it is not needed
user_code_list = [phonetic_dict[letter] for letter in user_word]
print(user_code_list)
