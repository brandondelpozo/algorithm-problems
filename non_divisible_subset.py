"""
Pseudocede 2
set element a
set element b
permutate two list sum two elements from a list (a[0]+a[1],a[1]+a[2])
while element1 < len(array) and element2 < len(array)
is the sum of the two element from the array is not multiple of the divisor
    add those numbers to the new array result
if those elemtens are multiple of the divsor don't do anything
continue whith two others number
print count of the new array result

arr = [1, 7, 2, 4]
res = []
import itertools
perr = list(itertools.permutations(arr, 2))

print(perr)
print(sum(perr[2]))
"""


from itertools import permutations

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

for p in unique_permutations([1,2,3], 2):
    new_arr = []
    print(p)
    sum_per = sum(p)
    print(sum_per)
    if sum_per % 3 == 0:
        print("this is multiple of 3")
    else:
        new_arr = new_arr + list(p)
    print(new_arr)