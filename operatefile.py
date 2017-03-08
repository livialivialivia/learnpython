#! /usr/bin/env python
# encoding=utf-8
try:
    f = open('data1','r')
    print f.read()
finally:
    if f:
        f.close()