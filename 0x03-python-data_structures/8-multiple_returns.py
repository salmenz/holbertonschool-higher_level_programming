#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        res = None
    else:
        res = sentence[0]
    return len(sentence), res
