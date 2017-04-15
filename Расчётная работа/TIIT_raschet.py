from tests_for_tiit import *

graph = {
    2: {3, 4, 5},
    3: {2, 4}
}


def Stas(graph, graph1=None):
    if graph1 == None:
        graph1 = dict()
    if graph1 is None:
        graph1 = dict()
    for i in graph:
        for j in graph[i]:
            try:
                a = graph[j]
            except:
                try:
                    a = graph1[j]
                except:
                    a = set()
            # print(a)
            # print(graph[i])
            a = a.union({i})
            graph1[j] = a
            # print("*****************")
            # print(graph1)
            # print("-----------------")
    return graph1


def union(graph1, graph2):
    graph0 = dict()
    for i in graph1:
        try:
            graph0[i] = graph1[i].union(graph2[i])
        except:
            graph0[i] = graph1[i]

    for i in graph2:
        try:
            graph0[i] = graph1[i].union(graph2[i])
        except:
            graph0[i] = graph2[i]

    return graph0


graph = Stas(graph)
new_graph = {1: {2, 7}}
new_graph.update(Stas(new_graph))

for i in tests:
    i[0] = Stas(i[0])
    print(i[0])
    print("--------+---------")
    i[1] = Stas(i[1])
    print(i[1])
    print("--------=---------")
    print(union(i[0], i[1]))
    print("******************")
