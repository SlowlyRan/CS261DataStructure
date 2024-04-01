# explanations for member functions are provided in requirements.py
# each file that uses a Zip Tree should import it from this file.

from typing import TypeVar
import random




KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')


class TreeNode:
	def __init__(self,key,val,rank=-1):
		self.key = key
		self.val = val
		self.rank = rank
		self.left = None
		self.right = None


class ZipTree:
	def __init__(self):
		self.root = None
		self.size = 0


	@staticmethod
	def get_random_rank():
		# 从几何分布中随机选择节点排名
		rank = random.expovariate(1)
		#rank = np.random.geometric(p=0.9)  # 以0.5的概率选择节点排名
		return round(rank)

	def get_root(self):
		return self.root
	def insert(self, key: KeyType, val: ValType, rank: int = -1):
		if rank == -1:
			rank = ZipTree.get_random_rank()
		node = TreeNode(key, val, rank)

		self.root = self.insert_node(node,self.root)
		self.size  = self.size+1
		return node


	def insert_node(self,node,root):
		if not root:
			root = node
			return node
		else:
			if node.key < root.key:
				if self.insert_node(node,root.left) == node:
					if node.rank < root.rank:
						root.left = node
					else:
						root.left = node.right
						node.right = root
						return node
			else:
				if self.insert_node(node,root.right) == node:
					if node.rank <= root.rank:
						root.right = node
					else:
						root.right = node.left
						node.left = root
						return node
			return root
	def zip(self,n1:TreeNode,n2:TreeNode):
		if not n1:
			return n2
		if not n2:
			return n1
		if n1.rank < n2.rank:
			n2.left = self.zip(n1,n2.left)
			return n2
		else:
			n1.right = self.zip(n1.right,n2)
			return n1




	def remove(self, key: KeyType):
		self.root = self.delete_node(key,self.root)
		return



	def find_node_with_key(self,root,key):
		if key == root.key:
			node = root

		elif key < root.key:
			node = self.find_node_with_key(root.left,key)
		elif key > root.key:
			node = self.find_node_with_key(root.right,key)
		return node


	def delete_node(self,key,root:TreeNode):
		if key == root.key:
			self.size = self.size-1
			root =  self.zip(root.left,root.right)
			return root
		elif key < root.key:
			root.left = self.delete_node(key,root.left)
		elif key > root.key:
			root.right = self.delete_node(key,root.right)
		return root

	def find(self, key: KeyType) -> ValType:
		node = self.find_node_with_key(self.root,key)
		return node.val


	def get_size(self) -> int:
		return self.size


	def get_height(self) -> int:
		return self.get_height_node(self.root)

	def get_depth(self, key: KeyType):
		return self.get_distance(self.root,key)


	def get_height_node(self,node:TreeNode):
		height = 0
		if node.left:
			height = max(height,self.get_height_node(node.left)+1)
		if node.right:
			height  = max(height,self.get_height_node(node.right)+1)
		return height




	def get_distance(self,root,key):
		if root.key ==  key:
			return 0
		elif root.key >key:
			return 1 + self.get_distance(root.left,key)
		elif root.key < key:
			return 1 + self.get_distance(root.right,key)


	def print_tree(self):
		self.print_nodes(self.root)

	def print_nodes(self,root):
		if root.left:
			print("left of {}".format(root.key))
			self.print_nodes(root.left)
		print("key:{},val:{},rank:{}".format(root.key,root.val,root.rank))
		if root.right:
			print("right of {}".format(root.key))
			self.print_nodes(root.right)
# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
