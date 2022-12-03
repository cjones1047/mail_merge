# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt

with open("Input/Names/invited_names.txt", mode="r") as all_names:
    names_list = all_names.readlines()
    cleaned_names_list = []
    for name in names_list:
        cleaned_names_list.append(name.strip())
    print(cleaned_names_list)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
