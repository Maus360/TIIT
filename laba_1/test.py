def print_tree(t):
    if t != None:
        print_tree(t.l)
        print(t.value)
        print_tree(t.r)


class tree(object):
    def __init__(self):
        self.value = None
        self.l = None
        self.r = None

    def add(self, val):
        if self.value is None:
            self.value = val

        if self.value > val:
            self.l = tree()
            self.l.add(val)

        if self.value < val:
            self.r = tree()
            self.r.add(val)

    def print_tree(self):
        if self.value is not None:
            try:
                self.l.print_tree()
            except:
                print("ERROR")
            print(self.value)
            try:
                self.r.print_tree()
            except:
                print("ERROR")

    def find(self, v):
        if self.value == v:
            print('match!')

        if v < self.value:
            try:
                find(self.l, v)
            except:
                print("No match")
        if v > self.value:
            try:
                find(self.r, v)
            except:
                print("No match")


arr = [1, 2, 3, 4, 5, 6, 7, 8, -5, -10, -3]
print(arr)