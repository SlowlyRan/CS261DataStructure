# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional

class CuckooHash24:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.bucket_size = 4
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.table = [None]*self.table_size

	def get_rand_bucket_index(self, bucket_idx: int) -> int:
		# you must use this function when you need to evict a random key from a bucket. this function
		# randomly chooses an index from a given cell index. this ensures that the random
		# index chosen by your code and our test script match.
		#
		# for example, if you need to remove a random element from the bucket at table index 5,
		# you will call get_rand_bucket_index(5) to determine which key from that bucket to evict, i.e. if get_random_bucket_index(5) returns 2, you
		# will evict the key at index 2 in that bucket.
		rand.seed(int(str(bucket_idx)))
		return rand.randint(0, self.bucket_size-1)

	def hash_func(self, key: int, func_id: int) -> int:
		# access h0 via func_id=0, access h1 via func_id=1
		key = int(str(key) + str(self.__num_rehashes) + str(func_id))
		rand.seed(key)
		result = rand.randint(0, self.table_size-1)
		return result

	def get_table_contents(self) -> List[Optional[List[int]]]:
		# the buckets should be implemented as lists. Table cells with no elements should still have None entries.
		return self.table

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	def insert(self, key: int) -> bool:
		cycle_num = 0
		tb = 0
		num = key
		flag = True
		while flag:
			f = self.insert_once(num)
			if f == "T":
				return True
			else:
				num = f
				cycle_num = cycle_num+1
				if cycle_num > 10:
					return False
	def insert_once(self, key):
		hash_value0 = self.hash_func(key, 0)

		look_up = self.table[hash_value0]
		if look_up == None:
			self.table[hash_value0] = [key]
			return "T"
		elif len(look_up) < self.bucket_size:
			self.table[hash_value0].append(key)
			return "T"
		else:
			hash_value1 = self.hash_func(key, 1)
			look_up = self.table[hash_value1]
			if look_up == None:
				self.table[hash_value1] = [key]
				return "T"
			elif len(look_up) < self.bucket_size:
				self.table[hash_value1].append(key)
				return "T"
			else:
				n = self.get_rand_bucket_index(hash_value0)
				next = self.table[hash_value0][n]
				self.table[hash_value0][n] = key
				return next


	def lookup(self, key: int) -> bool:
		hashvalue0 = self.hash_func(key, 0)
		hashvalue1 = self.hash_func(key, 1)
		if self.table[hashvalue0] and key in self.table[hashvalue0]:
			return True
		elif self.table[hashvalue1] and key in self.table[hashvalue1]:
			return True
		return False


	def delete(self, key: int) -> None:
		hashvalue0 = self.hash_func(key, 0)
		hashvalue1 = self.hash_func(key, 1)
		for j in [hashvalue0,hashvalue1]:
			if key in self.table[j]:
				self.table[j].remove(key)
				if self.table[j] == []:
					self.table[j] = None
			return

	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line
		old_table = self.table
		self.table =  [None]*self.table_size
		for j in old_table:
			if j != None:
				for i in j:
					self.insert(i)
		return


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define


