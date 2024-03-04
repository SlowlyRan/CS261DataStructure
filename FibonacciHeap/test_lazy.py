import requirements
import random as rand


# Instructions
# Some test cases for the FibHeap class can be found below.
#
# Note that the test cases here are just to give an idea of how we will test your submissions, so passing these tests does not mean that your code is correct.
# It is a good idea to try and create different test cases with different table sizes to fully test your implementation.


def fib_rand_insert(val,node,nodelazy,fib,fib2):
    v = rand.randint(0, 500)
    if v not in val:
        print("insert",v)
        val.append(v)
        n = fib.insert(v)

        node.append(n)
        n = fib2.insert(v)

        nodelazy.append(n)

def delete_min(val,node,nodelazy,fib,fib2):
    print("deletmin", fib.find_min().val)
    v = fib.find_min().val
    ind = val.index(v)
    node.remove(node[ind])
    nodelazy.remove(nodelazy[ind])
    val.remove(v)
    fib.delete_min()
    fib2.delete_min_lazy()
    fib2.find_min_lazy()

def decrease_pri_rand(val,node,nodelazy,fib,fib2):
    pass


def fib_heap_tests2():
    fib = requirements.FibHeap()
    fib2 = requirements.FibHeapLazy()
    # uncomment the following line to test FibHeapLazy. The outputs should stay the same.
    # fib = requirements.FibHeapLazy()
    node = []
    val = []
    nodelazy = []

    for i in range(100):
        fib_rand_insert(val, node, nodelazy, fib, fib2)
    for i in range(10):
        delete_min(val, node, nodelazy, fib, fib2)
    fib.print_heap()
    print("-----------------------------------------------------")
    fib2.print_heap()



def fib_heap_tests3():
    fib2 = requirements.FibHeapLazy()
    # uncomment the following line to test FibHeapLazy. The outputs should stay the same.
    # fib = requirements.FibHeapLazy()
    node = []
    val = []
    nodelazy = []

    for i in range(15):
        v = rand.randint(0, 500)
        if v not in val:
            val.append(v)
            n = fib2.insert(v)
            nodelazy.append(n)


    for i in range(2):
        print("____________________________")
        fib2.delete_min_lazy()
        fib2.print_heap()





if __name__ == '__main__':
    # fib_heap_tests()
    fib_heap_tests2()
    #fib_heap_tests3()
