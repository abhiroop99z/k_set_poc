from lucene.src_target_util import get_source_list, get_st_same_and_diff_list, get_target_list, st_diff_data, union_st_same
# from views import rdf_dict


from lucene.union_utils import get_union_of_papers
from lucene.globalClass import Loader

loader = Loader()

configs = loader.load_config()
rdf_dict = loader.load_rdf()

def findTargetedData(data1, source_list, target, rdf_dict):
    result1 = {}
    # print("findTargetedData target == ",target)
    if len(source_list) != 0:

        result1 = get_response(data1, source_list, target, rdf_dict)

    else:
        pass
    return result1

def get_response(data1, source, target, rdf_dict):
    # print("get response target == ",target)
    l = len(source)

    # getting source and target list
    src_lst = get_source_list(source)

    print("src_lst......",src_lst)

    target_lst = get_target_list(target)
    print("target_lst......", target_lst)

    # separating sources with same name as target
    st_same, st_diff = get_st_same_and_diff_list(src_lst,target)

    st_same_papers = []
    if len(st_same)!=0:
        st_same_papers = union_st_same(st_same)

    print("st_same --> ",st_same_papers)


    st_diff_papers = []
    # 1. finding shortest path between source and target and find relationship to get st_diff_data
    if len(st_diff)!=0:
        st_diff_papers = st_diff_data(st_diff,target_lst)

    final_paper_list = []
    for item in st_same_papers:
        final_paper_list.append(item)
    for item in st_diff_papers:
        final_paper_list.append(item)

    # print("final_paperList paper_res -->>> ",final_paper_list)
    
    paper_res = formatting_response(final_paper_list)
    # paper_res = formatting_response_multiple_target(final_paper_list)

    # removing duplicates
    # done = set()
    # paper_res_rem_dup = []
    # for d in paper_res:
    #     if d['name'] not in done:
    #         done.add(d['name'])  # note it down for further iterations
    #         paper_res_rem_dup.append(d)

    return paper_res
    # return final_paper_list


# added data1 and target_list in parameters
def get_union_target_all(data1, rdf_dict, exact_match_list, partial_match_list,target_list):
    all_target_papers = []
    for target in target_list:
        current_target_papers = get_union_of_papers(data1,target, rdf_dict,exact_match_list, partial_match_list)['paper_res']
        # print("type ---- ",(current_target_papers))
        all_target_papers = all_target_papers + current_target_papers

    return all_target_papers


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

def call_rdf(key,val):
    filter_name = []
    for filter_id in val:
        x = configs[key].data
        if x == "vertical.company.vertical_of_company":
            y = "company.literal.company_name"
        # elif x == "usecase.feedback.usecase_has_feedback":
        #     y = "usecase.company.usecase_of_company"
        else:
            y = x
        print(f"{key} configs--->>> ",configs[key].data)
        a = rdf_dict[filter_id][y]
        print(f"{configs[key]} rdf_data --->>> ",a)
        filter_name.append(a)

    str = ","
    # print("filterNamne --- >>> ",key , "  " ,filter_name)
    return str.join(filter_name)

def find_relationship_data(papers):
    print("papers --> ",papers)
    for item in papers:
        for key, val in item.items():
            if (type(val) is list) and (key!= 'path'):
                print(key , val)
                x = call_rdf(key,val)
                # has_technology_focus - technologyfocus
                # key = str(key).replace('_',' ').replace('has','').title()
                item[key] = x
                
    return papers


def formatting_response(applied_filters_papers):
    # print("length of applied_filters_papers -- ",len(applied_filters_papers))
    # paper_res = []
    papers = []
    for item in applied_filters_papers:
        dict3 = {}
        for key in item.keys():
            # if key != 'company.vertical.has_vertical' and key != 'company.technology_focus.has_technology_focus':
            if '.' in key:
                key_list = key.split('.')

                dict3[key_list[-1]] = item[key]
                # if configs[key].data :
                #     asset = configs[key].data
                #     print("asset ========= ",asset)
            else:
                # print("",)
                dict3[key] = item[key]
        papers.append(dict3)

        # break
    # print("papers in formting_resp --> ",papers)

    paper_res = find_relationship_data(papers)
    # print("papers.............................",papers)
    
    return paper_res

