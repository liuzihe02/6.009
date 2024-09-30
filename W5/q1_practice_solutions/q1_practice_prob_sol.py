# NO IMPORTS!

# SPRING 2019 Quiz 1 Practice Problems

##############
# Problem 01 #
##############

def is_permutation(A, B):
    """ Given two strings, return True iff one is a permutation of the other. """
    return sorted(A) == sorted(B)


##############
# Problem 02 #
##############

def is_unique(A):
    """ Return True iff no repeated element in list A. """
    return len(A) == len(set(A))


##############
# Problem 03 #
##############

def median(A):
    """ Given a list of numbers, return the median. """
    B, i = sorted(A), len(A)//2
    return B[i] if len(A) % 2 else (B[i-1]+B[i])/2


##############
# Problem 04 #
##############

def mode(A):
    """ Return the most common value in list A. """
    count_d, first_seen_index = {}, {}
    for i, elem in enumerate(A): # O(len(A))
        first_seen_index.setdefault(elem,i)
        count_d.setdefault(elem,0)
        count_d[elem] += 1
    freq_d = {}
    for val, count in count_d.items(): # O(len(count_d)) => O(len(A))
        freq_d.setdefault(count, set()).add(val)
    most_commons = {first_seen_index[val]:val for val in freq_d[max(freq_d)]} # O(len(A))
    return most_commons[min(most_commons)]


##############
# Problem 05 #
##############

def find_triple(ilist):
    """ If the list ilist contains three values x, y, and z such that x + y = z
        return a tuple with x and y. Otherwise return None. """
    assert len(ilist) > 2 # precondition
    l = sorted(ilist)
    for i in range(len(l)-2):
        for j in range(i+1,len(l)-1):
            required_sum, low, high = l[i]+l[j], j+1, len(l)-1 # bisection search starts
            while True: 
                k = (low + high)//2 # "x"=l[i], "y"=l[j], "z"=l[k]
                if l[k] == required_sum: return (l[i],l[j]) # "z" found
                if low == high: break # "z" not found but no remaining options with fixed "i" & "j"
                if l[k] > required_sum: high = k # "z" too large
                else: low = k + 1 # "z" too small; NOTE: "+1" because k=(low+high)//2
    return None


##############
# Problem 06 #
##############

