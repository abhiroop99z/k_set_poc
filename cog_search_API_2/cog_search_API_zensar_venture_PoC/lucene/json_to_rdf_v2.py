import pandas as pd 
import json
import re

df_data = pd.read_excel('lucene\collectionsReport_Percipio.xlsx',sheet_name='collectionsReport (23)')
# df_data.head(5)

df_data = df_data.fillna('No data')


# index number 8083 and 8823
# for j,i in enumerate(df_data['CONTENT UUID']):
# #     print(type(i))
#     if (i == "e266146d-c004-4b24-aeaa-37b4a5ea2059") or (i == "7a03fdda-e320-4f72-85b7-4363777b2887"):
#         print(j)
#         print(df_data.AREA[j])
#         a = df_data['CONTENT UUID'][j]
#         df_data['AREA'].mask(df_data['AREA'] == '生产力和协作工具', "No Data", inplace=True)

df_data= pd.DataFrame(df_data)
json_data = df_data.to_json(orient = 'records')

data = json.loads(json_data)
print(type(data))

document_dic = {}
asset_type_dic ={}
channel_dic ={}
area_dic ={}
collection_dic ={}
subject_dic ={}
technology_dic ={}


for i,item in enumerate(data):
    key_1 = ('bot.1{}').format(i)
    if item['CONTENT TITLE'] not in document_dic.keys():
        document_dic[item['CONTENT TITLE']] = key_1

    key_2 = ('bot.2{}').format(i)
    if item['ASSET TYPE'] not in asset_type_dic.keys():
        asset_type_dic[item['ASSET TYPE']] = key_2

    key_3 = ('bot.3{}').format(i)
    if item['CHANNEL'] not in channel_dic.keys():
        channel_dic[item['CHANNEL']] = key_3

    key_4 = ('bot.4{}').format(i)
    if item['AREA'] not in area_dic.keys():
        area_dic[item['AREA']] = key_4

    key_5 = ('bot.5{}').format(i)
    if item['COLLECTION'] not in collection_dic.keys():
        collection_dic[item['COLLECTION']] = key_5

    key_6 = ('bot.6{}').format(i)
    if item['SUBJECT'] not in subject_dic.keys():
        subject_dic[item['SUBJECT']] = key_6

    key_7 = ('bot.7{}').format(i)
    if item['TECHNOLOGY TITLE'] not in technology_dic.keys():
        technology_dic[item['TECHNOLOGY TITLE']] = key_7



document_asset_dict = {}
document_channel_dict = {}
document_collection_dict = {}
document_area_dict = {}
document_subject_dict = {}
document_technology_dict = {}


for document in document_dic.keys():
    document_asset_lst = []
    document_channel_lst = []
    document_collection_lst = []
    document_area_lst = []
    document_subject_lst = []
    document_technology_lst = []


    for item in data:
        if item['CONTENT TITLE'] == document:
            document_asset_lst.append(item['ASSET TYPE'])
            document_channel_lst.append(item['CHANNEL'])
            document_area_lst.append(item['AREA'])
            document_collection_lst.append(item['COLLECTION'])
            document_subject_lst.append(item['SUBJECT'])
            document_technology_lst.append(item['TECHNOLOGY TITLE'])

    document_asset_dict[document] = list(set(document_asset_lst))
    document_channel_dict[document] = list(set(document_channel_lst))
    document_area_dict[document] = list(set(document_area_lst))
    document_collection_dict[document] = list(set(document_collection_lst))
    document_subject_dict[document] = list(set(document_subject_lst))
    document_technology_dict[document] = list(set(document_technology_lst))

asset_document_dict = {}
for asset in asset_type_dic.keys():
    asset_document_lst = []
    for item in data:
        if item['ASSET TYPE'] == asset:
            asset_document_lst.append(item['CONTENT TITLE'])
    asset_document_dict[asset] = list(set(asset_document_lst))

