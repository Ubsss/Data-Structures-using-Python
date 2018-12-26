from binarysearchtree.BinarySearchTree import binar_search_tree

myBST = binar_search_tree()

myBST.insert(54)
myBST.insert(77)
myBST.insert(9)
myBST.insert(0)

myBST.traverse_orderly()

myBST.remove(77)

myBST.traverse_orderly()

print(myBST.getMax())
print(myBST.getMin())