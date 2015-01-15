#!/usr/bin/python
import random, argparse, os

parser = argparse.ArgumentParser(description='Script to randomize the lines in a file and then pick one randomly.')
parser.add_argument('-i','--input', help='Input file name',required=True)
args = parser.parse_args()

with open(args.input,'r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('randomfile','w') as target:
    for _, line in data:
        target.write( line )

with open('randomfile') as f:
    lines = random.sample(f.readlines(),1)

print "================================="
print "\n"
print "The randomly selected winner is: " 
print(", ".join(lines)) 
print "================================="

os.remove('randomfile')