channel_document_dict = {}
for channel in channel_dic.keys():
    channel_document_lst = []
    for item in data:
        if item['CHANNEL'] == channel:
            channel_document_lst.append(item['CONTENT TITLE'])
    channel_document_dict[channel] = list(set(channel_document_lst))

area_document_dict = {}
for area in area_dic.keys():
    area_document_lst = []
    for item in data:
        if item['AREA'] == area:
            area_document_lst.append(item['CONTENT TITLE'])
    area_document_dict[area] = list(set(area_document_lst))

collection_document_dict = {}
for collection in collection_dic.keys():
    collection_document_lst = []
    for item in data:
        if item['COLLECTION'] == collection:
            collection_document_lst.append(item['CONTENT TITLE'])
    collection_document_dict[collection] = list(set(collection_document_lst))

subject_document_dict = {}
for subject in subject_dic.keys():
    subject_document_lst = []
    for item in data:
        if item['SUBJECT'] == subject:
            subject_document_lst.append(item['CONTENT TITLE'])
    subject_document_dict[subject] = list(set(subject_document_lst))

technology_document_dict = {}
for technology in technology_dic.keys():
    technology_document_lst = []
    for item in data:
        if item['TECHNOLOGY TITLE'] == technology:
            technology_document_lst.append(item['CONTENT TITLE'])
    technology_document_dict[technology] = list(set(technology_document_lst))

