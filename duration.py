'''
this script is a bond duration calculator because I cba 
to do it all by hand for homeworks
'''

import math

Ct = int(input("Enter the coupon value: ")) # coupon value
r = float(input("Enter the rate (Apr): ")) # apr
t0 = int(input("enter the time: ")) # time period
p0 = float(input("enter the p0 value: ")) # p0 
 
total = 0
end = t0 + 1

for t in range(1,end):
    if t == (end-1):
        Ct += p0
    denom = math.pow((1 + r), t)
    block = (Ct / denom) * t
    total += block

duration = total / p0
print(f"The duration is: {duration} years ")

