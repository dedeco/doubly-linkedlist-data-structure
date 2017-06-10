from linkedlist import node, linkedList

def test():

	print 'Testing Linked List'

	l = linkedList()

	l.add(10)
	l.add(20)
	l.add(30)
	l.add(40)
	l.add(50)
	l.add(60)

	print 'Linked List after insert nodes:'
	l.__str__()

	print 'Search some value, 30:'
	node = l.search(30)
	print node

	print 'Delete some value, 30:'
	node = l.delete(30)
	l.__str__()

	print 'Delete first element, 60:'
	node = l.delete(60)
	l.__str__()

	print 'Delete last element, 10:'
	node = l.delete(10)
	l.__str__()


if __name__ == "__main__":
	test()