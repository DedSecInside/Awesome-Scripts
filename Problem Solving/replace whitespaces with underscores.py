import re


Input = input("Please enter a string: ")
def replace_white_spaces_with_underscores(input_string):
    list_input = list(input_string)
    final_string = " "
    white_spaces = []
    for match in re.finditer('\s', input_string):
        white_spaces.append(match.start())

    for i in range(len(white_spaces)):
        list_input[white_spaces[i]] = "_"
    return final_string.join(list_input)

print(replace_white_spaces_with_underscores(Input))
