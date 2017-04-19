def b(arr, v, tl, tr):
    if (tl == tr):
        laba[v] = arr[tl]
    else:

        tm = (tl + tr) // 2
        b(arr, v * 2, tl, tm)
        b(arr, v * 2 + 1, tm + 1, tr)
        laba[v] = laba[v * 2] + laba[v * 2 + 1]


k = 0


def build(arr):
    global laba
    global k
    k=0
    laba = [0] * len(arr) * 4
    b(arr, 1, 0, len(arr) - 1)
    print(laba)
    return laba


def u(v, tl, tr, pos, add):
    if tl == tr:
        laba[v] += add
    else:
        tm = (tl + tr) // 2
        if pos <= tm:
            u(v * 2, tl, tm, pos, add)
        else:
            u(v * 2 + 1, tm + 1, tr, pos, add)
        laba[v] = laba[v * 2] + laba[v * 2 + 1]


def update(arr, l, r, x):
    if l >= 0 and r <= len(arr):
        for i in range(l - 1, r):
            u(1, 0, len(arr) - 1, i, x)
        return laba
    else:
        Exception("ERROR")


def get(v, tl, tr, key):
    global k
    if tr == tl:
        if laba[v] == key:
            k += 1
        return
    tm = (tl + tr) // 2
    get(v * 2, tl, tm, key)
    get(v * 2 + 1, tm + 1, tr, key)
    return k
