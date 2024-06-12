# from lucene.documents_resp_util import findTargetedData, get_final_result
from lucene.util_functions import *
import lucene.documents_resp_util as d

def get_union(data1,source_list,target, rdf_dict):
    if len(source_list) != 0:
        union = []
        for i, source in enumerate(source_list):
            src_lst = []
            src_lst.append(source)
            current_src_papers = d.findTargetedData(data1, src_lst,
                                                  target, rdf_dict)
            union = union + current_src_papers
        # print("union of papers................")
        # print(union)

        return union

def get_union_of_papers(data1,target, rdf_dict,exact_match_list, partial_match_list):
    exact_src_papers_union = []
    partial_src_papers_union = []
    if(len(exact_match_list)!= 0):
        exact_src_papers_union = get_union(data1,exact_match_list,target, rdf_dict)
        print("exact_src_papers_union---> ",len(exact_src_papers_union))
    if (len(partial_match_list) != 0):
        partial_src_papers_union = get_union(data1,partial_match_list,target, rdf_dict)
        print("partial_src_papers_union---> ", len(partial_src_papers_union))
    final_result = d.get_final_result(exact_src_papers_union,partial_src_papers_union)
    return final_result
