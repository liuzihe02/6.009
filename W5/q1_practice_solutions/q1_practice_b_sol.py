# NO IMPORTS!

##################################################
##  Problem 1
##################################################

def vals_at_depth(tree, depth):
    if tree == []:
        return []
    if depth == 0:
        return [tree[0]]
    vals = []
    for c in tree[1:]:
        vals.extend(vals_at_depth(c, depth-1))
    return vals


##################################################
##  Problem 2
##################################################

# iterative
def iweave(list1, list2):
    result = []
    last = None

    def until_diff(L):
        while L != []:
            first = L.pop(0)
            if first != last:
                return first

    while list1!=[] or list2!=[]:
        next = until_diff(list1)
        if next is not None:
            result.append(next)
            last = next
        next = until_diff(list2)
        if next is not None:
            result.append(next)
            last = next
    return result

# recursive
def weave(list1, list2, last=None, result=None):
    if result is None:
        result = []
    if list1 == [] and list2 == []:
        return result
    (source, other) = (list1, list2) if list1!=[] else (list2, list1)
    while source != []:
        next = source.pop(0)
        if next != last:
            result.append(next)
            return weave(other, source, next, result)
    return weave(other, source, last, result)

weave = iweave


##################################################
##  Problem 3
##################################################

def all_blobs(world):
    blobs = []
    vals = [[x for x in row] for row in world["grid"]]

    def first_occupied():
        """Return (r, c) for first "occupied" (i.e., non-None) square, 
           or None if vals is empty or has nothing but Nones in it.
        """
        for r in range(world["nrows"]):
            for c in range(world["ncols"]):
                val = vals[r][c]
                if val is not None:
                    return (r, c)
        return None

    def get_blob(r, c):
        """Create a NEW blob at (r, c)"""
        val = vals[r][c]
        blob = [val, set()]
        expand_blob(blob, val, r, c)
        return blob

    def expand_blob(blob, val, r, c):
        """Recursively grow the blob"""
        if r < 0 or r >= world["nrows"] or c < 0 or c >= world["ncols"]:
            return
        if vals[r][c] != val:
            return
        blob[1].add((r,c))
        vals[r][c] = None
        for dr, dc in [(-1, 0), (0,0), (1,0), (0, -1), (0,1)]:
            expand_blob(blob, val, r+dr, c+dc)

    while True:
        locn = first_occupied()
        if locn is None:
            return blobs
        else:
            r, c = locn
            blobs.append(get_blob(r, c))

    return blobs
