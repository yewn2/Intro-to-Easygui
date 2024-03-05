string = "The coordinates you require are xyz"
string_list = list(string)
letters_to_remove = "xyz"
position = (string.find(letters_to_remove))
for char in range(len(letters_to_remove)):
    string_list.pop(position)
string_list = ''.join(string_list)
print(string_list)
