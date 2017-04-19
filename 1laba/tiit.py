from funcs import get, build, update
from tests import test


def main(k=0):
    for t in enumerate(test):
        print("====================== Test", str(t[0]+1),"================================================")
        arr = t[1]["arr"]
        start1, end1, value1 = t[1]["update"]
        value2 = t[1]["search"]
        build(arr)
        print("Количество элементов, равных", value2,"\n", get(1, 0, len(arr) - 1, value2))
        print("Каждый элемент, начиная с",start1," и заканчивая",end1,"изменили на", value1,
              "\n", update(arr, start1, end1, value1))


main()
