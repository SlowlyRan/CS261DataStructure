import requirements

from typing import TypeVar, NamedTuple

KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')

class InsertType(NamedTuple):
	key: KeyType
	val: ValType
	rank: int
KeyType = TypeVar('KeyType')
ValType = TypeVar('ValType')
tree = requirements.ZipTree()
skip_list = requirements.SkipList()

def create_tree_with_data(data: [InsertType]) -> requirements.ZipTree:
	tree = requirements.ZipTree()
	for item in data:
		tree.insert(item.key, item.val, item.rank)

	return tree

data = [InsertType(4, 'a', 0), InsertType(5, 'b', 0), InsertType(2, 'c', 2), InsertType(1, 'd', 1)]
tree = create_tree_with_data(data)

skip_list.from_zip_tree(tree)
skip_list.print_skiplist()





