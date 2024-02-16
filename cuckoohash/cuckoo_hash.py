# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List

class CuckooHash:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.tables = [[None]*init_size for _ in range(2)]

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size-1)

	def get_table_contents(self) -> List[List[int]]:
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




	def insert_once(self,key,table_id):
		hash_value = self.hash_func(key, table_id)
		if self.tables[table_id][hash_value] == None:
			self.tables[table_id][hash_value] = key
			return "T"
		else:
			next = self.tables[table_id][hash_value]
			self.tables[table_id][hash_value] = key
			return next


	def lookup(self, key: int) -> bool:
		hashvalue0 = self.hash_func(key, 0)
		hashvalue1 = self.hash_func(key, 1)
		if self.tables[0][hashvalue0] == key or self.tables[1][hashvalue1] == key:
			return True
		else:
			return False


	def delete(self, key: int) -> None:
		hashvalue0 = self.hash_func(key, 0)
		hashvalue1 = self.hash_func(key, 1)
		if self.tables[0][hashvalue0] == key:
			self.tables[0][hashvalue0] = None
		elif self.tables[1][hashvalue1] == key:
			self.tables[1][hashvalue1] = None
		return



	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line
		old_table = self.tables
		self.tables = [[None] * self.table_size for _ in range(2)]
		for i in old_table[0]+old_table[1]:
			if i!=None:
				self.insert(i)
		return

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define

