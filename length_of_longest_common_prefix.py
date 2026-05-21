def longest_common_prefix(arr1, arr2):
    arr1 = list(map(str, arr1))
    arr2 = list(map(str, arr2))
    arr1.sort()
    arr2.sort()

    max_len = 0
    y = 0
    i = 0

    while i < len(arr1) and y < len(arr2):
        e1 = arr1[i]
        e2 = arr2[y]
        if not e1 or not e2:
            break

        se = e1[0]
        if e2[0] < se:
            y += 1
            continue
        elif e2[0] > se:
            i += 1
            continue
        else:
            ci = 0
            while ci < len(e1) and ci < len(e2) and e1[ci] == e2[ci]:
                ci += 1
            max_len = max(max_len, ci)
            if e1 > e2:
                y += 1
            elif e1 == e2:
                y += 1
            i += 1

    return max_len
