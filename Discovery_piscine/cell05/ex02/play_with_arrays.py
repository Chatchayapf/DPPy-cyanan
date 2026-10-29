#!/usr/bin/python3

#Cell 5-2 - Python

oriArray = [2, 8, 9, 48, 8, 22, -12, 2]
newArray = []

for num in oriArray:
    if num > 5:
        newArray.append(num+2)

print("Original array:", oriArray)
print("New array:", newArray)
