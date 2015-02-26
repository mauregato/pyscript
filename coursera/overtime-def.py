#!/usr/bin/env python
def computepay(h, r):
    if h <= 40:
        p = r * h
    else:
        normal = 40 * r
        extra = ((h-40) * 1.5) * r
        p = normal+extra
    return p
    
    

try:
    inp = raw_input("Enter Hours: ")
    hours = float(inp)
    inp = raw_input("Enter Rate: ")
    rate = float(inp)
except:
    print "Error, plase numeric input"
    quit()

pay = computepay(hours, rate)
print pay
