from typing import Any, List
#from graphviz import Digraph

class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left_child: BinaryNode = None
        self.right_child: BinaryNode = None

    def min(self):
        if not self.left_child:
            return self
        else:
            self.left_child.min()

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        else:
            return True

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def _insert(self, node: BinaryNode, val: Any) -> BinaryNode:

        if node.value > val:
            node.left_child = self._insert(node.left_child, val)
        if node.value < val or node.value == val:
            node.right_child = self._insert(node.right_child, val)
        return node


        # if val < node.value:
        #     if node.left_child:
        #         self._insert(node.left_child, val)
        #     if not node.left_child:
        #         node.left_child = BinaryNode(val)
        #         node.left_child.parent = node
        # if val > node.value:
        #     if node.right_child:
        #         self._insert(node.right_child, val)
        #     if not node.right_child:
        #         node.right_child = BinaryNode(val)
        #         node.right_child.parent = node




    def insert(self, val: Any) -> None:
        if self.root is None:
            self.root = BinaryNode(val)
        else:
            self._insert(self.root, val)

    def insertList(self, list: List[Any]) -> None:
        for val in list:
            if self.root is None:
                self.root = BinaryNode(val)
            else:
                self._insert(self.root, val)

    def contains(self, val: Any):
        if type(self) is BinarySearchTree:
            if not self.root:
                raise ValueError("Root = None")
            if self.root:
                node = self.root
                if val == node.value:
                    return True
                if val < node.value:
                    if not node.left_child:
                        return False
                    return BinarySearchTree.contains(node.left_child, val)
                if val > node.value:
                    if not node.right_child:
                        return False
                    return BinarySearchTree.contains(node.right_child, val) # na 2 czesci podzielone
        if type(self) is BinaryNode:
            if val == self.value:
                return True
            if val < self.value:
                if not self.left_child:
                    return False
                return BinarySearchTree.contains(self.left_child, val)
            if val > self.value:
                if not self.right_child:
                    return False
                return BinarySearchTree.contains(self.right_child, val)



    def _remove(self, node: BinaryNode, val: Any):
        if node.value == val:
            if node.is_leaf() is True:
                return None
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
            node = node.min()
            node.right_child = self._remove(node.right_child, val)
        if node.value > val:
            node.left_child = self._remove(node.left_child, val)
        if node.value < val:
            node.right_child = self._remove(node.right_child, val)
         return node
       
       
       
       
       
        # if self.root > val:
        #     node.left_child = self._remove(node.left_child, val)
        # if self.root < val:
        #     node.right_child = self._remove(node.right_child, val)
        # 
        # else:    # gdy rowne wartosci
        #     if node.is_leaf() is True:
        #         return None
        #     if not root.letf_child:
        #         node = self.root.self.right_child
        #         root = None
        #         return node
        #     if not root.right_child:
        #         node = self.root.letf_child
        #         root = None
        #         return node
        #     node = node.min()
        #     node.right_child = self._remove(node.right_child, val)






        

    def remove(self, val: Any):
        if self.root.value != val:
            self._remove(self.root, val)

    def show(self):
        if self is None:
            raise ValueError("Tree is empty")

        def function(self, dot=None):
            if dot is None:
                dot = Digraph(filename='diagram', comment='Binary Search Tree')
                dot.format = 'png'
                dot.attr('node', shape='circle')
                dot.node(name=str(self), label=str(self))

            for child in [self.left, self.right]:
                if child is not None:
                    if child is self.right:
                        dot.attr('node', shape='circle', style='filled', fillcolor='orange')
                    if child is self.right:
                        dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')
                    dot.node(name=str(child), label=str(child.value))
                    dot.edge(str(self), str(child))
                    dot = function(child, dot=dot)

    # def show(self):
    #     view = " ----- "
    #
    #     if type(self) is BinarySearchTree:
    #         if self.root is None:
    #             return
    #         if self.root.left_child:
    #             BinarySearchTree.show(self.root.left_child)
    #         print("|" + str(self.root.value) + "|")
    #         if self.root.right_child:
    #             BinarySearchTree.show(self.root.right_child)
    #     if type(self) is BinaryNode:
    #         if self.left_child:
    #             BinarySearchTree.show(self.left_child)
    #
    #         print("  " + view * self.level_of() + str(self.value) + "|")
    #         if self.right_child:
    #             BinarySearchTree.show(self.right_child)

B_S_T = BinarySearchTree()
li = [5, 13, 4, 7, 9, 6, 15, 1]

B_S_T.insert(11)
B_S_T.insert(3)
B_S_T.insert(12)
B_S_T.insertList(li)

#B_S_T.show()

B_S_T.remove(5)
B_S_T.show()
