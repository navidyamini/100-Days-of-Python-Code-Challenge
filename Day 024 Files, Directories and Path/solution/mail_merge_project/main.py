starting_letter_path = "Input/Letters/starting_letter.txt"
names_path = "Input/Names/invited_names.txt"
output_path = "Output/ReadyToSend/"
PLACEHOLDER = "[name]"

with open(names_path) as file:
    info = file.read()
    names = info.splitlines()

with open(starting_letter_path) as file:
    starting_letter = file.read()

for name in names:
    letter = starting_letter.replace(PLACEHOLDER, name)
    with open(f"{output_path}letter_for_{name}.txt", mode="w") as file:
        file.write(letter)
