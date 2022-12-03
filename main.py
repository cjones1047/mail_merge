# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt

cleaned_names_list = []

with open("Input/Names/invited_names.txt", mode="r") as all_names:
    names_list = all_names.readlines()
    for name in names_list:
        cleaned_names_list.append(name.strip())
    print(cleaned_names_list)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

for name in cleaned_names_list:
    named_letter_list = []
    with open("Input/Letters/starting_letter.txt", mode="r") as letter_template:
        template_list = letter_template.readlines()
        template_list[0] = f"Dear {name},\n"
        for line in template_list:
            named_letter_list.append(line)
    print(named_letter_list)
    #     # with open(f"Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
    #     #     for l
