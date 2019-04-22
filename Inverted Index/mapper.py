#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter = "\t")

for line in reader:
    if len(line) == 19:
        data = (line[0], line[4])
        node_id, body = data
        count = 0
        body = re.split("\W+", body)
	for word in body:
	    if word.lower() == "fantastically":
		count += 1
        print "{0}\t{1}".format(node_id, count)
    
