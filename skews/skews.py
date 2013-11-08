import argparse
import operator

# set up the args parser
parser = argparse.ArgumentParser(description='This is a script to print out the skew value for each nucleotide in a genome.')
parser.add_argument("file", help="The file to operate on")
args = parser.parse_args()

# open the file and read it
f = open(args.file)
input_lines = f.readlines();

genome = input_lines[0][:-1]

# function to calculate the G-C skew of a genome
def skew(genome):
    skew = 0
    for nucleotide in genome:
        # subtract 1 for C, add one for G
        if nucleotide == "C":
            skew -= 1
        elif nucleotide == "G":
            skew += 1

    return skew

# calculate the skew for each prefix
for i in range(0, len(genome) + 1):
    print skew(genome[:i]),
