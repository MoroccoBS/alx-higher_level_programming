#!/usr/bin/python3
""" Read stdin line by line and computes metrics """
import sys
import signal

codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
lines = 0


def signal_handler(signal, frame):
    """Handle Ctrl-C"""
    print_metrics()
    raise SystemExit(0)


def print_metrics():
    """Print metrics"""
    print("File size: {}".format(file_size))
    for code in sorted(codes.keys()):
        if codes[code] > 0:
            print("{}: {}".format(code, codes[code]))


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        status_code = parts[-2]
        size = parts[-1]
        if status_code in codes:
            codes[status_code] += 1
        file_size += int(size)
        lines += 1
        if lines % 10 == 0:
            print_metrics()
    except:
        pass


print_metrics()