def formatting_response_multiple_target(applied_filters_papers):
    print("length of applied_filters_papers -- ",applied_filters_papers)
    # paper_res = []
    papers = []
    for item in applied_filters_papers:
        dict3 = {}
        for key in item.keys():
            # if key != 'company.vertical.has_vertical' and key != 'company.technology_focus.has_technology_focus':
            if '.' in key:
                key_list = key.split('.')
                updated_key = key_list[-1].replace("_"," ")
                dict3[updated_key] = item[key]
                # dict3[key_list[-1]] = item[key]
                # if configs[key].data :
                #     asset = configs[key].data
                #     print("asset ========= ",asset)
            else:
                # print("",)
                updated_key = key.replace("_"," ")
                dict3[updated_key] = item[key]
                # dict3[key] = item[key]
        papers.append(dict3)

    #     # break
    # # print("papers in formting_resp --> ",papers)

    # paper_res = find_relationship_data(papers)
    # print("papers.............................",papers)
    
    # return applied_filters_papers
    return papers


# deprecated - (uses hard coded approach)

def formatting_response_deprecated(applied_filters_papers):
    print("length of applied_filters_papers -- ",len(applied_filters_papers))
    # print(applied_filters_papers)
    paper_res = []
    for item in applied_filters_papers:
        dict1 = {}
        dict1['bot_rdf_id'] = item['bot_rdf_id']
        dict1['name'] = item['document.literal.content_title']
        dict1['doc_uuid'] = item['document.literal.content_uuid']
        dict1['description'] = item['document.literal.content_description']

        asset_lst = item['document.asset_type.of_asset_type']
        asset_lst_name = []
        for asset_id in asset_lst:
            asset = rdf_dict[asset_id]['asset_type.literal.asset_name']
            asset_lst_name.append(asset)

        # dict1['asset'] = asset_lst_name

        str = ","
        dict1['asset'] = str.join(asset_lst_name)
        # dict1['asset_for_filter'] = asset_lst_name

        channel_lst = item['document.channel.of_channel']
        channel_lst_name = []
        for channel_id in channel_lst:
            channel = rdf_dict[channel_id]['channel.literal.channel_name']
            channel_lst_name.append(channel)

        # dict1['asset'] = asset_lst_name

        str = ","
        dict1['channel'] = str.join(channel_lst_name)
        # dict1['channel_for_filter'] = channel_lst_name

        area_lst = item['document.area.of_area']
        area_lst_name = []
        for area_id in area_lst:
            area = rdf_dict[area_id]['area.literal.area_name']
            area_lst_name.append(area)

        # dict1['asset'] = asset_lst_name

        str = ","
        dict1['area'] = str.join(area_lst_name)
        # dict1['area_for_filter'] = area_lst_name

        collection_lst = item['document.collection.of_collection']
        collection_lst_name = []
        for collection_id in collection_lst:
            collection = rdf_dict[collection_id]['collection.literal.collection_name']
            collection_lst_name.append(collection)

        # dict1['asset'] = asset_lst_name

        str = ","
        dict1['collection'] = str.join(collection_lst_name)
        # dict1['collection_for_filter'] = collection_lst_name

        subject_lst = item['document.subject.of_subject']
        subject_lst_name = []
        for subject_id in subject_lst:
            subject = rdf_dict[subject_id]['subject.literal.subject_name']
            subject_lst_name.append(subject)

        # dict1['asset'] = asset_lst_name

        str = ","
        dict1['subject'] = str.join(subject_lst_name)
        # dict1['subject_for_filter'] = subject_lst_name

        technology_lst = item['document.technology.of_technology']
        # print(type(technology_lst))
        technology_lst_name = []
        for technology_id in technology_lst:
            technology = rdf_dict[technology_id]['technology.literal.technology_title']
            # print(type(technology))
            technology_lst_name.append(technology)

        # print("technology_lst_name::::::::",technology_lst_name)
        # dict1['asset'] = asset_lst_name

        str = ","
        dict1['technology'] = str.join(technology_lst_name)
        # dict1['technology_for_filter'] = technology_lst_name

        # print("path in output..............................")
        # print(item['path'])
        dict1['shortest_path'] = item['path']
        paper_res.append(dict1)

    return paper_res