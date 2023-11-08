#!/usr/bin/python3

import sys
import collections

status_code_counts = collections.defaultdict(int)
total_size = 0

for line in sys.stdin:

    line_data = line.split()

    status_code = int(line_data[3])

    status_code_counts[status_code] += 1
    total_size += int(line_data[4])

    if len(status_code_counts) % 10 == 0:
        print("File size:", total_size)
        for status_code, count in status_code_counts.items():
            print(status_code, ":", count)

try:
    while True:
        print("File size:", total_size)
        for status_code, count in status_code_counts.items():
            print(status_code, ":", count)
except KeyboardInterrupt:
    pass
