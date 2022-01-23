'''
### Properties of Red-Black tree
- it has to be BST and self balancing tree
- every node has to be either red/black
- every node which is Nil is black
- root node has to be black
- red node shoul not be adjacent (black node could be adjacent)
- the number of black nodes from root to each leaf must have to be the same
'''

'''
### Rules of inserting a node in of Red-Black tree
1. if root is null, create new node with color black and make it root node
2. if root exist, create a new node with color red
3. if the color of parent of newNode is black, exit
4. if the parent's color is Red
    - check the parent's sibling color. If sibling is Null or color is black, 
        do the suitable rotation and re-coloring
    - if the parent's sibling's color is Red, re-colore (both parent and parent's sibling) and check the parent's parent's
        is not root node (if grandfather is not root node then have to re-color the grandparent also) then re-color it and rec-check
'''