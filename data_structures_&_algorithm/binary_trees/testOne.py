import BinaryTree

tree = BinaryTree.BinaryTree(1)
tree.root.left = BinaryTree.Node(2)
tree.root.right = BinaryTree.Node(3)
tree.root.left.left = BinaryTree.Node(4)
tree.root.left.right = BinaryTree.Node(5)
tree.root.right.left = BinaryTree.Node(6)
tree.root.right.right = BinaryTree.Node(7)

print(tree.print_tree("reverseorder"))
print(tree.tree_height(tree.root))