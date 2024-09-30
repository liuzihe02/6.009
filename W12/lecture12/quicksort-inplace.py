#In place partitioning

def partition(list, start, end):
    pivot = list[end]                          # Partition around the last value
    bottom = start-1                           # Start outside the area to be partitioned
    top = end                                  # Ditto

    done = False
    while not done:                            # Until all elements are partitioned...

        while not done:                        # Until we find an out of place element...
            bottom = bottom+1                  # ... move the bottom up.

            if bottom == top:                  # If we hit the top...
                done = True                    # ... we are done.
                break

            if list[bottom] > pivot:           # Is the bottom out of place?
                list[top] = list[bottom]       # Then put it at the top...
                print (list, 'bottom =', bottom, 'top = ', top)
                break                          # ... and start searching from the top.

        while not done:                        # Until we find an out of place element...
            top = top-1                        # ... move the top down.
            
            if top == bottom:                  # If we hit the bottom...
                done = True                    # ... we are done.
                break

            if list[top] < pivot:              # Is the top out of place?
                list[bottom] = list[top]       # Then put it at the bottom...
                print (list, 'bottom =', bottom, 'top = ', top)
                break                          # ...and start searching from the bottom.

    list[top] = pivot                          # Put the pivot in its place.
    print (list)
    return top                                 # Return the split point


def quicksort(list, start, end):
    if start < end:                            # If there are two or more elements...
        print ('Partition start: bottom =', start-1, 'top = ', end)
        print (list)
        split = partition(list, start, end)    # ... partition the sublist...
        print ('Partition end')
        quicksort(list, start, split-1)        # ... and sort both halves.
        quicksort(list, split+1, end)
    else:
        return
    
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
quicksort(a, 0, len(a)-1)

