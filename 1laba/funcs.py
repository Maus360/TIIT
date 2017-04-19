
class tree():
    def __init__(self, arr):
        self.laba = [0]*4*len(arr)
        self.arr = arr
    def b(self,arr, v, tl, tr):
        if (tl == tr):
            self.laba[v] = self.arr[tl]
        else:

            tm = (tl + tr) // 2
            self.b(arr, v * 2, tl, tm)
            self.b(arr, v * 2 + 1, tm + 1, tr)
            self.laba[v] = self.laba[v * 2] + self.laba[v * 2 + 1]


    def build(self):

        laba = [0] * len(self.arr) * 4
        self.b(self.arr, 1, 0, len(self.arr) - 1)
        print(self.laba)


    def u(self, v, tl, tr, pos, add):
        if tl == tr:
            self.laba[v] += add
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.u(v * 2, tl, tm, pos, add)
            else:
                self.u(v * 2 + 1, tm + 1, tr, pos, add)
            self.laba[v] = self.laba[v * 2] + self.laba[v * 2 + 1]


    def update(self, l, r, x):

        if l >= 0 and r <= len(self.arr):
            for i in range(l - 1, r):
                self.u(1, 0, len(self.arr) - 1, i, x)
            return self.laba
        else:
            Exception("ERROR")


    def get(self, key):
        self.k = 0
        return self.g(1, 0, len(self.arr)-1, key)


    def g(self, v, tl, tr, key):
        if tr == tl:
            if self.laba[v] == key:
                self.k += 1
            return
        tm = (tl + tr) // 2
        self.g(v * 2, tl, tm, key)
        self.g(v * 2 + 1, tm + 1, tr, key)
        return self.k
