# explanations for member functions are provided in requirements.py
# each file that uses a skip list should import it from this file.

from typing import TypeVar
import random
from zip_tree import ZipTree

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')
class ListNode:
	def __init__(self,key,val):
		self.key = key
		self.val = val
		self.levels = []
		self.right = []

class SkipList:
	def __init__(self):
		self.level_list = []
		self.level_number=0
		self.dummy = None


	def get_random_level(self, key: KeyType) -> int:
	  	# Do not change this function. Use this function to determine what level each key should be at. Assume levels start at 0 (i.e. the bottom-most list is at level 0)
		# e.g. for some key x, if get_random_level(x) = 5, then x should be in the lists on levels 0, 1, 2, 3, 4 and 5 in the skip list.
		random.seed(str(key))
		level = 0
		while random.random() < 0.5 and level < 20:
			level += 1
		return level


	def search_start(self,key,node,level):
		if node == self.level_list:
			if node[level].key > key:
				return node
			else:
				return self.search_start(key, node[level], level)
		if node.levels[level]=="new":
			return node
		elif node.levels[level].key >key:
			return node
		else:
			return self.search_start(key,node.levels[level],level)

	def insert(self, key: KeyType, val: ValType,level="no"):
		node = ListNode(key,val)
		if level =="no":
			level = self.get_random_level(key=key)
		node.levels = ["new"]*(level+1)
		i = self.level_number
		if i==0 and not self.level_list:
			self.level_list = [node]
		elif key < self.level_list[i].key:
			if level >= i:
				node.levels[i] = self.level_list[i]
				self.level_list[i] = node
			next = self.level_list
		else:
			pre_node = self.search_start(key,self.level_list[i],i)
			if level >= i:
				node.levels[i] = pre_node.levels[i]
				pre_node.levels[i] = node
			next =  pre_node

		while i > 0:
			i = i-1
			pre_node = self.search_start(key,next,i)
			next = pre_node
			if level >= i:
				if pre_node == self.level_list:
					node.levels[i] = self.level_list[i]
					self.level_list[i] = node
				else:
					node.levels[i] = pre_node.levels[i]
					pre_node.levels[i] = node

		while level > self.level_number:
			self.level_list.append(node)
			self.level_number = self.level_number+1
		return

	def remove(self, key: KeyType):
		i = self.level_number
		self.dummy = ListNode(float('-inf'), "o")
		self.dummy.levels = self.level_list
		res = self.dummy
		while i >= 0:
			res = self.remove_start(key, res, i)
			i = i - 1
		self.level_list = []
		self.level_number = -1
		for i in self.dummy.levels:
			if i != "new":
				self.level_list.append(i)
				self.level_number+=1


	def remove_start(self, key, node, level):
		if node.key < key:
			if node.levels[level].key == key:
				temp = node.levels[level]
				node.levels[level] = temp.levels[level]
				return node
			if node.levels[level] == "new":
				return node
			elif node.levels[level].key > key:
				return node
			else:
				return self.remove_start(key, node.levels[level], level)




	def find(self, key: KeyType) -> ValType:
		i = self.level_number
		res = self.find_start(key,self.level_list,i)
		while i >=0:
			if isinstance(res, tuple):
				return res[1]
			i = i - 1
			res = self.find_start(key, res, i)
			if isinstance(res, tuple):
				return res[1]
		return False


	def find_start(self,key,node,level):
		if node == self.level_list:
			if node[level].key == key:
				return (node,node[level].val)
			if node[level].key > key:
				return node
			else:
				return self.find_start(key, node[level], level)
		if node.key == key:
			return (node,node.val)
		if node.levels[level]=="new":
			return node
		elif node.levels[level].key > key:
			return node
		else:
			return self.find_start(key,node.levels[level],level)



	def get_list_size_at_level(self, level: int):
		if level > self.level_number:
			return 0
		head = self.level_list[level]
		num = 1
		while head.levels[level]!="new":
			num = num+1
			head = head.levels[level]
		return num


	def from_zip_tree(self, zip_tree: ZipTree) -> None:
		self.get_tree_node(zip_tree.root)

	def get_tree_node(self,root):
		if root.left:
			self.get_tree_node(root.left)
		self.insert(root.key,root.val,root.rank)
		if root.right:
			self.get_tree_node(root.right)

	def print_skiplist(self):
		print(self.level_list)
		print(self.level_number)

		for i in range(self.level_number+1):
			print("level",i)
			self.print_level(self.level_list[i],i)

		return

	def print_level(self,node,i):
		print(node.key)
		if node.levels[i] == "new":
			print("new")
		else:

			self.print_level(node.levels[i],i)

# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
