#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as html:
        res = html.read()
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
    print("\t- utf8 content: {}".format(res.decode(encoding="utf-8")))
