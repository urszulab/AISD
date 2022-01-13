from typing import Any, List

class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left_child: BinaryNode = None
        self.right_child: BinaryNode = None
        self.parent: BinaryNode = None

    def min(self):  #wchodzi nam wezel jako ten self
        if not self.left_child: #wywoluje sie na nim lewe dziecko i jesli nie ma go, to zwraca sie ten wezel, ktory jest ostatnim lewym dzieckiem
            return self  #zwraca wezel
        else:
            self.left_child.min()    # jesli lewe dziecko ma lewe
                                #dziecko, to wywolana jest na nim metoda min()


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def _insert(self, node: BinaryNode, number: Any) -> BinaryNode: # tu nie ma przypadku, gdzie if node is NOne, bo na nodzie te metode wywoluje, wiec muso byc node wczesniej
        if node.value > number:
            if not self.right_child:
                self.right_child = BinaryNode(number)
            else:
                self._insert(node.right_child, number)
        else:
            if not self.left_child:
                self.left_child = BinaryNode(number)
            else:
                self._insert(node.left_child, number)
        return node


    def insert(self, number: Any) -> None:
        if self.root is None:
            self.root = BinaryNode(number)
        else:
            self._insert(self.root, number)

    def insertList(self, list: List[Any]) -> None:
        for number in list:
            if self.root is None:
                self.root = BinaryNode(number)
            else:
                self._insert(self.root, number)

    def contains(self, value: Any):
        if type(self) is BinarySearchTree:
            if not self.root:
                raise ValueError("Root = None")
            if self.root:
                node = self.root
                if value == node.value:
                    return True
                if value < node.value:
                    if not node.left_child:
                        return False
                    return BinarySearchTree.contains(node.left_child, value)
                if value > node.value:
                    if not node.right_child:
                        return False
                    return BinarySearchTree.contains(node.right_child, value) # na 2 czesci podzielone
        if type(self) is BinaryNode:
            if value == self.value:
                return True
            if value < self.value:
                if not self.left_child:
                    return False
                return BinarySearchTree.contains(self.left_child, value)
            if value > self.value:
                if not self.right_child:
                    return False
                return BinarySearchTree.contains(self.right_child, value)

    def _remove(self, node: BinaryNode, value: Any):
        if value == node.value:
            if node.is_leaf() is True:
                node = None
            if node.right_child:

    def remove(self, value: Any):
        if self.root.value != value
            self._remove(self.root, value)

    def show(self):
        view = " ----- "

        if type(self) is BinarySearchTree:
            if self.root is None:
                return
            if self.root.left_child:
                BinarySearchTree.show(self.root.left_child)
            print("|" + str(self.root.value) + "|")
            if self.root.right_child:
                BinarySearchTree.show(self.root.right_child)
        if type(self) is BinaryNode:
            if self.left_child:
                BinarySearchTree.show(self.left_child)

            print("  " + view * self.level_of() + str(self.value) + "|")
            if self.right_child:
                BinarySearchTree.show(self.right_child)



B_S_T = BinarySearchTree()

li = [5,13,4,7,9,6,15,1]

for el in li:
    B_S_T.insert(el)
B_S_T.insertList(li)





"""
 #nowy wezel jest za kazdym razem korzeniem
        if self.root is None:
            self.root = node(value)
            return self.root

"""
