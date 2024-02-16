from cuckoo2 import *
import random
nn = []
for i in range(8):
    nn.append(random.randint(1, 20))
print(nn)

a = CuckooHash(11)

p = 11

nums = []
for i in range(8):
    nums.append(random.randint(0,p*p))
nums = [113, 106, 12, 47, 67, 14, 38, 109]
print("To be inserted:",nums)
hash_value0 = []
hash_value1 = []
for i in nums:
    hash_value0.append(a.hash_func(i,0))
    hash_value1.append(a.hash_func(i,1))

print("hash values0:",hash_value0)
print("hash values1:",hash_value1)

h1 = [[] for i in range(p)]
for j in nums:
    v = a.hash_func(j,0)
    h1[v].append(j)

print("hash chaining",h1)
h2 = [None]*p
for j in nums:
    v0 = a.hash_func(j, 0)
    v = v0
    i = 0
    while 1:
        if h2[v] ==None:
            h2[v] = j
            print("key:", j, "hash_value:", v, "iteration:", i, "inserted!")
            break
        else:
            i = i+1
            v = (v+1)%p
            print("key:",j,"hash_value:", v0,"iteration:",i,"new_value:",v0+i,"new index:", v)


print("linear probing:",h2)

h3 = [None]*p
for j in nums:
    v = a.hash_func(j, 0)
    v0 =v
    i = 0
    while 1:
        if h3[v] ==None:
            h3[v] = j
            print("key:",j,"hash_value:", v,"iteration:",i,"inserted!")
            break
        else:
            i =i+1

            v = (v0+i**2)%p
            print("key:",j,"hash_value:", v0,"iteration:",i,"new_value:",v0 + i *i,"new index:", v)


print("quadratic probing:",h3)
#发现如果只冲突一次，这个其实和linear probing的结果是一样的，相比较而言就是less cluters

h4 = [None]*p
for j in nums:
    v1 = a.hash_func(j, 0)
    v2 =a.hash_func(j, 1)
    i = 0
    v= v1
    while 1:
        if h4[v] ==None:
            h4[v] = j
            print("key:",j,"hash_value:", v1,v2,"iteration:",i,"index:", v,"inserted!")
            break
        else:
            i =i+1
            v = (v1+i*v2)%p
            print("key:",j,"hash_value:", v1,v2,"iteration:",i,"new_value:",v1+i*v2,"new index:", v)


print("double hashing:",h4)

for j in nums:
    a.insert(j)
print(a.tables)




