import argparse
import operator

# set up the args parser
parser = argparse.ArgumentParser(description='search a string for the most common substring of length k')
parser.add_argument("file", help="The file to perform analysis on")
args = parser.parse_args()

#read the file
f = open(args.file)
lines = f.readlines()

# initialize things
string = lines[0]
k = int(lines[1])
kmers = {}

# count the occurrances of all substrings of length k
for i in range(0, len(string) - k):
    # get the next k-mer
    kmer = string[i:i+k]

    # count it
    if kmer in kmers:
        kmers[kmer] += 1
    else:
        kmers[kmer] = 1

# sort the list
kmers_ordered = sorted(kmers.iteritems(), key=operator.itemgetter(1))
kmers_ordered.reverse()

# determine highest frequency
max_frequency = kmers_ordered[0][1]

# make a list of all most frequent kmers
frequent_kmers = []
current_frequency = max_frequency
i = 0
while current_frequency == max_frequency:
    frequent_kmers.append(kmers_ordered[i][0])
    i += 1
    current_frequency = kmers_ordered[i][1]

# sort this list
frequent_kmers.sort()

# print out the most frequent kmers
for kmer in frequent_kmers:
    print kmer,
