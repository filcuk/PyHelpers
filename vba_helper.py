import re
import sys

print('VBA split delimited string in code\n\n')

# Get input
#string = input("Insert single-line string list to break down:")
print('Insert string and confirm with CTRL+D:')
string = sys.stdin.read()
delimiter = input("Insert delimiter to split the string by:")

# Clean up the string
string = string.replace('"', '')
string = string.replace('\n', '')
string = string.replace(' & _', '')
string = re.sub(' +', ' ', string)

# Split it
arr = string.split(delimiter)
string = '"' + '," & _\n"'.join(arr) + '"'

print(string)
