# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

def quicksort(numbers):
    quicksort_helper(numbers, 0, len(numbers)-1)


def quicksort_helper(numbers, start, end):
    if start < end:
        split_point = partition(numbers, start, end)

        quicksort_helper(numbers, start, split_point-1)
        quicksort_helper(numbers, split_point+1, end)


def partition(numbers, start, end):
    pivot = numbers[start]

    leftmark = start + 1
    rightmark = end

    done = False
    while not done:
        while leftmark <= rightmark and numbers[leftmark] <= pivot: # the order of these conditions are critical!
            leftmark += 1
        while rightmark >= leftmark and numbers[rightmark] >= pivot:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]

    numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
    return rightmark




s = [3,9,1,2,20,100,8,7]
quicksort(s)
print(s)

