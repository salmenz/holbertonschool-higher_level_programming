#!/usr/bin/python3
def uppercase(str):
	for i in str:
		if 123 > ord(i) > 96:
			i = chr(ord(i) - 32)
		print('{}'.format(i), end="")
	print('')
