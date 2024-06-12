from collections import defaultdict
# from source_identifier import identify_source
import pandas as pd


graph = defaultdict(list)

def addEdge(graph, u, v):
    graph[u].append(v)


def generate_edges(graph):
    edges = []

    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for neighbour in graph[node]:
            # if edge exists then append
            edges.append((node, neighbour))
    return edges


f2 = pd.read_excel('lucene\schema.xlsx', 'Sheet1')

graph_dict = {}

for index,row in f2.iterrows():

    if(row["Entity/Concept"] == row["Entity/Concept"]):
        key = row["Entity/Concept"]
        # print(key)

    if(row["Obj Type"] == "reference"):
        # print(row["Type"])
        # print(key)
        graph_dict[key]=row["Type"]
        # print(graph_dict)
        addEdge(graph, key, row["Type"])

# print(graph_dict)




def get_graph_dict():
    return dict(graph)
print(dict(graph))



# Driver Function call
# to print generated graph
# print("graph is..")
edges_2 = generate_edges(graph)
# print(generate_edges(graph))