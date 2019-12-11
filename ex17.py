from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# could combine the bottom two
in_file = open(from_file)
indata = in_file.read()

print(f"The input file {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")

print("If ready, hit Enter to continue")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('okay, all done')

out_file.close()
in_file.close()
