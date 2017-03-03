#! /usr/bin/env python
# encoding=utf-8


# Ascii表：
# 数字范围为：48—57
# 大写字母范围为：65—90
# 小写字母范围为：97—122

# ascii表中，打印出一串字符串，仅包含大写字母和小写字母与数字

a = ''

for i in range(65,91):
    a = a + chr(i)

for i in range(97,123):
    a = a + chr(i)

for i in range(48,58):
    a = a + chr(i)

print a