def merge(s1, s2, s):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            s.append(s1[i])
            i += 1
        else:
            s.append(s2[j])
            j += 1

    if i == len(s1):
        while j < len(s2):
            s.append(s2[j])
            j += 1
    else:
        while i < len(s1):
            s.append(s1[i])
            i += 1

def mergesort(s):
    if len(s) <= 1:
        return s

    mid = len(s) // 2
    left_sorted = mergesort(s[:mid])
    right_sorted = mergesort(s[mid:])

    merged = []
    merge(left_sorted, right_sorted, merged)
    return merged

s = [3,9,1,2,20,100,8,7]
merged = mergesort(s)
print(merged)