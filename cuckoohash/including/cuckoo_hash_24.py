# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random
import random as rand
from typing import List, Optional

class CuckooHash24:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.bucket_size = 4
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.tables = [[None]*init_size for _ in range(2)]

	def get_rand_idx_from_bucket(self, bucket_idx: int, table_id: int) -> int:
		# you must use this function when you need to displace a random key from a bucket during insertion (see the description in requirements.py). 
		# this function randomly chooses an index from a given bucket for a given table. this ensures that the random 
		# index chosen by your code and our test script match.
		# 
		# for example, if you are inserting some key x into table 0, and hash_func(x, 0) returns 5, and the bucket in index 5 of table 0 already has 4 elements,
		# you will call get_rand_bucket_index(5, 0) to determine which key from that bucket to displace, i.e. if get_random_bucket_index(5, 0) returns 2, you
		# will displace the key at index 2 in that bucket.
		rand.seed(int(str(bucket_idx) + str(table_id)))
		return rand.randint(0, self.bucket_size-1)

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size-1)

	def get_table_contents(self) -> List[List[Optional[List[int]]]]:
		# the buckets should be implemented as lists. Table cells with no elements should still have None entries.
		return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	def insert(self, key: int) -> bool:
		cycle_num = 0
		tb = 0
		num = key
		flag = True
		while flag:
			f = self.insert_once(num,tb)
			#print(self.tables)
			if f == "T":
				return True
			else:
				#print(f)
				num = f
				tb= (tb+1)%2
				cycle_num = cycle_num+1
				if cycle_num > 10:
					return False

	def insert_once(self, key, table_id):
		hash_value = self.hash_func(key, table_id)
		look_up = self.tables[table_id][hash_value]
		if look_up == None:
			self.tables[table_id][hash_value] = [key]
			return "T"
		elif len(look_up) < self.bucket_size:
			self.tables[table_id][hash_value].append(key)
			return "T"
		else:
			n= self.get_rand_idx_from_bucket(hash_value,table_id)
			next = self.tables[table_id][hash_value][n]
			self.tables[table_id][hash_value][n] = key
			return next

	def lookup(self, key: int) -> bool:
		hashvalue0 = self.hash_func(key, 0)
		hashvalue1 = self.hash_func(key, 1)
		if self.tables[0][hashvalue0] and key in self.tables[0][hashvalue0]:
			return True
		elif self.tables[1][hashvalue1] and key in self.tables[1][hashvalue1]:
			return True
		return False


	def delete(self, key: int) -> None:
		hashvalue0 = self.hash_func(key, 0)
		hashvalue1 = self.hash_func(key, 1)
		if key in self.tables[0][hashvalue0]:
			self.tables[0][hashvalue0].remove(key)
			if self.tables[0][hashvalue0] ==[]:
				self.tables[0][hashvalue0] = None
		elif key in self.tables[1][hashvalue1]:
			self.tables[0][hashvalue0].remove(key)
			if self.tables[1][hashvalue1] ==[]:
				self.tables[1][hashvalue1] = None

		return


	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line
		old_table = self.tables
		self.tables = [[None] * self.table_size for _ in range(2)]
		for j in old_table[0] + old_table[1]:
			if j != None:
				for i in j:
					self.insert(i)
		return


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define


