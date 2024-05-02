class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None



class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        if self.head:
            self.head.prev = node
            node.next = self.head
        self.head = node

    def insertAfter(self, prev_node, data):
        node = Node(data)
        node.prev = prev_node
        if prev_node.next:
            node.next = prev_node.next
            prev_node.next.prev = node
        prev_node.next = node
        self.print()

    def search(self,value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def delete(self,value):
        node = self.search(value)
        if node:
            print((self.head.value))
            if self.head == node:
                self.head == node.next
                print(self.head.value)
                if node.next:
                    print(node.next.value)
                    node.next.prev = None
                return
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

    def print(self):
        current = self.head
        while current:
            print(str(current.value) + " -> ", end = '')
            current = current.next

doubleLinkedlist = DoubleLinkedList()
doubleLinkedlist.push(1)
doubleLinkedlist.push(2)
doubleLinkedlist.insertAfter(doubleLinkedlist.search(2),10)
doubleLinkedlist.delete(2)
doubleLinkedlist.print()