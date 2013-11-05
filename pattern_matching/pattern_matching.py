import argparse
import operator

# set up the args parser
parser = argparse.ArgumentParser(description='This is a script to find all positions of a substring in a string')
parser.add_argument("file", help="The file to operate on")
args = parser.parse_args()

# open the file and read it
f = open(args.file)
input_lines = f.readlines()

# extract the data
pattern = input_lines[0][:-1]
string = input_lines[1][:-1]

# initialize data and take come metrics
start_index = 0
matches = []
string_length = len(string)
pattern_length = len(pattern)

# check every possible location for the string
# this is not optimal
while start_index < string_length:
    if string[start_index:start_index + pattern_length] == pattern:
        matches.append(start_index)

    start_index += 1

# print out the matches
for match in matches:
    print match,
