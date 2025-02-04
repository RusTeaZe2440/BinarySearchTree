# Binary Search Tree

A Binary Search Tree (BST) is a node-based binary tree data structure that maintains a sorted order of elements. Each node in a BST has at most two children, referred to as the left child and the right child. The key properties of a BST are:

* Left Subtree:

        All nodes in the left subtree of a node contain values less than the node's value.

* Right Subtree:

        All nodes in the right subtree of a node contain values greater than the node's value.

* No Duplicate Nodes:

        Typically, BSTs do not contain duplicate values.

#### Basic Operations on a BST
1. Insertion:

* Add a new node while maintaining the BST properties.

2. Search:

* Find a node with a given value.

3. Deletion:

* Remove a node while maintaining the BST properties.

4. Traversal:

* Visit all nodes in a specific order (e.g., in-order, pre-order, post-order).

#### BST Properties
Average Case Time Complexity:

    Insertion: O(log n)

    Search: O(log n)

    Deletion: O(log n)

    Worst Case Time Complexity:

    if the tree becomes unbalanced (e.g., a linked list), operations degrade to O(n).

## Traversal Methods
#### In-Order Traversal:

Traverse the left subtree, visit the root, then traverse the right subtree.

Outputs nodes in ascending order.

#### Pre-Order Traversal:

Visit the root, traverse the left subtree, then traverse the right subtree.

#### Post-Order Traversal:

Traverse the left subtree, traverse the right subtree, then visit the root.

![alt text](binraysearch.png)

### Key Points to Remember
* BSTs maintain a sorted order of elements.

* Insertion, deletion, and search operations are efficient in balanced BSTs.

* Traversal methods (in-order, pre-order, post-order) allow processing of nodes in different orders.

* Balancing techniques are crucial for maintaining performance.


