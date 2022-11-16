# Python3 program for the above approach

def checkstring(s1, s2, indexfound, size):
	for i in range(size):
		if(s1[i] != s2[(indexfound + i) % size]):
			return False
	return True

s1 = "abcd"
s2 = "cdab"

if(len(s1) != len(s2)):
	print("s2 is not a rotation on s1")

else:
	indexes = []
	size = len(s1)
	firstChar = s1[0]
	for i in range(size):
		if(s2[i] == firstChar):
			indexes.append(i)

	isRotation = False

	for idx in indexes:
		isRotation = checkstring(s1, s2, idx, size)

		if(isRotation):
			break

	if(isRotation):
		print("Strings are rotations of each other")
	else:
		print("Strings are not rotations of each other")