#function quicksort(array)
#    less, equal, greater := three empty arrays
#    if length(array) > 1  
#        pivot := select any element of array
#        for each x in array
#            if x < pivot then add x to less
#            if x = pivot then add x to equal
#            if x > pivot then add x to greater
#        quicksort(less)
#        quicksort(greater)
#        array := concatenate(less, equal, greater)

tosort = [5, 2, 0, 10, 12, 44, -5, 192, 0.001, -0.0001, 1000]

def quicksort(A):
    less, equal, greater = [], [], []
    if len(A) > 1:
        pivot = A[-1]
        for i in A:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
#        print([less, equal, greater])
        less = quicksort(less)
        greater = quicksort(greater)
        
        return less + equal + greater
    return A
        
print(quicksort(tosort))



import time
t0 = time.clock()
quicksort(tosort)
#sorted(tosort)
print(time.clock() - t0)