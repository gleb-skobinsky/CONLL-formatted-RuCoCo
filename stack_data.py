import os
import random
separate_files = os.listdir('conll_data')

all_conlls = len(separate_files)
train_split = (all_conlls // 10) * 8
dev_split = (all_conlls - train_split) // 2
test_split = all_conlls - train_split - dev_split

print(train_split)
print(dev_split)
print(test_split)

random.shuffle(separate_files)
train_data = separate_files[0:train_split]
dev_data = separate_files[train_split:train_split+dev_split]
test_data = separate_files[train_split+dev_split:train_split+dev_split+test_split]

print(train_data)
print(dev_data)
print(test_data)

for train_file in train_data:
    with open('conll_data' + '\\' + train_file, encoding='utf-8') as reader:
        train_rows = reader.read()
        reader.close()

    with open('train.conll', 'a', encoding='utf-8') as writer:
        writer.write(train_rows)
        writer.close()

for train_file in dev_data:
    with open('conll_data' + '\\' + train_file, encoding='utf-8') as reader:
        train_rows = reader.read()
        reader.close()

    with open('dev.conll', 'a', encoding='utf-8') as writer:
        writer.write(train_rows)
        writer.close()

for train_file in test_data:
    with open('conll_data' + '\\' + train_file, encoding='utf-8') as reader:
        train_rows = reader.read()
        reader.close()

    with open('test.conll', 'a', encoding='utf-8') as writer:
        writer.write(train_rows)
        writer.close()

# for conll_file in separate_files:
#     with open('conll_data' + '\\' + conll_file, 'r', encoding='utf-8') as input_file:
#         conll_doc = input_file.read()
#         input_file.close()
#     conll_doc += '\n'
#     with open('total.conll', 'a', encoding='utf-8') as output_file:
#         output_file.write(conll_doc)
#         output_file.close()
