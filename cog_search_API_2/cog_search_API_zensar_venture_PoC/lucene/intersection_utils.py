import itertools
from lucene.documents_resp_util import *
from lucene.documents_resp_util import findTargetedData
from lucene.partial_union_util import *

intersect = []

def get_papers_after_intersection(data1, source_list, target):
    global intersect
    # abc = []
    # print("get_papers_after_intersection target== ",target)
    # intersect = []
    # if len(source_list) != 0:
    for i, source in enumerate(source_list):
        src_lst = []
        src_lst.append(source)
        # print("current target in loop ...",target)
        current_src_papers = findTargetedData(data1,src_lst,target,rdf_dict)
        # abc = abc + current_src_papers
        # print("current_src_papers ->>",current_src_papers)
        if i == 0:
            intersect = current_src_papers
            # hm = HashMap
        else:
            intersect = do_intersection(intersect, current_src_papers)
        # print(" i and source  -------> ",i ,"--->" , source)
        # print(" intersect -----> ")
        # print(len(intersect))
        # print("--------------------------------------------------")
    print("final intersection result.................")
    print(len(intersect))
    # print(intersect)

    # print("current_papers -->",abc)
    return intersect


def do_intersection(intersect,final_result1_paper_res):
    # print("final_result1_paper_res ----> ",final_result1_paper_res)
    counts = {d2['bot_rdf_id'] for d2 in final_result1_paper_res}
    list3 = [d for d in intersect if d['bot_rdf_id'] in counts]

    return list3


def intersection_list(src_list):
    l = list(itertools.chain(*src_list))
    a = []
    for item in l:
        if item["bot_rdf_id"] not in a:
            a.append(item["bot_rdf_id"])
    result = [x for x in l if x["bot_rdf_id"] in a]

    return result

    # added data1  in parameters
def paper_with_target_all(data1,source_list,target_list,flag):
    # print("target_list 2 --> ",target_list)

    if flag == 0:

        all_target_papers = []
        for target in target_list:
            # print("target in target list --> ",target)
            current_target_papers = get_papers_after_intersection(data1,source_list,target)
            # print("intersection")
            # print("current_target_papers -- > ",current_target_papers)
            all_target_papers = all_target_papers + current_target_papers
    # print("all_target_papers -- > ", all_target_papers)

    elif flag ==1:
        all_target_papers = []
        for target in target_list:
            # print("target in target list --> ",target)
            current_target_papers = get_union_of_partial_src(data1,source_list,target,rdf_dict)
            # print("intersection")
            # print("current_target_papers -- > ",current_target_papers)
            all_target_papers = all_target_papers + current_target_papers


    return all_target_papers