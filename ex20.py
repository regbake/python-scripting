from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	line_has_content = len(f.readline()) > 0

	if line_has_content:
		print(line_count, f.readline())
	else:
		print(line_count, "has no content")

current_file = open(input_file)

print("First, here's the whole file: \n")

print_all(current_file)

print("Let's rewind")

rewind(current_file)

print("Print three lines...: ")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
