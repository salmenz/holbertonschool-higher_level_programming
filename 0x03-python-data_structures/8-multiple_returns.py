#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        res = None
    else:
        res = sentence[0]
    return len(sentence), res
