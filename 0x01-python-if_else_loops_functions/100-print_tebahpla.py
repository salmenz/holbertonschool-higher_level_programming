#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        t = 0
    else:
        t = 1
    print("{:s}".format(chr(i - (t * 32))), end="")
