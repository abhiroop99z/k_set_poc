import pandas as pd
import json

df = pd.read_excel('collectionsReport_Percipio.xlsx',sheet_name='collectionsReport (23)')
# df = df.fillna('No data', inplace=True)
df = pd.DataFrame(df)
js = df.to_json(orient = 'records')

data = json.loads(js)
print(len(data))

for i,item in enumerate(data):
    if i == 1232:
        print(item['DESCRIPTION'])
        break

# document_dic = {}
# asset_type_dic ={}
# channel_dic ={}
# area_dic ={}
# collection_dic ={}
# subject_dic ={}
# technology_dic ={}
#
#
# for i,item in enumerate(data):
#     key_1 = ('bot.1{}').format(i)
#     if item['CONTENT TITLE'] not in document_dic.keys():
#         document_dic[item['CONTENT TITLE']] = key_1
#
#     key_2 = ('bot.2{}').format(i)
#     if item['ASSET TYPE'] not in asset_type_dic.keys():
#         asset_type_dic[item['ASSET TYPE']] = key_2
#
#     key_3 = ('bot.3{}').format(i)
#     if item['CHANNEL'] not in channel_dic.keys():
#         channel_dic[item['CHANNEL']] = key_3
#
#     key_4 = ('bot.4{}').format(i)
#     if item['AREA'] not in area_dic.keys():
#         area_dic[item['AREA']] = key_4
#
#     key_5 = ('bot.5{}').format(i)
#     if item['COLLECTION'] not in collection_dic.keys():
#         collection_dic[item['COLLECTION']] = key_5
#
#     key_6 = ('bot.6{}').format(i)
#     if item['SUBJECT'] not in subject_dic.keys():
#         subject_dic[item['SUBJECT']] = key_6
#
#     key_7 = ('bot.7{}').format(i)
#     if item['TECHNOLOGY TITLE'] not in technology_dic.keys():
#         technology_dic[item['TECHNOLOGY TITLE']] = key_7
description_dict = {}

for i,item in enumerate(data):

    description_dict[item['DESCRIPTION']] = ('desc.1{id}').format(id = i)


i = 0
document_dic = {}
for item in data:
    key = ('bot.1{id}').format(id = i)
    if item['CONTENT TITLE'] not in document_dic.keys():
        document_dic[item['CONTENT TITLE']] = key
        i = i + 1


# print(document_dic)

i = 0
asset_type_dic = {}
for item in data:
    key = ('bot.2{id}').format(id = i)
    if item['ASSET TYPE'] not in asset_type_dic.keys():
        asset_type_dic[item['ASSET TYPE']] = key
        i = i + 1

i = 0
channel_dic = {}
for item in data:
    key = ('bot.3{id}').format(id = i)
    if item['CHANNEL'] not in channel_dic.keys():
        channel_dic[item['CHANNEL']] = key
        i = i + 1

i = 0
area_dic = {}
for item in data:
    key = ('bot.4{id}').format(id = i)
    if item['AREA'] not in area_dic.keys():
        area_dic[item['AREA']] = key
        i = i + 1

i = 0
collection_dic = {}
for item in data:
    key = ('bot.5{id}').format(id = i)
    if item['COLLECTION'] not in collection_dic.keys():
        collection_dic[item['COLLECTION']] = key
        i = i + 1

i = 0
subject_dic = {}
for item in data:
    key = ('bot.6{id}').format(id = i)
    if item['SUBJECT'] not in subject_dic.keys():
        subject_dic[item['SUBJECT']] = key
        i = i + 1

i = 0
technology_dic = {}
for item in data:
    key = ('bot.7{id}').format(id = i)
    if item['TECHNOLOGY TITLE'] not in technology_dic.keys():
        technology_dic[item['TECHNOLOGY TITLE']] = key
        i = i + 1

document_asset_dict = {}
for document in document_dic.keys():
    document_asset_lst = []
    for item in data:
        if item['CONTENT TITLE'] == document:
            document_asset_lst.append(item['ASSET TYPE'])
    document_asset_dict[document] = list(set(document_asset_lst))

asset_document_dict = {}
for asset in asset_type_dic.keys():
    asset_document_lst = []
    for item in data:
        if item['ASSET TYPE'] == asset:
            asset_document_lst.append(item['CONTENT TITLE'])
    asset_document_dict[asset] = list(set(asset_document_lst))

#     break
# print("document_asset_dict",document_asset_dict)

document_channel_dict = {}
for document in document_dic.keys():
    document_channel_lst = []
    for item in data:
        if item['CONTENT TITLE'] == document:
            document_channel_lst.append(item['CHANNEL'])
    document_channel_dict[document] = list(set(document_channel_lst))
#     break
# print("document_channel_dict",document_channel_dict)

document_area_dict = {}
for document in document_dic.keys():
    document_area_lst = []
    for item in data:
        if item['CONTENT TITLE'] == document:
            document_area_lst.append(item['AREA'])
    document_area_dict[document] = list(set(document_area_lst))
