# Python program to get intersection point of two linked list

# Link list node
class node:
	def __init__(self, data):
		self.data = data
		self.next = None

def getIntersectionNode(h1, h2):
	while h2:
		temp = h1
		while temp:
			if temp == h2:
				return h2
			temp = temp.next
		h2 = h2.next
	return None

if __name__ == '__main__':

	newNode = node(10)
	h1 = newNode
	newNode = node(3)
	h2 = newNode
	newNode = node(6)
	h2.next = newNode
	newNode = node(9)
	h2.next.next = newNode
	newNode = node(15)
	h1.next = newNode
	h2.next.next.next = newNode
	newNode = node(30)
	h1.next.next = newNode

	intersectionPoint = getIntersectionNode(h1, h2)

	if not intersectionPoint:
		print(" No Intersection Point ")
	else:
		print("Intersection Point:", intersectionPoint.data)