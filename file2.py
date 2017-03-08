#! /usr/bin/env python
# encoding=utf-8

with open('data1','w') as f:
    print f.write('hello,world')

with open('data1','r') as f:
    print f.read()