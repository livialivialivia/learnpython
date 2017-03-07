#! /usr/bin/env python
# encoding=utf-8

class Student(object):
    __slots__=('name','age')

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Livia'
s.age = 18

try:
    s.score = 99
except AttributeError as e:
    print 'AttributeError:',e

g = GraduateStudent()
g.score=99
print 'g.score = ',g.score