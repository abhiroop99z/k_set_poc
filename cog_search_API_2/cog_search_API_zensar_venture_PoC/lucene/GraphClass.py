from collections import defaultdict

import pandas as pd


class GraphClass():
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = []
        self.graph_dict = {}

    def addEdge(self,graph, u, v):
        graph = self.graph
        graph[u].append(v)
    
    def generate_edges(self,graph):
        edges = self.edges
        
        # for each node in graph
        for node in self.graph:

            # for each neighbour node of a single node
            for neighbour in graph[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        
        return edges

    def get_graph_dict(self):
        return dict(self.graph)

    def get_graph_from_schema(self,schema_file_path,sheet_name):

        schema_df = pd.read_excel(schema_file_path, sheet_name)

        for index,row in schema_df.iterrows():

            if(row["Entity/Concept"] == row["Entity/Concept"]):
                key = row["Entity/Concept"]

            if(row["Obj Type"] == "reference"):
                self.graph_dict[key]=row["Type"]
                self.addEdge(self.graph, key, row["Type"])

        print("Graph_dict --->>>",self.graph_dict)

        return self.graph_dict

graphClass_obj = GraphClass()
get_graph = graphClass_obj.get_graph_from_schema("C:/Users/ak59584/Downloads/cog_search_API_zensar_venture_PoC/lucene/schema.xlsx", 'Sheet1')
graph_dict = graphClass_obj.get_graph_dict()

# print()
# print(graph_dict)


class PathTraversal():
    def __init__(self):
        self.graph = graph_dict

    def find_shortest_path(self,graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def get_src_and_target(self,src,target):
        source = src
        target = target
        return self.find_shortest_path(self.graph, source, target)

