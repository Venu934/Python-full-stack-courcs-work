def quick_sort(li, start, end):
    # ✅ Correct base condition
    if start >= end:
        return

    i = start - 1
    pivot = li[end]   # ✅ pivot should be VALUE

    for j in range(start, end):
        if li[j] < pivot:   # ✅ correct comparison
            i += 1
            li[i], li[j] = li[j], li[i]   # ✅ correct swap

    # ✅ Correct swap to place pivot
    li[i+1], li[end] = li[end], li[i+1]

    pivot_index = i + 1

    quick_sort(li, start, pivot_index - 1)
    quick_sort(li, pivot_index + 1, end)


my_list = [5, 3, 7, 9, 2, 5, 3]

quick_sort(my_list, 0, len(my_list) - 1)
print(my_list)
