#! /usr/bin/env python
# encoding=utf-8

class Animals(object):
    def run(self):
        print 'Animal is running.....'

class Dog(Animals):
    def run(self):
        print 'Dog is running....'

class Cat(Animals):
    def run(self):
        print 'Cat is running.....'


def run_twice(animal):
    animal.run()
    animal.run()

a = Animals()
d = Dog()
c = Cat()

print 'a is Animal?',isinstance(a,Animals)
print 'a is Dog?',isinstance(a,Dog)
print 'a is Cat?',isinstance(a,Cat)

print 'd is Animal?',isinstance(d,Animals)
print 'd is Dog?',isinstance(d,Dog)
print 'd is Cat?',isinstance(d,Cat)

run_twice(c)