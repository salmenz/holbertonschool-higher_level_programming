#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    la = len(argv)
    if la == 1:
        print('{} arguments.'.format(la - 1))
    elif la == 2:
        print('{} argument:'.format(la - 1))
    else:
        print('{} arguments:'.format(la - 1))
    for i in range(1, la):
        print('{:d}: {:s}'.format(i, argv[i]))
