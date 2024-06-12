from lucene.graphUsingDictionary2 import get_graph_dict


# graph = {
#     'person' : ['paper','organization','address'],
#     'paper' : ['organization','person'],
#     'organization' : ['address','person','paper'],
#     'address' : ['organization','person']
# }
# graph = {'person': ['paper', 'organization', 'address'], 'paper': ['person', 'prog_lang'], 'organization': ['paper', 'address', 'topic'], 'address': ['organization'], 'prog_lang': ['paper', 'topic'], 'topic': ['prog_lang']}
# print(graph_dict)
graph = get_graph_dict()

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

# print(find_shortest_path(graph, 'case_studies', 'proposals'))
# print("Shortest path is : ")
def get_src_and_target(src,target):
    source = src
    target = target
    return find_shortest_path(graph, source, target)

