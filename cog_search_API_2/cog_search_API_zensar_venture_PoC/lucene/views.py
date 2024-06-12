import json
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from jproperties import Properties
from rest_framework.parsers import JSONParser

from lucene.filters_util import *
from lucene.documents_resp_util import *
from lucene.source_identifier_util import *
from lucene.union_utils import *
from lucene.util_functions import *
from lucene.intersection_utils import *
from lucene.src_target_util import *

from lucene.globalClass import Loader

loader = Loader()

configs = loader.load_config()
rdf_dict = loader.load_rdf()
filter = loader.load_filters()
target_list = loader.load_target_list()

data1 = {}

lucene_sources = []
final_result_paper_res = []


filter_len = len(filter)


def get_final_result(exact_src_after_inter, partial_src_after_inter):
    final_result = {}
    # check length of src list -- may be
    if len(exact_src_after_inter) >= 1 and len(partial_src_after_inter) >= 1:
        # take intersection
        final_result['paper_res'] = [x for x in exact_src_after_inter if
                                     x["bot_rdf_id"] in [b["bot_rdf_id"] for b in partial_src_after_inter]]

        print("******************************************************")
        print("intersection result...............")


    elif len(exact_src_after_inter) >= 1 and len(partial_src_after_inter) == 0:
        final_result['paper_res'] = exact_src_after_inter
        print("result1...............")
        # print(final_result)

    else:
        final_result['paper_res'] = partial_src_after_inter
        # fina
        print("result2...............")
    

    return final_result


# def get_union_of_partial_src(data1, source_list, target):
#     partial_union = []
#     for i, source in enumerate(source_list):
#         src_lst = []
#         src_lst.append(source)
#         # print("current target in loop ...",target)
#         current_src_papers = findTargetedData(data1, src_lst, target, rdf_dict)
#         # temp = temp + current_src_papers
#         # [s1,s2,s3..]
#         partial_union = partial_union + current_src_papers

#     return partial_union

@csrf_exempt
def searchApi(request):
    global data1
    data1 = JSONParser().parse(request)
    query = data1['query']
    target = data1['target']

    # asset, channel, area, collection, subject, technology = applied_filters(data1)

    # call lucene to get all sources
    all_src_list = call_lucene(query)
    print("all_src_list : ",all_src_list)
    # Removing duplicate sources
    all_src_list = remove_duplicates(all_src_list)

    # lowercasing the query
    q = query.lower()

    q_list = q.split()

    # Identifies the exact source for the given user query and hence appends the value in exact_match_list.
    # example -> query : Bank of England testing , exact_match_string_list = ["bank of england"]
    exact_match_list,exact_match_string_list = get_exact_match_src(all_src_list, q)
    # print("printing exact source list...........")
    # print(exact_match_list)
    # print(exact_match_string_list)
    # print(len(exact_match_list))

    # remove full src found from query
    new_query = remove_exact_match_from_query(q,exact_match_string_list)

    new_query = new_query.strip(" ")
    rem_query = list(new_query.split(" "))
    print("rem_query => ", rem_query)

    # Identifying partial src
    partial_match_list = get_partial_match_src(all_src_list,new_query,rem_query)
    print("printing partial source list...........")
    # print(partial_match_list)
    print(len(partial_match_list))

    # if target == 'All'
    if target == 'All':
        exact_src_after_inter = paper_with_target_all(data1,exact_match_list,target_list,flag=0)
    else:

        # getting papers after intersection for both exact sources as well as partial sources
        if len(exact_match_list)!= 0:
            exact_src_after_inter = get_papers_after_intersection(data1,exact_match_list,target)
        else :
            exact_src_after_inter = []
    print("exact_src_after_inter -->")
    print(len(exact_src_after_inter))


    # Partial match opertaions

    if target == 'All':
        partial_src_after_inter = paper_with_target_all(data1,partial_match_list,target_list,flag=1)
    else:
        if len(partial_match_list)!= 0:
            # partial_src_after_inter = get_papers_after_intersection(data1,partial_match_list,target)
            partial_src_after_inter = get_union_of_partial_src(data1,partial_match_list,target,rdf_dict)
        else :
            partial_src_after_inter = []
    print("partial_src_after_inter -->")
    print(len(partial_src_after_inter))

    # final result ie papers with filters
    final_result = get_final_result(exact_src_after_inter,partial_src_after_inter)

    x = final_result['paper_res']
    # print("x above----- ", len(x))
    if 'filters' in data1.keys():
        # print("x filters if----- ", len(x))
        final_result['paper_res'] = check_for_filters(data1, x)
    else:
        final_result['paper_res'] = x
    # print("x final----- ", len(x))


    # print("union target ",target)


    if len(final_result['paper_res']) == 0:
        if target == 'All':
            final_result_papers = get_union_target_all(data1, rdf_dict,exact_match_list, partial_match_list,target_list)
            final_result['paper_res'] = final_result_papers
        else:
        # go for union of results
            final_result = get_union_of_papers(data1,target, rdf_dict,exact_match_list, partial_match_list)
        # print(final_result['paper_res'][1:4])
        x = final_result['paper_res']
        # print("x union --- ",len(final_result['paper_res']))
        if 'filters' in data1.keys():
            # print("x in union filter",len(x))
            final_result['paper_res'] = check_for_filters(data1, x)
        else:
            final_result['paper_res'] = x
        # print("x final union",len(x))
        # final_result['paper_res'] = check_for_filters(data1,final_result['paper_res'])
    dummy_paper_res = final_result['paper_res']

    # final_result["filters"] = get_filters_from_paper_res(filter, final_result['paper_res'])
    final_result["filters"] = []

    final_result['paper_res'] = remove_duplicate_papers(final_result['paper_res'])
    # for item in dummy_paper_res:
    #     for key in item.keys():
    #         if key in filter.keys():
    #             # print("key --->",key)

    # print("filter in views -->> ",filter )
    final_result["filters"] = get_filters_from_paper_res(filter, final_result['paper_res'])

    # final_result['paper_res'] = remove_duplicate_papers(final_result['paper_res'])
    # papers = final_result['paper_res']
    # exact_match_string_list1 = ["Human Resource"]
    # pprs_with_rank = ranking(q_list,papers,exact_match_string_list,rem_query)
    # pprs_with_rank = papers
    # pprs_sort_by_score = sort_by_score(pprs_with_rank)
    # final_result['paper_res'] = pprs_with_rank
    # final_result['paper_res'] = papers

    return JsonResponse(final_result, safe=False, status=200)

