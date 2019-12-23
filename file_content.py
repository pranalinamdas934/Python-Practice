filename = input('enter file name: ').strip()

content = input('enter file contents: ')
with open(filename, 'a+') as file:
    file.write(content)