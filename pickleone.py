#! /usr/bin/env python
# encoding=utf-8
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob',age=20,score=88)

f = open('dump.txt','wb')
pickle.dumps(d,f)
f.close()

f =  open('dump.txt','wb')
f.read()
f.close()
