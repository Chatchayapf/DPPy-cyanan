#!/usr/bin/python3

#Cell 5-3 - Python

oriArray = [2, 8, 9, 48, 8, 22, -12, 2]
newArray = []

for num in oriArray:
    if num > 5:
        newArray.append(num+2)

new = set(newArray)

print(oriArray)
print(new)