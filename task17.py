text = input('Text: ')
length = int(input('Length: '))

result = text.rjust(length, '0')

print(result)