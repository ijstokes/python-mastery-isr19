#!/usr/bin/env python

print "__name__", __name__
a = 3
b = 7
print a * b
nums = [3, 8, 3, 7, 2, 12, 6, -4]
print sorted(nums)

for n in nums:
    print n**2

print "max:", max(nums)
print "min:", min(nums)
print "sum:", sum(nums)

pos_evens = [ ] # empty list

for n in nums:
    if n > 0 and n%2 == 0:
        pos_evens.append(n)
    
print "positive even values", pos_evens

i        = 0
subtotal = 0
while subtotal < 30:
    subtotal += nums[i]
    i += 1

print subtotal
