file = open('24-3.txt')
text = file.read()
max_subsucsession_length = 0
max_subsucsession_start_index = 0
old_symbol = chr(0)
length = 0
first_symbol_index = 0
index = 0
for symbol in text:
    index += 1
    if symbol >= old_symbol:
        length += 1
    else:
        if length > max_subsucsession_length:
            max_subsucsession_length = length
            max_subsucsession_start_index = first_symbol_index
        first_symbol_index = index
        length = 1
    old_symbol = symbol
print(max_subsucsession_start_index)
