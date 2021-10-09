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

"""
from itertools import permutations

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

while p
for p in unique_permutations([1,2,3], 2):
    new_arr = []
    sum_per = sum(p)
    if sum_per % 3 == 0:
        print("this is multiple of 3")
    else:
        new_arr = new_arr + list(p)
    

    print(p)
    print(sum_per)
    print(new_arr)"""

read = lambda: map(int, input().split())

n, k = read()
a = list(read())
cnt = [0] * k
for x in a:
    cnt[x % k] += 1
    
ans = min(cnt[0], 1)
for rem in range(1, (k + 1) // 2):
    ans += max(cnt[rem], cnt[k - rem])
if k % 2 == 0:
    ans += min(cnt[k // 2], 1)
    
print(ans)