def is_quasidrome(s):
    """ Check whether s is a quasidrome. """
    def is_palindrome(s):
        return all(s[i]==s[len(s)-i-1] for i in range(len(s)//2))
    return any(is_palindrome(s[:i]+s[i+1:]) for i in range(len(s)+1))


##############
# Problem 07 #
##############

def max_subsequence(ilist, is_circular = False):
    """ Return the start and end indices as a tuple of the maximum subsequence
        in the list.  If is_circular = True, imagine the list is circular.
        That is, after the end index comes the start index. """
    def fixed_start(l, base, max_len): # return (max sum, start index, end index % max_len)
        return max((sum(l[:i+1]), base, (base+i) % max_len) for i in range(min(len(l), max_len)))
    l, max_len = ilist * (bool(is_circular)+1), len(ilist) # loop once if circular
    return max(fixed_start(l[start:], start, max_len) for start in range(max_len))[1:]


##############
# Problem 08 #
##############

def count_triangles(edges):
    """ Count the number of triangles in edges. """
    def is_triangle(e_1, e_2, e_3):
        return len(set(e_1 + e_2 + e_3)) == 3
    # can optimize by only looping i < j < k indices; but still the same O(len(edges)^3) runtime
    return sum(is_triangle(e_1, e_2, e_3) for i, e_1 in enumerate(edges) 
                                          for j, e_2 in enumerate(edges) 
                                          for k, e_3 in enumerate(edges) if i < j < k)


##############
# Problem 09 #
##############

def matrix_product(A, B, m, n, k):
    """ Compute m-by-k product of m-by-n matrix A with n-by-k matrix B. """
    def get_elem(X, num_cols, r, c): return X[num_cols*r+c]
    return [sum(get_elem(A,n,i,z) * get_elem(B,k,z,j) for z in range(n)) # AB_ij element
                                                            for i in range(m) for j in range(k)]


##############
# Problem 10 #
##############

def transpose(A, m, n):
    """ Return n-by-m transpose of m-by-n matrix A. """
    def get_elem(X, num_cols, r, c): return X[num_cols*r+c]
    return [get_elem(A,n,j,i) for i in range(n) for j in range(m)] # now n-by-m


##############
# Problem 11 #
##############

def check_valid_paren(s):
    """ Return True iff each left parenthesis is closed by exactly one
        right parenthesis later in the string and each right parenthesis
        closes exactly one left parenthesis earlier in the string. """
    # solution 1
    c = 0
    for char in s:
        if char == '(': c += 1
        else: c -= 1
        if c < 0: return False
    return c == 0

    # solution 2 (shorter code but more expensive for longer input)
    l = [int(p is '(') - int(p is ')') for p in s] # +1 for '(' and -1 for ')'
    return all(sum(l[:i]) >= 0 for i in range(len(l))) and sum(l) == 0


##############
# Problem 12 #
##############

def get_all_elements(root):
    """ Return a list of all numbers stored in root, in any order. """
    # one line solution
    return [root["value"]] + get_all_elements(root["left"]) + get_all_elements(root["right"]) if root else []
    
    # expanded version
    elements = []
    if root:
        elements.append(root["value"])
        elements += get_all_elements(root["left"])
        elements += get_all_elements(root["right"])
    return elements


##############
# Problem 13 #
##############

def find_path(grid):
    """ Given a two dimensional m by n grid, with a 0 or a 1 in each cell,
        find a path from the top row (0) to the bottom row (n-1) consisting of
        only ones.  Return the path as a list of coordinate tuples (row, column).
        If there is no path return None. """
    nrows, ncols = len(grid), len(grid[0])
    def is_valid(r,c): return 0 <= r < nrows and 0 <= c < ncols and grid[r][c] == 1
    def get_next(r,c): return {(r+1,c+dc) for dc in (-1,0,1) if is_valid(r+1,c+dc)}
    seen, queue = set(), [((0,c),[(0,c)]) for c in range(ncols) if grid[0][c]] # top row
    while queue:
        (r,c), path = queue.pop(0) # expensive but ok for now
        for cell in get_next(r,c) - set(path):
            if cell[0] + 1 == nrows: return path + [cell] # path found
            if cell in seen: continue
            queue.append((cell, path + [cell]))
            seen.add(cell)
    return None


##############
# Problem 14 #
##############

def longest_sequence(s):
    """ Find sequences of a single repeated character in string s.
        Return the length of the longest such sequence. """
    if len(s) < 1: return 0
    cur, cur_len, max_len = s[0], 0, 0
    for char in s:
        if char == cur: cur_len += 1
        else:
            max_len = max(cur_len, max_len)
            cur, cur_len = char, 1
    return max(cur_len,max_len)


##############
# Problem 15 #
##############

def integer_right_triangles(p):
    """ Let p be the perimeter of a right triangle with integral, non-zero
        length sides of length a, b, and c. Return a sorted list of
        solutions with perimeter p. """
    triangles = []
    a_bound = int(p * 1/(2+2**.5)) + 1 # a:b:c = 1:1:sqrt(2) ratio (impossible with integral lengths)
    for a in range(1, a_bound):
        b_bound = (p-a)//2 + (p-a)%2 # b!=c in a right triangle with a<b<c side lengths
        for b in range(a+1, b_bound):
            c = p - a - b
            if a**2 + b**2 == c**2: triangles.append([a,b,c])
    return triangles # automatically sorted because of the search ordering


##############
# Problem 16 #
##############

def encode_nested_list(seq):
    """ Encode a sequence of nested lists as a flat list. """
    encoded = []
    for elem in seq:
        if isinstance(elem,list): encoded += encode_nested_list(elem)
        else: encoded.append(elem)
    return ['up'] + encoded + ['down']


##############
# Problem 17 #
##############

def second_largest(A):
    """ Given a list of numbers, return the second largest element in the list. 
        You may assume the list has at least two elements. """
    assert len(A) > 1 # precondition
    elems = set(A)
    elems.remove(max(elems)) # largest elem
    return max(elems)


##############
# Problem 18 #
##############

def run_length_encode(S):
    """ Given a string S, return a string that is the run length encoding of S. 
        Assume only alphabetic, capital characters occur in the string (A-Z only). """
    if len(S) < 1: return ""
    cur, cur_len, encoded = S[0], 0, ""
    for char in S:
        if char == cur: cur_len += 1
        else:
            encoded += cur + str(cur_len)
            cur, cur_len = char, 1
    return encoded + cur + str(cur_len)


##############
# Problem 19 #
##############

def histogram(A, low, high, n):
    """ Given a dataset A (a list of integers), count how many numbers fall into each bucket.
        Include only numbers in the [low, high); any integers in A that do not fall into any bucket 
        should not be counted. Return a list of counts for each bin (a list of n elements, where the 
        ith element is the count for the ith bucket from the left). You may assume that (high-low) 
        is a multiple of n. """
    h, size = [0 for _ in range(n)], (high-low)//n
    for val in A:
        if not low <= val < high: continue
        h[(val-low)//size] += 1
    return h


##############
# Problem 20 #
##############

def knight_in_two_moves(A, B):
    """ Given two locations A and B on the chessboard, determine if a knight can travel from one to 
        the other in exactly two moves. Return a Boolean, True if the knight can indeed reach B from 
        A in two moves, and False otherwise. """
    moves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    def is_valid(p): return 0 <= p[0] < 8 and 0 <= p[1] < 8
    def get_next(p): return set((p[0]+r,p[1]+c) for r, c in moves if is_valid((p[0]+r,p[1]+c)))
    return len(set(get_next(A) & get_next(B))) > 0 # at least one way exists
