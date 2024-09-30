# NO IMPORTS!

##################################################
##  Problem 1
##################################################

def trailing_weighted_average(S, W):
    R = [0]*len(S)
    for i in range(len(S)):
        for j in range(len(W)):
            k = i - j
            if k < 0:
                R[i] += S[0] * W[j]
            elif k > len(S): # never happens
                R[i] += S[-1] * W[j]
            else:
                R[i] += S[k] * W[j]
    return R


##################################################
##  Problem 2
##################################################

def all_consecutives(vals, n):
    def helper(prev_set, m):
        if m > len(vals): # tricky case
            return set()
        if m >= n:
            return prev_set
        if m == 0:
            next_set = set((v,) for v in vals)
        else: 
            next_set = set()
            for seq in prev_set:
                next_val = seq[-1]+1
                if next_val in vals:
                    next_set.add(seq + (next_val,))
        return helper(next_set, m+1)
    return helper(None, 0)


##################################################
##  Problem 3
##################################################

import time, math

FREE = 0
BOTH = 1
SINGLE = 1

cached_answers = {}
n_calls = 0

def cost_to_consume(seq1, seq2):
    global n_calls
    n_calls += 1
    len1 = len(seq1)
    len2 = len(seq2)

    if len1 == 0:
        return SINGLE * len2
    elif len2 == 0:
        return SINGLE * len1
    elif seq1[0] == seq2[0]:
        return FREE + cost_to_consume(seq1[1:], seq2[1:])
    else:
        # Minor optimization: if best possible answer, don't
        # go down the subsequent branch.
        both_distance = cost_to_consume(seq1[1:], seq2[1:])
        if both_distance == 0:
            return BOTH

        eat_seq1_distance = cost_to_consume(seq1[1:], seq2)
        if eat_seq1_distance == 0:
            return SINGLE
        
        eat_seq2_distance = cost_to_consume(seq1, seq2[1:])
        if eat_seq2_distance == 0:
            return SINGLE
        
        return min(BOTH + both_distance,
                   SINGLE + eat_seq1_distance,
                   SINGLE + eat_seq2_distance)

# Another solution
def cost_to_consume(left, right):
    global n_calls
    n_calls += 1

    def both() :
        cost = 0
        if (left[0] != right[0]) :
            cost = 1
        return cost
            
    # base case
    if right == str() or left == str() :
        cost = len(left) + len(right)

    # recursive case
    else :
        cost = min(cost_to_consume(left[1:], right) + 1,
                   cost_to_consume(left, right[1:]) + 1,
                   cost_to_consume(left[1:], right[1:]) + both())

    return cost

# A fancy solution; necessary for larger cases (cases
# larger than we ask on the quiz).
def cost_to_consume_cached(seq1, seq2):
    global n_calls
    n_calls += 1
    known = cached_answers.get((seq1, seq2), None)
    if known:
        return known
    len1 = len(seq1)
    len2 = len(seq2)
    if len1 == 0:
        ans = SINGLE * len2
    elif len2 == 0:
        ans = SINGLE * len1
    elif seq1[0] == seq2[0]:
        ans = FREE + cost_to_consume_cached(seq1[1:], seq2[1:])
    else:
        ans = min(BOTH + cost_to_consume_cached(seq1[1:], seq2[1:]),
                  SINGLE + cost_to_consume_cached(seq1[1:], seq2),
                  SINGLE + cost_to_consume_cached(seq1, seq2[1:]))
    cached_answers[(seq1, seq2)] = ans
    return ans
