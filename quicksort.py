def quicksort(a):
    if not a:
        return []
    else:
        left=[]
        right=[]
        pivot=a[0]
        for i in a[1:]:
            if i <=pivot:
                left.append(i)
            else:
                right.append(i)
        return quicksort(left)+[pivot]+quicksort(right)
print(quicksort([2,6,4,2,7,9,1]))