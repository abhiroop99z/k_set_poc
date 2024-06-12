from collections import defaultdict

def applied_filters(data1):

    filters_name = {}
    if 'filters' in data1.keys():
        filters_name = data1['filters']
        # print(filters_name)

    else:
        filters_name = {}

    return filters_name

def applied_filters_backup(data1):

    filters_name = {}
    if 'filters' in data1.keys():
        for j,key in enumerate(filter.keys()):

            x = ('{}_dict').format(key)
            # print(x)
            x = data1["filters"][j]
            # print(x)
            key1 = x["values"]
            filters_name[key] = key1
        # print(filters_name)

    else:
        for key in filter.keys():
            # key = []
            filters_name[key]=[]

    return filters_name
    # return filters_name[0], filters_name[1], filters_name[2], filters_name[3], filters_name[4], filters_name[4]


# def apply_filter(papers_list, filters_dict):
#     paper_result = []  # to be returned, a list of dicts

#     for d in papers_list:
#         check_key_list = []
#         n = 0  # count how many key/value pairs matches with filterDict
#         for key, val in filters_dict.items():

#             for v in val:
#                 # print(v)

#                 val_list = d[key].split(',')
#                 # for i in x:

#                 try:  # in case key is missing
#                     # print("i--->",i,v)
#                     if v in val_list:
#                         if key not in check_key_list:
#                             check_key_list.append(key)
#                             # print(v)
#                             n += 1
#                             # print("n incremented")
#                 except:
#                     pass  # change with a proper error message
#         # print(n, len(filters_dict))
#         if n == len(filters_dict):  # if True then all the key/value pairs in filterDict are in d
#             paper_result.append(d)
#     #         print("paper_Result== ",paper_result)
#     # print("length of result --> ", len(paper_result))
#     return paper_result

def apply_filter(papers_list, filters_dict):
    paper_result = []  # to be returned, a list of dicts

    for d in papers_list:
        check_key_list = []
        n = 0  # count how many key/value pairs matches with filterDict
        for item in filters_dict:
            # print("item of filters_dict -> ",item)
            for key,val in item.items():
                # print("val of item",val)
                for v in val:
                    # print(v)

                    val_list = d[key].split(',')
                    # for i in x:

                    try:  # in case key is missing
                        # print("i--->",i,v)
                        if v in val_list:
                            if key not in check_key_list:
                                check_key_list.append(key)
                                # print(v)
                                n += 1
                                # print("n incremented")
                    except:
                        pass  # change with a proper error message
        # print(n, len(filters_dict))
        if n == len(filters_dict):  # if True then all the key/value pairs in filterDict are in d
            paper_result.append(d)
    #         print("paper_Result== ",paper_result)
    # print("length of result --> ", len(paper_result))
    return paper_result


def check_for_filters(data1, final_paper_list):
    f = applied_filters
    filters = applied_filters(data1)
    # print("length of final_paper_list--> ",len(final_paper_list))
    # print("filters ------------------",filters)
    papers = apply_filter(final_paper_list,filters)
    return papers


def get_filters(filters_result):
    filters_list = []
    for key,value in filters_result.items():
        filter_dict = {}
        filter_dict["name"] = key
        key2 = str(key).replace('has_','').replace('_',' ').title()

        filter_dict['ui_name'] = key2
        # has_technology_focus
        filter_dict["type_of_value"] = value
        filter_dict["values"] = []
        filters_list.append(filter_dict)
    return filters_list


def get_filters_from_paper_res(filters_dict,paper_res):
    # filters_dict  ->  from application.properties file
    filters_dict_with_list = defaultdict(list)
    filters_result = {}
    for item in paper_res:
        for key,value in item.items():       
            if key in filters_dict.keys():
                filters_dict_with_list[key].append(value)

    for item in filters_dict_with_list.items():
        filter_value_list = []
        for i in item[1]:
            i = i.split(",")
            for a in i:
                a = " ".join(a.split())
                if a != '':
                    filter_value_list.append(a)
        
        filters_result[item[0]] = list(set(filter_value_list))

    result = get_filters(filters_result)
    # print("Filters result -->>> ",result)
    
    return result