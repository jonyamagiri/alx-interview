#!/usr/bin/python3
""" module 0-stats.py that reads stdin line by line and computes metrics """

import sys


if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """Print the file size and number of lines per status code"""
        print("File size: {:d}".format(filesize))
        for code, count in sorted(stats.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            if len(data) < 7:
                continue  # Skip invalid lines
            status_code = data[-2]
            if status_code in stats:
                stats[status_code] += 1
            try:
                filesize += int(data[-1])
            except ValueError:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
