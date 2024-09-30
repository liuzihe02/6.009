
#Using a recursive strategy to solve the Dinner Problem


LargeGuestList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
LargeDislikes = [['B', 'C'], ['C', 'D'], ['D', 'E'], ['F','G'],
                 ['F', 'H'], ['F', 'I'], ['G', 'H']]


def dinnerCheck(invited, dislikePairs):
    good = True
    for j in dislikePairs:
        #Check that each element of j is in guests
        if j[0] in invited and j[1] in invited:
            good = False
    return good


def largestSol(chosen, elts, dPairs, Sol):
    """
    Input: chosen is a (possibly empty) list of elements chosen so far.
           elts is a (possibly empty) list of elements yet to consider.
           dinnerCheck(chosen, x, dislikes) return True if it is OK to append x to chosen.
           Sol is list of all largest Sol found so far.
    Return list of all largest Sol found.
    """
    if len(elts) == 0:
        if Sol == [] or len(chosen) > len(Sol):
            Sol = chosen
        return Sol
    if dinnerCheck(chosen + [elts[0]], dPairs):
        Sol = largestSol(chosen + [elts[0]], elts[1:], dPairs, Sol)
    return largestSol(chosen, elts[1:], dPairs, Sol)

    
def InviteDinner(guestList, dislikePairs):
    """
    Print an optimum (largest) dinner party for given input.
    """
    Sol = largestSol([], guestList, dislikePairs, [])
    print("Optimum solution:", Sol, "\n")


InviteDinner(LargeGuestList, LargeDislikes)
