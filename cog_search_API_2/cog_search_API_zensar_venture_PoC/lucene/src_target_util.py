
from lucene import GraphClass
# from lucene.path_traversal import get_src_and_target

from lucene.globalClass import Loader

loader = Loader()

shrts_path_obj = GraphClass.PathTraversal()


configs = loader.load_config()
rdf_dict = loader.load_rdf()



# configs = Properties()
# with open('lucene/application.properties', 'rb') as config_file:
#     configs.load(config_file)


# # global rdf_dict
# file = open(configs['RDF_JSON'].data)
# rdf_dict = json.load(file)



def get_source_list(source):
    l = len(source)
    src_lst = []
    for i in range(l):
        src_dic = {}
        src_dic["bot_rdf_id"] = source[i]["bot_rdf_id"]
        lst = []
        lst = source[i]["type.is_a"].split(".")
        src_dic["entity_type"] = lst[1]
        src_lst.append(src_dic)

    return src_lst


def get_target_list(target):
    target_lst = []
    target_lst.append(target)
    return target_lst


def get_st_same_and_diff_list(src_lst,target):
    st_same = []
    st_diff = []
    for item in src_lst:
        if item['entity_type'] == target:
            st_same.append(item)
        else:
            st_diff.append(item)

    for item in st_same:
        item['path'] = []
        item['path'].append(item['entity_type'])
        item['path'].append(target)

    for item in st_diff:
        # print(item)
        item['path'] = []
        item['path'].append(item['entity_type'])
        item['path'].append(target)

    return st_same,st_diff


def union_st_same(st_same):
    union_result = []
    if len(st_same) != 0:
        for item in st_same:
            st_same_data = rdf_dict[item['bot_rdf_id']]
            st_same_data['path'] = item['path']
            st_same_data['bot_rdf_id'] = item['bot_rdf_id']
            union_result.append(st_same_data)
    # print("union st_same -->> ", union_result)
    return union_result


def st_diff_data(st_diff,target_lst):
    shortest_path_lst = []
    result = []
    relationship = []
    result2 = []
    # print("target_lst ====== ",target_lst)

    # 
    if (len(st_diff) != 0):
        for i in range(len(st_diff)):
            # print("shortest path is...")
            # shortest_path = get_src_and_target(st_diff[i]["entity_type"], target_lst[0])
            shortest_path = shrts_path_obj.get_src_and_target(st_diff[i]["entity_type"], target_lst[0])
            st_diff[i]['path'] = shortest_path
            shortest_path_lst.append(shortest_path)

        shortest_path_lst1 = []
        [shortest_path_lst1.append(x) for x in shortest_path_lst if x not in shortest_path_lst1]
        print("shortest_path_lst1-----------> ",shortest_path_lst1)

        for path in shortest_path_lst1:
            for i in range(len(path)):
                if (i + 1 < len(path)):
                    relation = path[i] + "." + path[i + 1]
                    relationship.append(relation)
        print("relationship--------------> ",relationship)

        if len(st_diff) != 0:
            for item in st_diff:
                st_diff_data = rdf_dict[item['bot_rdf_id']]
                st_diff_data['path'] = item['path']
                st_diff_data['bot_rdf_id'] = item['bot_rdf_id']
                result2.append(st_diff_data)
        res_keys = set().union(*(d.keys() for d in result2))
        res_keys = list(res_keys)
        # result = []
        print("result2 ---> ",result2)
    #     for relation in relationship:
    #         result = []
    #         print("relation in relationship --> ",relation)
    #         # company.usecase
    #         for i in result2:
    #             for key in i.keys():
    #                 if (key.startswith(relation)):
    #                     print("key --> relation",key,relation)
    #                     bots_list = i[key]
    #                     print("bots_list --> " ,bots_list)
    #                     for ids in bots_list:
    #                         rdf_dict[ids]["bot_rdf_id"] = ids
    #                         st_diff_data1 = rdf_dict[ids]
    #                         st_diff_data1['path'] = i['path']
    #                         result.append(st_diff_data1)
    # # print("result ------>>> ",result)

        # for relation in relationship:
        #     result = []

        if len(relationship)== 1:
            for relation in relationship:
                result = []
                print("relation in relationship --> ",relation)
                # company.usecase
                for i in result2:
                    for key in i.keys():
                        if (key.startswith(relation)):
                            print("key --> relation",key,relation)
                            bots_list = i[key]
                            print("bots_list --> " ,bots_list)
                            for ids in bots_list:
                                rdf_dict[ids]["bot_rdf_id"] = ids
                                st_diff_data1 = rdf_dict[ids]
                                st_diff_data1['path'] = i['path']
                                result.append(st_diff_data1)
                result = [result]
        else :           
            print("relation in relationship --> ",relationship[0])
                # company.usecase
            
            # for i in result2:
            #     for key in i.keys():
            #         if (key.startswith(relationship[0])):
            #             print("key --> relation",key,relationship[0])
            #             bots_list = i[key]
            #             print("bots_list --> " ,bots_list)
            #             for ids in bots_list:
            #                 print("id in botlist --> ",ids)
            #                 # rdf_dict[ids]["bot_rdf_id"] = ids
            #                 st_diff_data1 = rdf_dict[ids]

            #                 print("st_diff_data1 --> ",st_diff_data1)
            #                 for k in st_diff_data1.keys():
            #                     print("2nd relation  --> ",relationship[1],k)
            #                     if (k.startswith(relationship[1])):
            #                         bots_list2 = st_diff_data1[k]
            #                         print("bots_list --> " ,bots_list2)
            #                         for ids2 in bots_list2:
            #                             rdf_dict[ids2]["bot_rdf_id"] = ids2
            #                             st_diff_data12 = rdf_dict[ids2]
            #                             st_diff_data12['path'] = i['path']
            #                             result.append(st_diff_data12)

    
            # for r_index in range(relationship):
            print("relation ")
            st_diff_data1 = {}
            for i in result2:

                for r_index in range(len(relationship)):
                    print("r_index, relationship ",r_index,relationship[r_index])
                    if r_index == 0:
                        st_diff_data1 = abc([i],r_index,relationship)
                    else:
                        st_diff_data1 = abc(st_diff_data1,r_index,relationship)
                # xyz.append()    
            st_diff_data12 = st_diff_data1
            
            result.append(st_diff_data12)



    print("result ------>>> ",result)
    return result[0]

def abc(st_diff_data1,r_index,relationship):
    xyz = []
    for i in st_diff_data1:

    #     for r_index in range(len(relationship)):
    #         print("r_index, relationship ",r_index,relationship[r_index])
    #         st_diff_data1 = {}
        for key in i.keys():
            # company.usecase
            print("key in i.keys -- ",key)
            if (key.startswith(relationship[r_index])):
                print("key --> relation",key,relationship[r_index])
                bots_list = i[key]
                print("bots_list --> " ,bots_list)
                # 79,72
                for ids in bots_list:
                    print("id in botlist --> ",ids)
                    # if "bot_r"
                    rdf_dict[ids]["bot_rdf_id"] = ids
                    st_diff_data1 = rdf_dict[ids]
                    st_diff_data1['path'] = i['path']
                    print("st_diff_data1 --> ",st_diff_data1)
                    xyz.append(st_diff_data1)
                    # list_st.append
    return xyz