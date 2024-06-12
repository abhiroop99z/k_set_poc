from lucene.globalClass import Loader

loader = Loader()

configs = loader.load_config()


def get_exact_match_src(all_src_list, q):
    exact_match_list = []
    exact_match_string_list = []
    entities_set = set()
    for item in all_src_list:
        if item['type.is_a']:
            entities_set.add(item['type.is_a'])
    print("entities_set---")
    print(entities_set)

    for item in all_src_list:
        for entity in entities_set:
            # use of dictionary instead of app.prop
            if item['type.is_a'] == entity:
                # key1 = entity
                if item[configs[entity].data].lower() in q:
                    exact_match_list.append(item)
                    exact_match_string_list.append(item[configs[entity].data].lower())
    
    

    exact_match_string_list = get_exact_match_string_list(exact_match_string_list)

    # print("exact_match_list --> ", exact_match_list)
    # print("exact_match_string_list --> ", exact_match_string_list)
    
    return exact_match_list,exact_match_string_list


def get_partial_match_src(all_src_list, new_query, rem_query_list):
    entities_set = set()
    for item in all_src_list:
        if item['type.is_a']:
            entities_set.add(item['type.is_a'])
    partial_match_list = []
    if len(new_query) != 0:
        for item in all_src_list:
            for query in rem_query_list:

                for entity in entities_set:
                    if item['type.is_a'] == entity:
                        if query in item[configs[entity].data].lower().split():
                            partial_match_list.append(item)
    print("partial_match_list",len(partial_match_list))

    return partial_match_list

def get_exact_match_string_list(exact_match_string_list):
    exact_match_string_list = list(set(exact_match_string_list))
    x = []
    for s in exact_match_string_list:
        if ' ' in s:
            x = x + s.split()
        else:
            x.append(s)
    exact_match_string_list = list(set(x))
    return exact_match_string_list
