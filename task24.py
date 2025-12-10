text = input('Text: ')

result = text.startswith('@') != True and text.endswith('.com') == True

print(result)