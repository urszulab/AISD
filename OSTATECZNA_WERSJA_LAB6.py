from typing import Any, List
from graphviz import Digraph

class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left_child: BinaryNode = None
        self.right_child: BinaryNode = None

    def min(self): #wchodzi nam wezel jako ten self
        if not self.left_child: #wywoluje sie na nim lewe dziecko i jesli nie ma go, to zwraca sie ten wezel, ktory jest ostatnim lewym dzieckiem
            return self #zwraca wezel
        else:
            self.left_child.min()   # jesli lewe dziecko ma lewe
                # dziecko, to wywolana jest na nim metoda min()

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        else:
            return True

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def _insert(self, node: BinaryNode, val: Any): # tu nie ma przypadku, gdzie if node is NOne, bo na nodzie te metode wywoluje, wiec muso byc node wczesniej
        if val < node.value:
            if node.left_child:
                self._insert(node.left_child, val)
            if not node.left_child:
                node.left_child = BinaryNode(val)
        if val > node.value:
            if node.right_child:
                self._insert(node.right_child, val)
            if not node.right_child:
                node.right_child = BinaryNode(val)
        #TEN DOLNY KOD MI WYRZUCA BLAD
        # if node.value > val:
        #     node.left_child = self._insert(node.left_child, val)
        # if node.value < val or node.value == val:
        #     node.right_child = self._insert(node.right_child, val)
        # return node

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

    def contains(self, val: Any): #PIERWSZY IF SIE WYKONA TYLKO RAZ
        if type(self) is BinarySearchTree: # sprawdza czy obiekt,na ktorym wywolywana jets metoda contains jest typu BinarySearchTree
            if not self.root:
                raise ValueError("Root = None")
            if self.root:
                node = self.root
                if val == node.value:
                    return True
                if val < node.value: # jak znajdzie wartosc to zwraca True, jak nie to False(przy dojsciu do liscia)
                    if not node.left_child:
                        return False # jak szuka wartosci w porownaiu do tje co akuta;nie jest i nie ma dziecka lewgo, to nie moze miec mnejsjzej wartosci
                    return BinarySearchTree.contains(node.left_child, val) # tu wychodiz juz jako typ BinaryNode, wiec pierwsyz if sie nie wykona
                if val > node.value:
                    if not node.right_child:
                        return False
                    return BinarySearchTree.contains(node.right_child, val) # na 2 czesci podzielone
        if type(self) is BinaryNode: # jak 1. raz wywoluje metody is prawdxzam czy drzewo zaiwera, to wywoluje ja ma obiekcie typu binary search tree, a jak wartosc nie jest rowna wartosci roota
            if val == self.value:
                return True
            if val < self.value:
                if not self.left_child:
                    return False
                return BinarySearchTree.contains(self.left_child, val) # To znowu wywola sie na BinaryNode obiekcie i skoncyz jak jak znajdziemy wartosc, ktorej suzkamy albo dojdziemy do liscia drzewa(lewego albo prawego)
            if val > self.value:
                if not self.right_child:
                    return False
                return BinarySearchTree.contains(self.right_child, val)

    def _remove(self, node: BinaryNode, val: Any):
        if val == node.value:
            if node.is_leaf():
                return None
            if not node.left_child:
                return node.right_child
            if not node.right_child:
                return node.left_child
            node = node.right_child.min()
            node.right_child = self._remove(node.right_child, val)  # jak 7 to to, co chcemy usunac, to ona ma jeszce 9. i ta 9 wchodzi nam tu, ale sprawdzamy prawe dziekco 9, ktore nie istnieje, stad blad
        if val < node.value:
            node.left_child = self._remove(node.left_child, val)
        if val > node.value:
            node.right_child = self._remove(node.right_child, val)
        return node

    def remove(self, val: Any): #punkt wejscie metody remove to root
        if self.contains(val): #jesli zawiera wezel jakikolwiek
            if val == self.root.value:
                self.root == None # jak nasza wartosc jest wartoscia z roota, to usuwamy
            else: # a jak nie, to salej szukamy
                self._remove(self.root, val) # tu juz nie sprawdzi czy jest rowny, tylko sprawdzi jego dzieci
        else:
            raise ValueError("There isn\'t any node in this tree")

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

B_S_T = BinarySearchTree()
li = [5, 13, 4, 7, 9, 6, 15, 1]

B_S_T.insert(11)
B_S_T.insert(3)
B_S_T.insert(12)
B_S_T.insertList(li)

B_S_T.show()

B_S_T.remove(9)
B_S_T.show()
