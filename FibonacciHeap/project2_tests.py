import requirements
import random as rand

# Instructions
# Some test cases for the FibHeap class can be found below.
#
# Note that the test cases here are just to give an idea of how we will test your submissions, so passing these tests does not mean that your code is correct.
# It is a good idea to try and create different test cases with different table sizes to fully test your implementation.

def is_delete_min_correct(roots):
	seen = set()
	for root in roots:
		if len(root.children) in seen:
			return False
		seen.add(len(root.children))
	return True

def fib_heap_tests():
	fib = requirements.FibHeap()
	# uncomment the following line to test FibHeapLazy. The outputs should stay the same.
	# fib = requirements.FibHeapLazy() 
	fib.insert(5)
	fib.insert(7)
	fib.insert(12)
	node = fib.insert(14)
	fib.insert(2)
	fib.print_heap()
	if [x.val for x in fib.get_roots()] != [5, 7, 12, 14, 2]:
		print("fib heap contents incorrect")
		return

	if fib.find_min().val != 2:
		print("min value incorrect")
		return

	fib.delete_min()
	if not is_delete_min_correct(fib.get_roots()):
		print("delete_min incorrect")
		return
	fib.print_heap()
	
	if fib.find_min().val == 2:
		print("error: min val should have changed")
		return

	fib.decrease_priority(node, 1)
	if fib.find_min().val != 1:
		print("min val should be 1")
		return
	fib.print_heap()

	print("all tests passed")
	return

def fib_heap_tests2():
	fib = requirements.FibHeap()
	fib2 = requirements.FibHeapLazy()
	# uncomment the following line to test FibHeapLazy. The outputs should stay the same.
	# fib = requirements.FibHeapLazy()
	node = []
	val = []
	nodelazy = []

	for i in range(30):
		v = rand.randint(0,500)
		if v not in val:
			val.append(v)
			n = fib.insert(v)

			node.append(n)
			n = fib2.insert(v)

			nodelazy.append(n)


	for i in range(20):
		print("deletmin",fib.find_min().val)
		fib.delete_min()
		fib.print_heap()
		fib2.delete_min_lazy()
		c = fib2.find_min_lazy()
		print("min",c.val)
		fib2.print_heap()


def fib_heap_tests3():
	fib = requirements.FibHeap()
	fib2 = requirements.FibHeapLazy()
	# uncomment the following line to test FibHeapLazy. The outputs should stay the same.
	# fib = requirements.FibHeapLazy()
	node = []
	val = []
	nodelazy = []

	for i in range(15):
		v = rand.randint(0,500)
		if v not in val:
			val.append(v)
			n = fib.insert(v)

			node.append(n)
			n = fib2.insert(v)

			nodelazy.append(n)


	for i in range(10):
		print(val[i])
		print(val[i]-8)
		if val[i]-8  not in val:
			fib.decrease_priority(node[i],val[i]-8)
			fib2.decrease_priority(nodelazy[i],val[i]-8)
			fib.print_heap()
			print("fib2")
			fib2.print_heap()







if __name__ == '__main__':
	#fib_heap_tests()
	#fib_heap_tests2()
	fib_heap_tests3()
