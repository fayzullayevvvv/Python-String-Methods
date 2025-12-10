text = input('Text: ')

clean_text = text.replace('-', '')
result = clean_text.isalnum()

print(result)