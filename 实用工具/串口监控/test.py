# a=input()
# sets=set()
# l=len(a)
# for i in range(l):
#     sets.add(a[i:]+a[:i])
# print(len(sets))

import re
a=input()
b=input()
ref=re.compile(b)
n=int(input())
for i in range(n):
    instr=input()
    l=int(instr.split(' ')[0])
    r = int(instr.split(' ')[1])
    txt = a[l-1:r]
    sum= len(ref.findall(txt))
    print(sum)