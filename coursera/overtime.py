#!/usr/bin/env python
hrs = raw_input("Enter Hours: ")
h = float(hrs)
inp = raw_input("Enter rate: ")
rate = float(inp)
print rate, h
if h <= 40:
    pay = rate * h
    print pay
else:
    normal = 40 * rate
    extra = ((h-40) * 1.5) * rate
    pay = normal+extra
    print pay
