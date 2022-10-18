from asyncore import write
import os
import json
import collections
from tqdm import tqdm
unprocessed_docs = []
files = os.listdir('json_data')
filename = files[20]
for filename in tqdm(files):
    try:
        with open('json_data' + '\\' + filename, encoding='utf-8') as json_file:
                data = json.load(json_file)
                json_file.close()
        entities = data["entities"]
        text = data["text"]
        mentions = []
        entity_count = 0
        entity_dict = {}
        for entity in entities:
            entity_count += 1
            for mention in entity:
                mentions.append(mention)
                entity_dict[tuple(mention)] = entity_count
        gone_through_left = []
        gone_through_right = []
        for w in sorted(mentions, key=lambda x:-x[0]):
            # if there were right-hand brackets inserted whose offset is less than the current left bracket, we add 2 as per such bracket
            alignment = sum(w[0] >= i for i in gone_through_right) * 2
            # if there were left-hand brackets inserted whose offset is less than the current left bracket, we add 6 as per such bracket (3 for '{M ', and 3 for entity id)
            alignment += sum(w[0] >= i for i in gone_through_left) * 6
            # accordingly for current right bracket...
            alignment = sum(w[1] >= i for i in gone_through_right) * 2
            alignment += sum(w[1] >= i for i in gone_through_left) * 6            
            entity_num = '{M' + str(entity_dict[tuple(w)]).zfill(3) + ' '
            text = text[:w[0]] + entity_num + text[w[0]:alignment+w[1]] + ' }' + text[alignment+w[1]:]
            gone_through_left.append(w[0])
            gone_through_right.append(w[1])
        output_filename = filename.replace('.json', '.sacr')
        with open('sacr_data' + '\\' + output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(text)
            output_file.close()
    except:
        print("Parsing error.")
        unprocessed_docs.append(filename)
        continue
print('Conversion completed.')
print('These docs could not be converted due to errors:{}'.format(', '.join(unprocessed_docs)))

