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

minimum_skew = 0
minimum_locations = []

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

# check teh skew for each prefix
for i in range(0, len(genome) + 1):
    current_skew = skew(genome[:i])
    if i % 50 == 0:
        print (float(i) / float(len(genome)))

    # start a new minimum list if a new minimum has been found
    if current_skew < minimum_skew:
        minimum_skew = current_skew
        minimum_locations = [ i ]

    # if this location has the same skew as the minimum, add it to the list
    elif current_skew == minimum_skew:
        minimum_locations.append(i)

print "Done!"
# print out the minimums
for location in minimum_locations:
    print location,
