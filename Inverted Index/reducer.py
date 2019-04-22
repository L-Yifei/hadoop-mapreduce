#!/usr/bin/python

import sys

total_count = 0
id_list = []
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_id, this_count = data_mapped[0], int(data_mapped[1])

    if this_count > 0:
	total_count = total_count + this_count
	id_list.append(this_id)
        print this_id, "\t", this_count
id_list.sort()
print "ID list: ", id_list
print "Total count:", total_count
