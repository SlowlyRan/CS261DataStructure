from cuckoo_hash import CuckooHash
input_size, table_size = 10, 10
nums = [i for i in range(input_size)]

print(nums)
c = CuckooHash(table_size)
for num in nums:
    print("inserting %d" % num)
    no_cycle = c.insert(num)
    if no_cycle == False:
        print("error: cycle should not exist")
print(c.tables)