@csrf_exempt
def targetList(request):
    if request.method == "POST":
        # data1 = JSONParser().parse(request)
        res = {}
        for item in target_list:
            # if "_" in item:
            #     item = item.split()
            #     print(item)
            # res[item] = item.capitalize()
            item2 = item.replace('_',' ').title()
            res[item2] = item
        # print("res --> ",res)
        return JsonResponse(res, safe=False, status=200) 

@csrf_exempt
def dummy_Func(request):
    auto_suggest = defaultdict(list)
    auto = []
    if request.method == "POST":
        data1 = JSONParser().parse(request)
        query = data1['query']

        if len(query) == 0:
            return

        for item in rdf_dict:
            if item.startswith('bot.1'):

                if query.lower() in rdf_dict[item]['document.literal.content_title'].lower():
                    value = (rdf_dict[item]['type.is_a']).split('entity.')
                    auto_suggest[rdf_dict[item]['document.literal.content_title']].append(value)

            elif item.startswith('bot.2'):

                if query.lower() in rdf_dict[item]['asset_type.literal.asset_name'].lower():
                    value = (rdf_dict[item]['type.is_a']).split('entity.')
                    auto_suggest[rdf_dict[item]['asset_type.literal.asset_name']].append(value)

            elif item.startswith('bot.3'):

                if query.lower() in rdf_dict[item]['channel.literal.channel_name'].lower():
                    # auto.append(rdf_dict[item]['case_studies.literal.name'])
                    value = (rdf_dict[item]['type.is_a']).split('entity.')
                    auto_suggest[rdf_dict[item]['channel.literal.channel_name']].append(value)

            elif item.startswith('bot.4'):

                if query.lower() in rdf_dict[item]['area.literal.area_name'].lower():
                    # auto.append(rdf_dict[item]['case_studies.literal.name'])
                    value = (rdf_dict[item]['type.is_a']).split('entity.')
                    auto_suggest[rdf_dict[item]['area.literal.area_name']].append(value)

            elif item.startswith('bot.5'):

                if query.lower() in rdf_dict[item]['collection.literal.collection_name'].lower():
                    # auto.append(rdf_dict[item]['case_studies.literal.name'])
                    value = (rdf_dict[item]['type.is_a']).split('entity.')
                    auto_suggest[rdf_dict[item]['collection.literal.collection_name']].append(value)

            elif item.startswith('bot.6'):

                if query.lower() in rdf_dict[item]['subject.literal.subject_name'].lower():
                    # auto.append(rdf_dict[item]['case_studies.literal.name'])
                    value = (rdf_dict[item]['type.is_a']).split('entity.')
                    auto_suggest[rdf_dict[item]['subject.literal.subject_name']].append(value)

            elif item.startswith('bot.7'):

                if query.lower() in rdf_dict[item]['technology.literal.technology_title'].lower():
                    # auto.append(rdf_dict[item]['case_studies.literal.name'])
                    value = (rdf_dict[item]['type.is_a']).split('entity.')
                    auto_suggest[rdf_dict[item]['technology.literal.technology_title']].append(value)


    return JsonResponse(auto_suggest, safe=False, status=200)

