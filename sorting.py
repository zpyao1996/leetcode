# this is a summary for different sorting algorithm
import heapq
def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        idx = len(a) // 2
        first_half = a[:idx]
        second_half = a[idx:]
        first_half = merge_sort(first_half)
        second_half = merge_sort(second_half)
        ans_list = []
        while first_half and second_half:
            if first_half[0] <= second_half[0]:
                ans_list.append(first_half.pop(0))
            else:
                ans_list.append(second_half.pop(0))
        if not first_half:
            ans_list.extend(second_half)
        else:
            ans_list.extend(first_half)
        return ans_list

def quick_sort1(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    # lazy but easy to understand method
    left_part = [i for i in a[1:] if i <= pivot]
    right_part = [i for i in a[1:] if i > pivot]
    left_part = quick_sort(left_part)
    right_part = quick_sort(right_part)
    return left_part + [pivot] + right_part

def quick_sort(a):
    if len(a) <= 1:
        return a
    # remember this elegant partition code
    def partition(a):
        low, high = 0, len(a) - 1
        pivot = a[high]
        j = low
        for i in range(low, high):
            if a[i] <= pivot:
                a[j], a[i] = a[i], a[j]
                j += 1
        a[j], a[high] = pivot, a[j]
        return j
    idx = partition(a)
    return quick_sort(a[:idx]) + quick_sort(a[idx:])

def heap_sort(a):
    heapq.heapify(a)
    ans_list = []
    while a:
        ans_list.append(heapq.heappop(a))
    return ans_list

a = [2,3,6,1,9,3,4]
print(quick_sort(a))
