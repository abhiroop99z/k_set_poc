from collections import defaultdict
import json
import requests

from lucene.globalClass import Loader

loader = Loader()

configs = loader.load_config()
fields_list = loader.load_fields()


def call_lucene(query):

    data = json.dumps({"query": query})
    headers = {'Content-type': 'application/json'}
    res = requests.post(configs.get("LUCENE_URL").data, data=data, headers=headers)
    res = res.json()

    return res


def remove_duplicates(data_list):
    # data_list = [dict(t) for t in {tuple(d.items()) for d in data_list}]
    return data_list


def remove_duplicate_papers(paper_res):
  unique_papers_set = set()
  unique_papers_list = []
  for paper in paper_res:
      if paper['bot_rdf_id'] not in unique_papers_set:
          unique_papers_set.add(paper['bot_rdf_id'])  # note it down for further iterations
          unique_papers_list.append(paper)
  # print(len(paper_res))
  # print(len(unique_papers_list))
  return unique_papers_list


def get_sources_from_lucene(query):
    data = json.dumps({"query": query})
    headers = {'Content-type': 'application/json'}
    # if 'filters' not in data1.keys():
    global lucene_sources
    global final_result_paper_res
    lucene_sources = requests.post('http://172.16.10.19:3035/lucene/luceneSearch', data=data, headers=headers)
    lucene_sources = lucene_sources.json()
    all_sources = lucene_sources
    return all_sources


def remove_exact_match_from_query(q, exact_match_string_list):
    print("initial query ---> ", q)
    if len(exact_match_string_list) != 0:
        for item in exact_match_string_list:
            q = q.replace(item,"")

    print("query after replacing exact source----> ",q)

    return q

def ranking(q_list, papers,exact_match_query,rem_query):
    final_papers = []
    for item in papers:
        c = 0
        for word in q_list:
            for field in fields_list:
                if word in item[field].lower():
                    c = c + 1
        item['score'] = c

    scores_dict = defaultdict(list)
    for i,item in enumerate(papers):   
        scores_dict[item['score']].append(item)

    
    for key,val in scores_dict.items():
        # papers = ranking_on_content_title(q_list,val,exact_match_query,rem_query)
        final_papers = final_papers + papers
        final_papers = sorted(final_papers, key=lambda i: i['score'],reverse=True )

    return final_papers

def ranking_backup(q_list, papers,eaxct_match_query,rem_query):
    # new_ppr = pprs
    final_papers = []
    for item in papers:
        c = 0
        for word in q_list:
            # print(word)
            if word in item['content_title'].lower():
                c = c + 1
                # print(item['name'])
            elif word in item['of_asset_type'].lower():
                c = c + 1
                # print(item['asset'])
            elif word in item['of_channel'].lower():
                c = c + 1
                # print(item['channel'])
            elif word in item['of_area'].lower():
                c = c + 1
                # print(item['area'])
            elif word in item['of_collection'].lower():
                c = c + 1
                # print(item['collection'])
            elif word in item['of_subject'].lower():
                c = c + 1
                # print(item['subject'])
            elif word in item['of_technology'].lower():
                c = c + 1
                # print(item['technology'].lower())
            # else:
            #     c = c
        item['score'] = c


    scores_dict = defaultdict(list)
    for i,item in enumerate(papers):   
        scores_dict[item['score']].append(item)

    
    for key,val in scores_dict.items():
        # papers = ranking_on_content_title(q_list,val,eaxct_match_query,rem_query)
        final_papers = final_papers + papers

    final_papers = sorted(final_papers, key=lambda i: i['score'],reverse=True )
    return final_papers

# backup function
def ranking_old(q_list, papers,eaxct_match_query,rem_query):
    final_papers = []
    for item in papers:
        c = 0
        for word in q_list:
            if word in item['name'].lower():
                c = c + 1

            elif word in item['asset'].lower():
                c = c + 1

            elif word in item['channel'].lower():
                c = c + 1

            elif word in item['area'].lower():
                c = c + 1

            elif word in item['collection'].lower():
                c = c + 1

            elif word in item['subject'].lower():
                c = c + 1

            elif word in item['technology'].lower():
                c = c + 1

        item['score'] = c

    
    scores_dict = defaultdict(list)
    for i,item in enumerate(papers):   
        scores_dict[item['score']].append(item)

      
    # list_c = [list_b[item['score']].append(item) for i,item in enumerate(papers)]
    

    # with open('paper_res.json', 'w+') as out_file:
    #     json.dump(list_b, out_file)

    for key,val in scores_dict.items():
        # papers = ranking_on_content_title(q_list,val,eaxct_match_query,rem_query)
        final_papers = final_papers + papers

    final_papers = sorted(final_papers, key=lambda i: i['score'],reverse=True )
    return final_papers

def ranking_on_content_title(q_list, papers,exact_match_query,rem_query):    
    for item in papers:
        c = item['score']
        for word in q_list:
            # if word == item['content_title'].lower() and word == exact_match_query:
            #     c = c + 0.85
            # elif word in item['content_title'].lower() and word in exact_match_query:
            #     c = c + 0.75
            
            if word == item['company_name'].lower():
                c = c + 0.85
            elif word in item['company_name'].lower():
                c = c + 0.50
                
        item['score'] = c
    papers = sorted(papers, key=lambda i: i['score'],reverse=True )
    return papers

# previously used in ranking function and in views file
def sort_by_score(pprs_with_rank):
    # pprs = sorted(pprs_with_rank, key=operator.itemgetter('score'),reverse=True)
    pprs = sorted(pprs_with_rank, key=lambda i: i['score'],reverse=True )

    for item in pprs:
        pass
    return pprs

def removeStopWords(query):
    return query