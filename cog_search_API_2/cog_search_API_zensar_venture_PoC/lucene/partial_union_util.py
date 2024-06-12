from lucene.documents_resp_util import findTargetedData
from lucene.util_functions import *

def get_union_of_partial_src(data1, source_list, target,rdf_dict):
    partial_union = []
    for i, source in enumerate(source_list):
        src_lst = []
        src_lst.append(source)
        # print("current target in loop ...",target)
        current_src_papers = findTargetedData(data1, src_lst, target, rdf_dict)
        # temp = temp + current_src_papers
        # [s1,s2,s3..]
        partial_union = partial_union + current_src_papers

    return partial_union