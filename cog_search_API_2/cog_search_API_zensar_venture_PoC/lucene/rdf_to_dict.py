import json
from collections import defaultdict

filename = "new_rdf_4_bots_v1.rdf"

asset_type = "document.asset_type.of_asset_type"
channel =	"document.channel.of_channel"
area = "document.area.of_area"
collection = "document.collection.of_collection"
subject = "document.subject.of_subject"
technology = "document.technology.of_technology"

def rdf_to_dict(file):
	dict1 = {}
	s = 'a'
	with open(file) as fh:
		for line in fh:
			b, c, d = line.strip().split(None, 2)

			if (s != b):
				dict2 = defaultdict(list)
				empty_list_asset_type = []
				empty_list_channel = []
				empty_list_area = []
				empty_list_collection = []
				empty_list_subject = []
				empty_list_technology = []

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

			dict1[s] = dict2

	return dict1

# rdf1 = rdf_to_dict(filename)

# out_file = open("new_test_bot4-v2.json", "w")
# json.dump(dict1, out_file)
# out_file.close()