with open('lucene\collections_rdf_v22222.rdf','w') as f:
    for i,item in enumerate(data):
    #         print(i)
        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "type.is_a" + "\t" + "entity.document" + "\n")
        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.literal.content_title" + "\t" + item['CONTENT TITLE'].encode('utf-8').decode('ascii','ignore') + "\n")
        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.literal.content_uuid" + "\t" + item['CONTENT UUID'].encode('utf-8').decode('ascii','ignore') + "\n")

        regex_remove_new_line = re.compile(r'[\r?\n]')
        desc = item['DESCRIPTION'].encode('utf-8').decode('ascii','ignore')

        regex_replace_with = ""

        description = re.sub(regex_remove_new_line,regex_replace_with,desc)

        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.literal.content_description" + "\t" + description + "\n")


        for i in document_asset_dict[item['CONTENT TITLE']]:
            f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.asset_type.of_asset_type" + "\t" + asset_type_dic[i] + "\n")

        for i in document_channel_dict[item['CONTENT TITLE']]:
            f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.channel.of_channel" + "\t" + channel_dic[i] + "\n")

        for i in document_area_dict[item['CONTENT TITLE']]:
            f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.area.of_area" + "\t" + area_dic[i] + "\n")

        for i in document_collection_dict[item['CONTENT TITLE']]:
            f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.collection.of_collection" + "\t" + collection_dic[i] + "\n")

        for i in document_subject_dict[item['CONTENT TITLE']]:
            f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.subject.of_subject" + "\t" + subject_dic[i] + "\n")

        for i in document_technology_dict[item['CONTENT TITLE']]:
            f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.technology.of_technology" + "\t" + technology_dic[i] + "\n")

    for item in data:
        f.write(asset_type_dic[item['ASSET TYPE']] + "\t" + "type.is_a" + "\t" + "entity.asset_type" + "\n")
        f.write(asset_type_dic[item['ASSET TYPE']] + "\t" + "asset_type.literal.asset_name" + "\t" + item['ASSET TYPE'].encode('utf-8').decode('ascii','ignore') + "\n")
        # f.write(asset_type_dic[item['ASSET TYPE']] + "\t" + "asset_type.document.for_asset" + "\t" + document_dic[item['CONTENT TITLE']].encode('utf-8').decode('ascii','ignore') + "\n")
        for i in document_asset_dict[item['CONTENT TITLE']]:
            if item['ASSET TYPE'] in i:
                f.write(asset_type_dic[item['ASSET TYPE']] + "\t" + "asset_type.document.for_asset" + "\t" + asset_type_dic[i] + "\n")


    for item in data:
        f.write(channel_dic[item['CHANNEL']] + "\t" + "type.is_a" + "\t" + "entity.channel" + "\n")
        f.write(channel_dic[item['CHANNEL']] + "\t" + "channel.literal.channel_name" + "\t" + item['CHANNEL'].encode('utf-8').decode('ascii','ignore') + "\n")
        # f.write(channel_dic[item['CHANNEL']] + "\t" + "channel.document.for_channel" + "\t" + document_dic[item['CONTENT TITLE']].encode('utf-8').decode('ascii','ignore') + "\n")
        for i in channel_document_dict[item['CHANNEL']]:
            f.write(channel_dic[item['CHANNEL']] + "\t" + "channel.document.for_channel" + "\t" + document_dic[item['CONTENT TITLE']] + "\n")

    for item in data:
        f.write(area_dic[item['AREA']] + "\t" + "type.is_a" + "\t" + "entity.area" + "\n")
        f.write(area_dic[item['AREA']] + "\t" + "area.literal.area_name" + "\t" + item['AREA'].encode('utf-8').decode('ascii','ignore') + "\n")
        # f.write(area_dic[item['AREA']] + "\t" + "area.document.for_area" + "\t" + document_dic[item['CONTENT TITLE']].encode('utf-8').decode('ascii','ignore') + "\n")
        for i in area_document_dict[item['AREA']]:
            f.write(area_dic[item['AREA']] + "\t" + "area.document.for_area" + "\t" + document_dic[item['CONTENT TITLE']] + "\n")

    for item in data:
        f.write(collection_dic[item['COLLECTION']] + "\t" + "type.is_a" + "\t" + "entity.collection" + "\n")
        f.write(collection_dic[item['COLLECTION']] + "\t" + "collection.literal.collection_name" + "\t" + item['COLLECTION'].encode('utf-8').decode('ascii','ignore') + "\n")
        # f.write(collection_dic[item['COLLECTION']] + "\t" + "collection.document.for_collection" + "\t" + document_dic[item['CONTENT TITLE']].encode('utf-8').decode('ascii','ignore') + "\n")
        for i in collection_document_dict[item['COLLECTION']]:
            f.write(collection_dic[item['COLLECTION']] + "\t" + "collection.document.for_collection" + "\t" + document_dic[item['CONTENT TITLE']] + "\n")

    for item in data:
        f.write(subject_dic[item['SUBJECT']] + "\t" + "type.is_a" + "\t" + "entity.subject" + "\n")
        f.write(subject_dic[item['SUBJECT']] + "\t" + "subject.literal.subject_name" + "\t" + item['SUBJECT'].encode('utf-8').decode('ascii','ignore') + "\n")
        # f.write(subject_dic[item['SUBJECT']] + "\t" + "subject.document.for_subject" + "\t" + document_dic[item['CONTENT TITLE']].encode('utf-8').decode('ascii','ignore') + "\n")
        for i in subject_document_dict[item['SUBJECT']]:
            f.write(subject_dic[item['SUBJECT']] + "\t" + "subject.document.for_subject" + "\t" + document_dic[item['CONTENT TITLE']] + "\n")

    for item in data:
        f.write(technology_dic[item['TECHNOLOGY TITLE']] + "\t" + "type.is_a" + "\t" + "entity.technology" + "\n")
        f.write(technology_dic[item['TECHNOLOGY TITLE']] + "\t" + "technology.literal.technology_title" + "\t" + item['TECHNOLOGY TITLE'].encode('utf-8').decode('ascii','ignore') + "\n")
        # f.write(technology_dic[item['TECHNOLOGY TITLE']] + "\t" + "technology.document.for_technology" + "\t" + document_dic[item['CONTENT TITLE']].encode('utf-8').decode('ascii','ignore') + "\n")
        for i in technology_document_dict[item['TECHNOLOGY TITLE']]:
            f.write(technology_dic[item['TECHNOLOGY TITLE']] + "\t" + "technology.document.for_technology" + "\t" + document_dic[item['CONTENT TITLE']] + "\n")