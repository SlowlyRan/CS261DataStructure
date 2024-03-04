# explanations for member functions are provided in requirements.py
from __future__ import annotations

class FibNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []
        self.flag = False

    def get_value_in_node(self):
        return self.val

    def get_children(self):
        return self.children

    def get_flag(self):
        return self.flag

    def __eq__(self, other: FibNode):
        return self.val == other.val

class FibHeap:
    def __init__(self):
        # you may define any additional member variables you need
        self.roots = []
        self.min = 0
        self.number_of_nodes=0

    def get_roots(self) -> list:
        return self.roots

    def insert(self, val: int) -> FibNode:
        self.roots.append(FibNode(val))
        if self.roots[-1].val < self.roots[self.min].val:
            self.min = len(self.roots)-1
        self.number_of_nodes +=1
        return self.roots[-1]
        
    def delete_min(self) -> None:
        for i in self.roots[self.min].children:
            i.parent = None
            self.roots.append(i)
            i.flag = False
        self.roots.remove(self.roots[self.min])

        R = self.get_roots().copy()
        c = dict()
        while R:
            root = R.pop(-1)
            num_of_children = len(root.children)
            if num_of_children not in c.keys() or c[num_of_children] is None:
                c[num_of_children] = root
            else:
                root_new = self.combine(c[num_of_children],root)
                R.append(root_new)
                c[num_of_children] = None

        min_value = "k"
        for i in range(len(self.roots)):
            if min_value =="k" or min_value > self.roots[i].val:
                min_value = self.roots[i].val
                self.min = i





    def combine(self,node1,node2):
        if node1.val < node2.val:
            node1.children.append(node2)
            self.roots.remove(node2)
            node2.parent = node1
            return node1
        else:
            node2.children.append(node1)
            self.roots.remove(node1)
            node1.parent = node2
            return node2




    def find_min(self) -> FibNode:
        return self.roots[self.min]

    def promote(self,node):
        p = node.parent
        p.children.remove(node)
        node.parent = None
        self.roots.append(node)
        node.flag = False
        if p.flag:
            self.promote(p)
        elif p not in self.roots:
            p.flag = True
        return

    def decrease_priority(self, node: FibNode, new_val: int) -> None:
        if node in self.roots:
            node.val = new_val
        else:
            self.promote(node)
        node.val = new_val
        if new_val <  self.roots[self.min].val:
            self.min = self.roots.index(node)

    def print_heap(self):
        #return
        print("A new heap")
        for i in self.roots:
            print("root_node_val{}".format(i.val))
            self.print_children(i)
    def print_root(self):
        #return
        print("A new heap")
        for i in self.roots:
            print("root_node_val{}".format(i.val))

    def print_children(self,parent):
        #return
        if not parent.children:
            return
        for i in parent.children:
            print("child_of_val{},flag = {},val = {},parent{}".format(parent.val,i.flag,i.val,i.parent.val))
            self.print_children(i)



    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define
