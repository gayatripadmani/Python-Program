# Python3 program to find
# N'th node from end

class node:
	def __init__(self, newData):
		self.data = newData
		self.next = None

class linkedlist:
	def __init__(self):
		self.head = None

	def push(self, newData):
		newNode = node(newData)
		newNode.next = self.head
		self.head = newNode

	def printnthfromlast(self, n):
		temp = self.head
		length = 0
		while temp is not None:
			temp = temp.next
			length += 1

		if n > length:
			print('Location is greater than the' + ' length of LinkedList')
			return
		temp = self.head
		for i in range(0, length - n):
			temp = temp.next
		print(temp.data)

if __name__ == "__main__":
	llist = linkedlist()
	llist.push(20)
	llist.push(4)
	llist.push(15)
	llist.push(35)

	llist.printnthfromlast(4)