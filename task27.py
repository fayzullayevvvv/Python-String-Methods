doc = input('Document: ')

if doc.endswith('.pdf') or doc.endswith('.docx') or doc.endswith('.txt'):
    print(True)
else:
    print(False)