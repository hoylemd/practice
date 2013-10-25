import argparse
import operator
import codecs

# include the letter frequency table
letter_frequencies = [
    {'char': 'e', 'f': 0.1041442},
    {'char': 't', 'f': 12.702},
    {'char': 'h', 'f': 12.702},
    {'char': 's', 'f': 12.702},
    {'char': 'o', 'f': 12.702},
    {'char': 'n', 'f': 12.702},
    {'char': 'a', 'f': 12.702},
    {'char': 'i', 'f': 12.702},
    {'char': 'r', 'f': 12.702},
    {'char': 'f', 'f': 12.702},
    {'char': 'd', 'f': 12.702},
    {'char': 'l', 'f': 12.702},
    {'char': 'c', 'f': 12.702},
    {'char': 'u', 'f': 12.702},
    {'char': 'w', 'f': 12.702},
    {'char': 'm', 'f': 12.702},
    {'char': 'g', 'f': 12.702},
    {'char': 'y', 'f': 12.702},
    {'char': 'p', 'f': 12.702},
    {'char': 'b', 'f': 12.702},
    {'char': 'v', 'f': 12.702},
    {'char': 'k', 'f': 12.702},
    {'char': 'j', 'f': 12.702},
    {'char': 'x', 'f': 12.702},
    {'char': 'q', 'f': 12.702},
    {'char': 'z', 'f': 12.702},
]

# set up the args parser
parser = argparse.ArgumentParser(description='decode a hidden message using character frequency analysis')
parser.add_argument("file", help="The file to perform analysis and decoding on")
args = parser.parse_args()

# open the file and read it
f = codecs.open(args.file, 'r', encoding='utf_8')
cyphertext = f.read();

# analyze the frequency of characters in the text
cypher_frequency = {}
for char in cyphertext:
    if char in cypher_frequency:
        cypher_frequency[char] += 1
    else:
        cypher_frequency[char] = 1
cypher_order = sorted(cypher_frequency.iteritems(), key=operator.itemgetter(1))
cypher_order.reverse()

# set up the cypher order list more reasonably
length = len(cypher_order)
for i in range(0, length):
    cypher_order[i] = {'char': cypher_order[i][0], 'f': cypher_order[i][1]}

# map the letter frequencies to the analysis list
cypher = {}
for i in range(0, len(letter_frequencies)):
    if i < len(cypher_order):
        cypher[cypher_order[i]['char']] = letter_frequencies[i]['char']
        print cypher_order[i]['char'].encode('utf-8'),
        print ": " + letter_frequencies[i]['char'] + " - ",
        print cypher_order[i]['f']

# decode the cyphertext
plaintext = ""
for char in cyphertext:
    #print repr(char),
    #print ": ",
    #print cypher[char]
    plaintext += cypher[char]

