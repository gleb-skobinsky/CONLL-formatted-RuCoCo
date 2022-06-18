from asyncore import write
import os
import json
import collections
unprocessed_docs = []
files = os.listdir('json_data')
for filename in files:
    try:
        print(filename)
        prepacked_entities = []
        mentions = []
        with open('json_data' + '\\' + filename, encoding='utf-8') as json_file:
            data = json.load(json_file)
            for index, entity in enumerate(data['entities']):
                for mention in entity:
                    mentions.append(mention)
                    start = int(mention[0])
                    end = int(mention[1])
                    prepacked_entities.append('{M' + str(index) + ' ' + data['text'][start:end] + ' }')
        tuple_mentions = [tuple(i) for i in mentions]
        iterator = zip(tuple_mentions, prepacked_entities)
        mentions_dict = dict(iterator)
        ordered_mentions_dict = collections.OrderedDict(sorted(mentions_dict.items()))
        ordered_mentions = list(ordered_mentions_dict.values())

        mentions.sort()

        first_order_mentions = []
        second_order_mentions = []
        third_order_mentions = []
        frth_order_mentions = []
        ffth_order_mentions = []
        sixth_order_mentions = []
        seventh_order_mentions = []
        eighth_order_mentions = []
        ninth_order_mentions = []
        tenth_order_mentions = []
        for idx, mention in enumerate(mentions):
            overlaps = []
            current_mention = mentions[idx]
            for tested_range in mentions:
                if current_mention[0] >= tested_range[0] and tested_range[1] >= current_mention[1]:
                    if not (current_mention[0]==tested_range[0] and current_mention[1]==tested_range[1]):
                        overlaps.append(tested_range)
            if len(overlaps) > 0:
                if len(overlaps) == 1:
                    second_order_mentions.append(current_mention)
                elif len(overlaps) == 2:
                    third_order_mentions.append(current_mention)
                elif len(overlaps) == 3:
                    frth_order_mentions.append(current_mention)
                elif len(overlaps) == 4:
                    ffth_order_mentions.append(current_mention)
                elif len(overlaps) == 5:
                    sixth_order_mentions.append(current_mention)
            else:
                first_order_mentions.append(current_mention)

        for som in second_order_mentions:
            som_string = ordered_mentions_dict[tuple(som)]
            som_raw = data['text'][som[0]:som[1]]
            
            for fom in first_order_mentions:
                if som[0] >= fom[0] and fom[1] >= som[1]:
                    fom_string = ordered_mentions_dict[tuple(fom)]
                    
                    fom_raw = data['text'][fom[0]:fom[1]]
                    adjustment = len(fom_string) - len(fom_raw) - 2
                    if not (som[0] == fom[0] and som[1] == fom[1]):
                        starter = som[0] - fom[0] + adjustment
                        ordered_mentions_dict[tuple(fom)] = ordered_mentions_dict[tuple(fom)][0:starter] + som_string + fom_string[starter+len(som_raw):]

        for som in third_order_mentions:
            som_string = ordered_mentions_dict[tuple(som)]
            som_raw = data['text'][som[0]:som[1]]
            
            for fom in first_order_mentions:
                if som[0] >= fom[0] and fom[1] >= som[1]:
                    fom_string = ordered_mentions_dict[tuple(fom)]
                    
                    fom_raw = data['text'][fom[0]:fom[1]]
                    adjustment = len(fom_string) - len(fom_raw) - 2
                    if not (som[0] == fom[0] and som[1] == fom[1]):
                        starter = som[0] - fom[0] + adjustment
                        ordered_mentions_dict[tuple(fom)] = ordered_mentions_dict[tuple(fom)][0:starter] + som_string + fom_string[starter+len(som_raw):]

        for som in frth_order_mentions:
            som_string = ordered_mentions_dict[tuple(som)]
            som_raw = data['text'][som[0]:som[1]]
            
            for fom in first_order_mentions:
                if som[0] >= fom[0] and fom[1] >= som[1]:
                    fom_string = ordered_mentions_dict[tuple(fom)]
                    
                    fom_raw = data['text'][fom[0]:fom[1]]
                    adjustment = len(fom_string) - len(fom_raw) - 2
                    if not (som[0] == fom[0] and som[1] == fom[1]):
                        starter = som[0] - fom[0] + adjustment
                        ordered_mentions_dict[tuple(fom)] = ordered_mentions_dict[tuple(fom)][0:starter] + som_string + fom_string[starter+len(som_raw):]
        
        for som in ffth_order_mentions:
            som_string = ordered_mentions_dict[tuple(som)]
            som_raw = data['text'][som[0]:som[1]]
            
            for fom in first_order_mentions:
                if som[0] >= fom[0] and fom[1] >= som[1]:
                    fom_string = ordered_mentions_dict[tuple(fom)]
                    
                    fom_raw = data['text'][fom[0]:fom[1]]
                    adjustment = len(fom_string) - len(fom_raw) - 2
                    if not (som[0] == fom[0] and som[1] == fom[1]):
                        starter = som[0] - fom[0] + adjustment
                        ordered_mentions_dict[tuple(fom)] = ordered_mentions_dict[tuple(fom)][0:starter] + som_string + fom_string[starter+len(som_raw):]
        result = ''
        prev = 0
        for fom in first_order_mentions:
            result += data['text'][prev:fom[0]]
            prev = fom[1]
            result += ordered_mentions_dict[tuple(fom)]
        result += data['text'][prev:]
        with open('sacr_data' + '\\' + filename + '.sacr', 'w', encoding='utf-8') as output:
            output.write(result)
            output.close()
    except:
        unprocessed_docs.append(filename)
        continue
print('Conversion completed.')
print('These docs could not be converted due to errors:{}'.format(', '.join(unprocessed_docs)))

