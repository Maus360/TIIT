from funcs import tree
from tests import test


def main(k=0):
    for t in enumerate(test):
        print("====================== Test", str(t[0]+1),"================================================")
        Maks = tree(t[1]["arr"])
        start1, end1, value1 = t[1]["update"]
        value2 = t[1]["search"]
        Maks.build()
        print("Количество элементов, равных", value2,"\n", Maks.get(value2))
        print("Каждый элемент, начиная с",start1," и заканчивая",end1,"изменили на", value1,
              "\n", Maks.update(start1, end1, value1))


main()
