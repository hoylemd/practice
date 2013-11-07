import argparse
import operator

#function to print out a kmer occurrance list
def print_kmers_list (list):
    for i in list:
        print i,
        print ": ",
        print list[i],
        print " (",
        print len(list[i]),
        print")"

# set up the args parser
parser = argparse.ArgumentParser(description='This is a script to find clumps of k-mers in a genome')
parser.add_argument("file", help="The file to operate on")
args = parser.parse_args()

# open the file and read it
f = open(args.file)
input_lines = f.readlines();

# parse the parameters
genome = input_lines[0][:-1]
params = input_lines[1][:-1].split(" ")
k = int(params[0])
L = int(params[1])
t = int(params[2])

# we have a clump if a k-mer occurs t or more times in a string of length L

# lets perform some analytics on the genome - find all k-mers, and construct a library of their indicies
index = 0
genome_length = len(genome)
kmers = {}

# go over the whole genome and count each kmer
while index < genome_length - k:
    kmer = genome[index:index+k]

    if kmer in kmers:
        kmers[kmer].append(index)
    else:
        kmers[kmer] = [index]
    index += 1

# now find each kmer that ocurred t or more times
frequent_kmers = {}
for i in kmers:
    if len(kmers[i]) >= t:
        frequent_kmers[i] = kmers[i]


# now look at this list of frequent kmers and determine if they are occurring in a region shorter than L
clumps = {}
for i in frequent_kmers:
    index = 0
    occurrances = frequent_kmers[i]
    while index + t <= len(occurrances):
        if occurrances[index + t - 1] - occurrances[index] <= L - k:
            if i in clumps:
                clumps[i] += 1
            else:
                clumps[i] = 1
        index += 1

# now, print out the clumps
'''for i in clumps:
    print i,

print'''

# and of course, the count
print len(clumps)
