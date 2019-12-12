#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 1:
        print('{} arguments.'.format(l - 1))
    elif l == 2:
        print('{} argument:'.format(l - 1))
    else:
        print('{} arguments:'.format(l - 1))
    for i in range(1,l):
        print('{:d}: {:s}'.format(i, argv[i]))
