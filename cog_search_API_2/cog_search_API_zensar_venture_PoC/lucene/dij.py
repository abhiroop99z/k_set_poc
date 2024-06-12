from collections import defaultdict
from heapq import *

from lucene.graphUsingDictionary2 import *




def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None

def get_graphList(tup):
    tup_list = []

    for i, item in enumerate(tup):
        if i >= 1:
            # print("item ->", item)
            # print(item[0])
            tup_list.append(item[0])

            for j, item2 in enumerate(item[1]):
                # print("item2 ->", item2)
                if j == 0:
                    tup_list.append(item2)

    return tup_list

def get_src_and_target(src, target):
    source = src
    target = target

    tup1 = dijkstra(edges, source, target)
    print("--------------------")
    tup_list = get_graphList(tup1)
    tup_list.reverse()
    print(tup_list)
    return tup_list

def src_and_target(src, target):
    source = src
    target = target
    return source,target


a = {'customer': ['proposals', 'case_studies'], 'proposals': ['customer'], 'case_studies': ['customer']}

al = [('customer', 'proposals'), ('customer', 'case_studies'), ('proposals', 'customer'), ('case_studies', 'customer')]

# if __name__ == "__main__":
    # g = [('customer', 'proposals'), ('customer', 'case_studies'), ('proposals', 'customer'),
    #      ('case_studies', 'customer')]


get_graph  = edges_2
# print(get_graph)
edges = []
for i in get_graph:
    i = list(i)
    i.append(1)
    i = tuple(i)
    print(i)
    edges.append(i)

# print("=== Dijkstra ===")
# print(edges)
# print("customer -> proposals")
# print(dijkstra(edges, "customer", "proposals"))
# print("case_studies -> proposals")
# print(dijkstra(edges, "case_studies", "proposals"))



# print("GST -> ",get_src_and_target('customer','proposals'))


# tup = (get_src_and_target('customer','case_studies'))


    #             print("item222 ->",item2[2])

    #             for k,item3 in enumerate(item2[1]):
    #                 print("item3 ->",item3)
    #                 if k==0:
    #                     tup_list.append(item3)

    # print(tup_list)

# print(get_src_and_target('customer','case_studies'))
