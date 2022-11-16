# Python3 program to print reverse
# of a linked list

# Node class
class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printrev(self, temp):
        if temp:
            self.printrev(temp.next)
            print(temp.data, end=' ')
        else:
            return

    def push(self, newData):
        newNode = node(newData)
        newNode.next = self.head
        self.head = newNode

llist = LinkedList()

llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.printrev(llist.head)