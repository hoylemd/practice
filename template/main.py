import argparse
import operator

# set up the args parser
parser = argparse.ArgumentParser(description='This is a python script')
parser.add_argument("file", help="The file to operate on")
args = parser.parse_args()

# open the file and read it
f = open(args.file)
input_lines = f.readlines();

print input_lines


