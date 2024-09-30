class Trie:
    def __init__(self, itemtype=None):
        self.value = None
        self.children = {}
        self.type = itemtype

    def checktype(self, key):
        """
        Raise an error when a prefix of the wrong type is used
        """
        if not isinstance(key, self.type):
            raise TypeError

    def getval(self, key):
        """
        Helper for get and contains. Gets the value associated
        with a key if one exists, otherwise returns None
        """
        # Base case, traversed Trie down to the last element of the key
        if len(key) == 0:
            return self.value
        # Recursive step: walk down Trie one element of key at a time
        childKey = key[:1]
        if childKey in self.children:
            return self.children[childKey].getval(key[1:])
        # If key does not exist in the Trie
        else:
            return None

    def set(self, key, value):
        """
        Add a key with the given value to the trie, or reassign the associated
        value if it is already present in the trie.  Assume that key is an
        immutable ordered sequence.  Raise a TypeError if the given key is of
        the wrong type.
        """
        if self.type is None:
            self.type = type(key)
        else:
            self.checktype(key)
        # Iteratively travel down the trie one element of key at a time
        current = self
        for i in range(len(key)):
            subkey = key[i:i+1]
            if subkey not in current.children:
                # Add a node for this key element if it doesn't already exist
                if value is not None:
                    current.children[subkey] = Trie(self.type)
                else:
                    # If we try to delete a key that doesn't exist in the Trie
                    raise KeyError
            current = current.children[subkey]
        # Set the value for the node associated with the key
        current.value = value


    def get(self, key):
        """
        Return the value for the specified prefix.  If the given key is not in
        the trie, raise a KeyError.  If the given key is of the wrong type,
        raise a TypeError.
        """
        self.checktype(key)
        val = self.getval(key)
        if val is None:
            raise KeyError
        else:
            return val

    def delete(self, key):
        """
        Delete the given key from the trie if it exists.
        """
        # Setting the value of the key to None is all we need
        # to do to dissociate them in the Trie
        self.set(key, None)

    def contains(self, key):
        """
        Is key a key in the trie? return True or False.
        """
        return self.getval(key) is not None

    def get_items(self):
        """
        Returns a list of (key, value) pairs for all keys/values in this trie and
        its children.
        """
        # APPROACH: Recursively build up items from children
        ans = []
        # Base case: Found a Trie node associated with a value
        if self.value is not None:
            ans.append((self.type(), self.value))
        # Recursive step: Get items from children and prepend the keys associated with
        # the children to build up full sequences
        for childkey in self.children:
            for subitem, val in self.children[childkey].get_items():
                ans.append((childkey+subitem, val))
        return ans
    
    def generate_items(self):
        """
        Returns a list of (key, value) pairs for all keys/values in this trie and
        its children
        """
        # Base case: Found a Trie node associated with a value
        if self.value is not None:
            yield (self.type(), self.value)
        # Recursive step: Get items from children and prepend the keys associated with
        # the children to build up full sequences
        for childkey in self.children:
            for subitem, val in self.children[childkey].generate_items():
                yield childkey+subitem, val