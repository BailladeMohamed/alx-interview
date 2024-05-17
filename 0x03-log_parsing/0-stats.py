#!/usr/bin/python3
import sys
import signal

"""Initializing the variables"""
in_total = 0
code_st = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_stats():
    print("File size: {}".format(in_total))
    for code in sorted(code_st.keys()):
        if code_st[code] > 0:
            print("{}: {}".format(code, code_st[code]))


def handler_s(sig, frame):
    print_stats()
    sys.exit(0)


"""Handling the signal"""
signal.signal(signal.SIGINT, handler_s)

try:
    for i, line in enumerate(sys.stdin, 1):
        try:
            data = line.split()
            size = data[-1]
            status_code = data[-2]
            in_total += int(size)
            if status_code in code_st:
                code_st[status_code] += 1
        except Exception as e:
            pass
        if i % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
