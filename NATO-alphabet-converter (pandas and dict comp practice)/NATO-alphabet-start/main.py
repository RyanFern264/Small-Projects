import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#{"A": "Alfa", "B": "Bravo"}
# # this is equivalent to the dict comprehension below it
# for(index, row) in df.iterrows():
#     print(row.letter)
#     print(row.code)

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    user_word = input("Type your word: ").upper()  # turning the user input into a list of uppercased letters
    try:
        user_code_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(user_code_list)

generate_phonetic()