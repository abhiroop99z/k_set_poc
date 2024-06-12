# import re
# import distance
#
# # print(distance.jaccard("proposals", "prop"))
# query = "show me proposals"
# target = ["proposals","case studies"]
# query_lst = ["show", "me", "proposal"]
#
# def patternMatching(query,target):
#     for t in target:
#         if t.lower() in query.lower():
#             print("target --> ",t)
#
#             return t
#         else:
#             pass
#
# def similarityMatch(query_lst,target):
#     dist = []
#     for t in target:
#         for q in query_lst:
#             t_q_dict = {}
#             t_q_dict['t_q'] = t + " " + q
#             t_q_dict['distance'] = distance.jaccard(t, q)
#             dist.append(t_q_dict)
#
#     print(dist)
#     return dist
#
# print("pattern matching target found " , patternMatching(query,target))
# print("similarity matching target found " , similarityMatch(query_lst,target))

# s = "When analyzing the business problems, or internal processes, that exist in your organization, you must be knowledgeable in the characteristics, required competencies, methodologies and analytics tools involved. Youll also need to understand how different business analysis perspectives apply or can be combined depending on your organizations context."
# print(len(s))