#     break
# print("document_area_dict",document_area_dict)

document_collection_dict = {}
for document in document_dic.keys():
    document_collection_lst = []
    for item in data:
        if item['CONTENT TITLE'] == document:
            document_collection_lst.append(item['COLLECTION'])
    document_collection_dict[document] = list(set(document_collection_lst))
#     break
# print("document_collection_dict",document_collection_dict)

document_subject_dict = {}
for document in document_dic.keys():
    document_subject_lst = []
    for item in data:
        if item['CONTENT TITLE'] == document:
            document_subject_lst.append(item['SUBJECT'])
    document_subject_dict[document] = list(set(document_subject_lst))
#     break
# print("document_subject_dict",document_subject_dict)

document_technology_dict = {}
for document in document_dic.keys():
    document_technology_lst = []
    for item in data:
        if item['CONTENT TITLE'] == document:
            document_technology_lst.append(item['TECHNOLOGY TITLE'])
    document_technology_dict[document] = list(set(document_technology_lst))
#     break
# print("document_technology_dict",document_technology_dict)

with open('collections_rdf_v2.rdf','w') as f:
    for item in data:
        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "type.is_a" + "\t" + "entity.document" + "\n")
        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.literal.content_title" + "\t" + item['CONTENT TITLE'] + "\n")
        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.literal.content_uuid" + "\t" + item['CONTENT UUID'].encode('utf-8').decode('ascii','ignore') + "\n")
        f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.literal.content_description" + "\t" + item['DESCRIPTION'][:200].encode('utf-8').decode('ascii','ignore') + "\n")

        # f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.literal.content_description" + "\t" +description_dict[item['DESCRIPTION']] + "\n")
        # for i in description_dict[item['CONTENT TITLE']]:
        #     f.write(document_dic[item['CONTENT TITLE']] + "\t" + "document.asset_type.of_asset_type" + "\t" + asset_type_dic[i] + "\n")

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
        f.write(asset_type_dic[item['ASSET TYPE']] + "\t" + "document.literal.content_title" + "\t" + item['ASSET TYPE'] + "\n")
        # f.write(asset_type_dic[item['ASSET TYPE']] + "\t" + "asset_type.document.for_asset" + "\t" + document_dic['CONTENT TITLE'] + "\n")
        for i in asset_document_dict[item['ASSET TYPE']]:
            f.write(asset_type_dic[item['ASSET TYPE']] + "\t" + "asset_type.document.for_asset" + "\t" + document_dic[item['CONTENT TITLE']] + "\n")

    for item in data:
        f.write(channel_dic[item['CHANNEL']] + "\t" + "type.is_a" + "\t" + "entity.channel" + "\n")
        f.write(channel_dic[item['CHANNEL']] + "\t" + "channel.literal.channel_name" + "\t" + item['CHANNEL'] + "\n")
        f.write(channel_dic[item['CHANNEL']] + "\t" + "channel.document.for_channel" + "\t" + document_dic['CONTENT TITLE'] + "\n")

    for item in data:
        f.write(area_dic[item['AREA']] + "\t" + "type.is_a" + "\t" + "entity.area" + "\n")
        f.write(area_dic[item['AREA']] + "\t" + "area.literal.area_name" + "\t" + item['AREA'] + "\n")
        f.write(area_dic[item['AREA']] + "\t" + "area.document.for_area" + "\t" + document_dic['CONTENT TITLE'] + "\n")

    for item in data:
        f.write(collection_dic[item['COLLECTION']] + "\t" + "type.is_a" + "\t" + "entity.collection" + "\n")
        f.write(collection_dic[item['COLLECTION']] + "\t" + "collection.literal.collection_name" + "\t" + item['COLLECTION'] + "\n")
        f.write(collection_dic[item['COLLECTION']] + "\t" + "collection.document.for_collection" + "\t" + document_dic['CONTENT TITLE'] + "\n")

    for item in data:
        f.write(subject_dic[item['SUBJECT']] + "\t" + "type.is_a" + "\t" + "entity.subject" + "\n")
        f.write(subject_dic[item['SUBJECT']] + "\t" + "subject.literal.subject_name" + "\t" + item['SUBJECT'] + "\n")
        f.write(subject_dic[item['SUBJECT']] + "\t" + "subject.document.for_subject" + "\t" + document_dic['CONTENT TITLE'] + "\n")

    for item in data:
        f.write(technology_dic[item['TECHNOLOGY TITLE']] + "\t" + "type.is_a" + "\t" + "entity.technology" + "\n")
        f.write(technology_dic[item['TECHNOLOGY TITLE']] + "\t" + "technology.literal.technology_title" + "\t" + item['TECHNOLOGY TITLE'] + "\n")
        f.write(technology_dic[item['TECHNOLOGY TITLE']] + "\t" + "technology.document.for_technology" + "\t" + document_dic['CONTENT TITLE'] + "\n")