text = input('Text: ')
length = int(input('Length: '))

result = text.ljust(length, '0')

print(result)