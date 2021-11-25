from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode

    def append(self, value: Any) -> None:
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        # mozna tez dac self.push(value)
        else:
            node = self.tail
            newNode = Node(value)
            node.next = newNode
            self.tail = newNode

    def node(self, at: int) -> Node:
        if at < len(self):
            node = self.head
            for i in range(at):
                node = node.next
            return node
        else:
            raise ValueError("There was given an index out of the list.")

    def insert(self, value: Any, after: Node) -> None:
        if after is None:
            print("Given node doesn't exist")
            return
        elif after is self.tail:
            self.append(value)
            return
        newNode = Node(value)
        newNode.next = after.next
        after.next = newNode

    def pop(self) -> Any:
        if len(self) == 0:
            raise ValueError("The list is empty.")
        else:
            firstNode = self.head
            self.head = self.head.next
            return firstNode.value

    def remove_last(self) -> Any:
        if self.head is None:
            print("The list is empty")
            return Node(None)
        elif self.head is self.tail:
            deletedNode = self.head
            self.head = None
            self.tail = None
            return deletedNode
        else:
            node = self.head
            while node.next.next is not None:
                node = node.next
            self.tail = node
            deletedNode = node.next
            node.next = None
            return deletedNode

    def remove(self, after: Node) -> Any:
        if self.head is self.tail or after is self.tail:
            print("There is nothing after" + str(after.value))
            return Node(None)
        elif after.next is self.tail:
            deletedNode = self.remove_last()
            return deletedNode
        else:
            deletedNode = after.next
            after.next = deletedNode.next
            return deletedNode

    def __str__(self) -> str:
        if self.head is None:
            return "The list is empty"
        node = self.head
        resultStr = ""
        while node.next:
            resultStr += f'{node.value}' + " -> "
            node = node.next
        resultStr += f'{node.value}'
        return resultStr

    def __len__(self) -> int:
        node = self.head
        amount = 0
        while node:
            amount += 1
            node = node.next
        return amount


list_ = LinkedList()
list_.push(1)
list_.push(0)
print(f'The list after usage of the  method .push():  {list_}')

list_.append(9)
list_.append(10)
print(f'The list after usage of the method .append():  {list_}')

print(f'Node behind index 2 is: {list_.node(2).value}')

list_.insert(12, list_.node(3))
list_.insert(15, list_.node(2))
print(f'The list after usage of the method .node():  {list_}')

print(f'Deleted element by method pop() is: {list_.pop()}')
print(f'The list after usage of the method .pop():  {list_}')

print(f'Deleted element by method .remove_last() is: {list_.remove_last().value}')
print(f'The list after usage of the method .remove_last():  {list_}')

print(f'The amount of list\'s elements is: {len(list_)}')

print(f'Deleted element after indicated position  is: {list_.remove(list_.node(1)).value}')
print(f'The list after usage of the method .remove():  {list_}')


class Stack:
    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        if len(self._storage) == 0:
            print("Stack is empty")
        else:
            return self._storage.pop()

    def __str__(self) -> str:
        resultStr = ""
        for j in range(len(self._storage)):
            resultStr += f'{(self._storage.node(j).value)} \n'
        return f'Stack looks in this way:\n{resultStr}'

    def __len__(self) -> int:
        return len(self._storage)


stack = Stack()
stack.push(21)
stack.push(18)
stack.push(8)
stack.push(4)
print(stack)

top_value = stack.pop()
print(f'Deleted value is: {top_value}')
print(stack)

print(f'Current amount of stack\'s elements : {len(stack)}')

class Queue:
    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        if len(self._storage) == 0:
            print("The queue is empty")
        else:
            return self._storage.tail.value

    def enqueue(self, element: Any) -> None:
        self._storage.push(element)

    def dequeue(self) -> Any:
        if len(self._storage) == 0:
            print("The queue is empty")
        else:
            return self._storage.remove_last().value

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        resultStr = ""
        for e in range(len(self._storage)):
            resultStr += f'{(self._storage.node(e).value)} \n'
        return f'Queue looks in this way:\n{resultStr}'

queue = Queue()
queue.enqueue('Odpowiedz A')
queue.enqueue('Odpowiedz B')
queue.enqueue('Odpowiedz C')
print(queue)

queue.dequeue()
print(queue)
print(f'The amount of queue\'s elements is: {len(queue)}')

queue.dequeue()
print(queue)
print(f'The amount of queue\'s elements is: {len(queue)}')
