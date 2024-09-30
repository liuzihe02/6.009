

##############################################
##  Binary search tree with methods
##############################################

# Binary search tree and associated methods
class BSTree:
    def __init__(self,key,name,left=None,right=None):
        self.key = key
        self.name = name
        self.left = left
        self.right = right

    # does tree have a particular key?
    # Python3 syntax: "key in bst"
    def __contains__(self,key):
        node = self
        while node is not None:
            if key == node.key: return True
            node = node.left if key < node.key else node.right
        return False

    # find key in tree, return associated nameue
    def get(self,key,default = None):
        node = self
        while node is not None:
            if key == node.key:
                return node.name
            node = node.left if key < node.key else node.right
        return default

    # insert new nameue into tree
    def insert(self, key, name):
        node = self
        while True:
            if key == node.key:
                node.name = name
                return
            elif key < node.key:
                # key belongs in left subtree
                if node.left is None:
                    node.left = BSTree(key,name)
                    return
                node = node.left
            else:
                # key belongs n right subtree
                if node.right is None:
                    node.right = BSTree(key,name)
                    return
                node = node.right

    # helper function for removing nodes
    def _replace_child(self, child, new_child):
        if self.left == child:
            self.left = new_child
        elif self.right == child:
            self.right = new_child

    # remove key from tree
    def delete(self, key):
        parent, node = None, self
        while node is not None:
            if key == node.key: break
            parent, node = node, node.left if key < node.key else node.right
        else: raise KeyError

        # node has the key we wish to remove
        if node.left is None:
            if node.right is None:
                # node has no children, so just delete from tree
                assert parent is not None  # bug: can't remove last node!
                parent._replace_child(node, None)
            else:
                # node only has right child, so copy right child contents
                node.key,node.name,node.left,node.right = node.right.key,node.right.name,node.right.left,node.right.right
        else:
            if node.right is None:
                # node only has left child, so copy left child contents
                node.key,node.name,node.left,node.right = node.left.key,node.left.name,node.left.left,node.left.right
            else:
                # node has both children, so replace with in-order successor.
                parent, successor = node, node.right
                while successor.left:
                    parent, successor = successor, successor.left
                # copy successor contents to node
                node.key, node.name = successor.key, successor.name
                # now remove successor node
                parent._replace_child(successor, successor.right)


    # support iter() built-in function
    # a more incremental iterator to generate keys in order                                                         

    def __iter__(self):
        if self.left:
            for key in self.left:
                yield key
        yield self.key
        if self.right:
            for key in self.right:
                yield key

    # an even better iterator implementation
    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.key
        if self.right:
            yield from self.right

    # generate in-order list of (key,nameue) pairs
    def items(self):
        if self.left:
            yield from self.left.items()
        yield (self.key,self.name)
        if self.right:
            yield from self.right.items()
    
def print_tree(tree,prefix = ''):
    if tree is None:
        print('%sNone' % prefix)
    else:
        print('%s%s: %s' % (prefix,tree.key,tree.name))
        print_tree(tree.left,prefix + '  ')
        print_tree(tree.right,prefix + '  ')

tree = BSTree(22, "root")
tree.insert(14, "A")
tree.insert(33, "B")
tree.insert(2, "C")
tree.insert(17, "D")
tree.insert(27, "E")
tree.insert(45, "F")
tree.insert(47, "G")


print(tree.items())
print(list(tree.items()))

print(iter(tree))
for key in tree:
    if key == 45:
        break
    else:
        print(key)


