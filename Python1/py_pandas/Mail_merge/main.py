names = []
all_letter_data = []
PLACE_HOLDER = "[name]"
with open("Input/Names/data.txt", mode="r") as file:
    file_data = file.readlines()
for line in file_data:
    word = line.partition("\n")
    names.append(word[0])

with open("Input/Letters/starting_letter.txt", mode="r+") as letter:
    letter_data = letter.read()

    for name in names:
        new_letter = letter_data.replace(PLACE_HOLDER, name)
        with open(f"Output/ReadyToSend/letter_to_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
