# explanations for member functions are provided in requirements.py
# each file that uses a skip list should import it from this file.

from typing import List
import sys
class Trie_node:
    def __init__(self,val):
        self.val = val
        self.children = dict()


class Trie:


    # Trie data structure class
    def __init__(self, is_compressed: bool):
        self.root = Trie_node("root")
        self.is_compressed = is_compressed
        pass

    def insert_word_uncompress(self,word):
        node = self.root
        wordList = list(word)
        wordList.append("$")
        for i in wordList:
            if i in node.children.keys():
                node = node.children[i]
            else:
                node.children[i] = Trie_node(i)
                node = node.children[i]

    def insert_word_compress(self,node,word):
        if not word:
            return
        if word[-1]!="$":
            word = word +"$"
        i = 0
        f = 0
        if not node.children:
            node.children[word[0]] = Trie_node(word)
            return
        for c in node.children.keys():
            if c == word[0]:
                f = 1
                break
        if f == 0:
            node.children[word[0]] = Trie_node(word)
            return
        if f == 1:
            j = 0
            value = node.children[word[0]].val
            while j <min(len(value),len(word)):
                if value[j] != word[j]:
                    node.children[c].val = value[:j]
                    node = node.children[c]
                    d = node.children
                    node.children = dict()
                    node.children[value[j]] = Trie_node(value[j:])
                    node.children[value[j]].children = d
                    node.children[word[j]] = Trie_node(word[j:])
                    return
                else:
                    j = j +1
        if j == len(value):
            node = node.children[c]
            self.insert_word_compress(node,word[j:])
            return





    def print_trie(self):
        node = self.root
        self.print_node(node)
    def print_node(self,node):
        for i in node.children.keys():
            print("children of node {}".format(node.val),node.children[i].val)
        for i in node.children.keys():
            self.print_node(node.children[i])
    def construct_trie_from_text(self, keys: List[str]) -> None:
        if not self.is_compressed:
            for i in keys:
                self.insert_word_uncompress(i)
        if self.is_compressed:
            print("insert",keys)
            for i in keys:
                self.insert_word_compress(self.root,i)





    def construct_suffix_tree_from_text(self, keys: List[str]) -> None:
        if not self.is_compressed:
            for i in keys:
                for j in range(len(i)):
                    ins = i[j:]
                    if self.search_and_get_depth(ins) == -1:
                        self.insert_word_uncompress(ins)
        if self.is_compressed:
            print("insert",keys)
            for i in keys:
                for j in range(len(i)):
                    ins = i[j:]
                    if self.search_and_get_depth(ins) == -1:
                        self.insert_word_compress(self.root,ins)
                        print(ins)

                #print(i)
                #self.print_trie()


    def search_and_get_depth(self, key: str) -> int:
        print("search",key)
        sys.stdout.flush()
        if not self.is_compressed:
            return self.search_and_get_depth_uncompress(key)
        if self.is_compressed:
            return self.search_and_get_depth_compress(self.root,key)



    def search_and_get_depth_uncompress(self, key: str) -> int:
        node = self.root
        wordList = list(key)
        wordList.append("$")
        num= 0
        for i in wordList:
            if i in node.children.keys():
                node = node.children[i]
                num = num+1
            else:
                return -1
        return num-1

    def search_and_get_depth_compress(self, node,key: str) -> int:
        if key[-1]!="$":
            key= key+"$"
        if key[0] not in node.children.keys():
            return -1
        if key[0] in node.children.keys():
            value = node.children[key[0]].val
            print(value)
            j = 0
            while j < min(len(value), len(key)):
                if value[j] != key[j]:
                    return -1
                else:
                    j = j + 1
        if value[j-1] == "$":
            if j ==1:
                return 0
            else:
                return 1
        else:
            node = node.children[key[0]]
            num = self.search_and_get_depth_compress(node, key[j:])
            if num >=0:
                return num+1
            else:
                return num



# feel free to define new classes/methods in addition to the above
# fill in the definitions of each required member function (above),
# and any additional member functions you define
