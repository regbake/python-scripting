from sys import argv

script, filename = argv

print(f'going to erase {filename}')
print('if you do not want that then ^C')
print(f"if  you do want that then hit Enter")

input(">>? ")

print('Opening the file...')
target = open(filename, 'w')

print('truncating the file. later')
target.truncate()

print("enter three lines")

line1 = input('line1: ')
line2 = input('line2: ')
line3 = input('line3: ')

print("let's add these lines to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("closing...")

target.close()

