import json
from collections import defaultdict

filename = "D:\ZenLabs Work Folder\Projects\ZenVault\Collection-data Workspace\collection_data_ v1\lucene\collections_rdf_v1.rdf"

asset_type = "document.asset_type.of_asset_type"
channel = "document.channel.of_channel"
area = "document.area.of_area"
collection = "document.collection.of_collection"
subject = "document.subject.of_subject"
technology = "document.technology.of_technology"

asset_type_for = "asset_type.document.for_asset"
channel_for = "channel.document.for_channel"
area_for = "area.document.for_area"
collection_for = "collection.document.for_collection"
subject_for = "subject.document.for_subject"
technology_for = "technology.document.for_technology"


def rdf_to_dict(file):
    dict1 = {}
    s = 'a'
    with open(file) as fh:
        for line in fh:
            # print(line)
            b, c, d = line.strip().split(None, 2)
            if (s != b):
                dict2 = defaultdict(list)
                empty_list_asset_type = []
                empty_list_channel = []
                empty_list_area = []
                empty_list_collection = []
                empty_list_subject = []
                empty_list_technology = []
                empty_list_asset_type_for = []
                empty_list_channel_for = []
                empty_list_area_for = []
                empty_list_collection_for = []
                empty_list_subject_for = []
                empty_list_technology_for = []

            s = b
            dict2[c] = d.strip()

            if c == asset_type and s == b:
                asset_type_1 = []
                empty_list_asset_type.append(dict2[c])
                asset_type_1 = list(set(empty_list_asset_type))
                dict2[c] = asset_type_1

            if c == channel and s == b:
                channel_1 = []
                empty_list_channel.append(dict2[c])
                channel_1 = list(set(empty_list_channel))
                dict2[c] = channel_1

            if c == area and s == b:
                area_1 = []
                empty_list_area.append(dict2[c])
                area_1 = list(set(empty_list_area))
                dict2[c] = area_1

            if c == collection and s == b:
                collection_1 = []
                empty_list_collection.append(dict2[c])
                collection_1 = list(set(empty_list_collection))
                dict2[c] = collection_1

            if c == subject and s == b:
                subject_1 = []
                empty_list_subject.append(dict2[c])
                subject_1 = list(set(empty_list_subject))
                dict2[c] = subject_1

            if c == technology and s == b:
                technology_1 = []
                empty_list_technology.append(dict2[c])
                technology_1 = list(set(empty_list_technology))
                dict2[c] = technology_1

            if c == asset_type_for and s == b:
                asset_type_for_1 = []
                empty_list_asset_type_for.append(dict2[c])
                asset_type_for_1 = list(set(empty_list_asset_type_for))
                dict2[c] = asset_type_for_1

            if c == channel_for and s == b:
                channel_for_1 = []
                empty_list_channel_for.append(dict2[c])
                channel_for_1 = list(set(empty_list_channel_for))
                dict2[c] = channel_for_1

            if c == area_for and s == b:
                area_for_1 = []
                empty_list_area_for.append(dict2[c])
                area_for_1 = list(set(empty_list_area_for))
                dict2[c] = area_for_1

            if c == collection_for and s == b:
                collection_for_1 = []
                empty_list_collection_for.append(dict2[c])
                collection_for_1 = list(set(empty_list_collection_for))
                dict2[c] = collection_for_1

            if c == subject_for and s == b:
                subject_for_1 = []
                empty_list_subject_for.append(dict2[c])
                subject_for_1 = list(set(empty_list_subject_for))
                dict2[c] = subject_for_1

            if c == technology_for and s == b:
                technology_for_1 = []
                empty_list_technology_for.append(dict2[c])
                technology_for_1 = list(set(empty_list_technology_for))
                dict2[c] = technology_for_1

            dict1[s] = dict2

    return dict1


rdf1 = rdf_to_dict(filename)

out_file = open("percipio_collection_data_final.json", "w")
json.dump(rdf1, out_file)
out_file.close()

# import json
# from collections import defaultdict

# filename = "new_rdf_4_bots_v1.rdf"

# #  = "customer.case_studies.case_study_for"
# #  = "customer.proposals.proposal_for"

# asset_type_of = "document.asset_type.of_asset_type"
# channel_of = "document.channel.of_channel"
# area_of = "document.area.of_area"
# collection_of = "document.collection.of_collection"
# subject_of = "document.subject.of_subject"
# technology_of = "document.technology.of_technology"


# def rdf_to_dict(file):
# 	dict1 = {}
# 	s = 'a'
# 	with open(file) as fh:
# 		for line in fh:
# 			b, c, d = line.strip().split(None, 2)

# 			if (s != b):
# 				dict2 = defaultdict(list)
# 				of_asset_type = []
# 				of_channel = []
# 				of_area = []
# 				of_collection = []
#                 of_subject = []
#                 of_technology = []

# 			s = b
# 			dict2[c] = d.strip()

# 			if c == cs_asset_type_of:
# 				cs_for_1 = []
# 				empty_list_cs_for.append(dict2[c])
# 				cs_for_1 = list(set(empty_list_cs_for))
# 				dict2[c] = cs_for_1

# 			if c == pro_for and s == b:
# 				pro_for_1 = []
# 				empty_list_pro_for.append(dict2[c])
# 				pro_for_1 = list(set(empty_list_pro_for))
# 				dict2[c] = pro_for_1

# 			if c == cs_from and s == b:
# 				cs_from_1 = []
# 				empty_list_cs_from.append(dict2[c])
# 				cs_from_1 = list(set(empty_list_cs_from))
# 				dict2[c] = cs_from_1

# 			if c == pro_from and s == b:
# 				pro_from_1 = []
# 				empty_list_pro_from.append(dict2[c])
# 				pro_from_1 = list(set(empty_list_pro_from))
# 				dict2[c] = pro_from_1

# 			dict1[s] = dict2

# 	return dict1

# # rdf1 = rdf_to_dict(filename)

# # out_file = open("new_test_bot4-v2.json", "w")
# # json.dump(dict1, out_file)
# # out_file.close()
