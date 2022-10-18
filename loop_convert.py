import os
from tqdm import tqdm
path = 'sacr_data'
filenames = os.listdir(path)
for filename in tqdm(filenames):
    outfile = filename.replace('.json', '')
    outfile = outfile.replace('.sacr', '')
    os.system('python sacr2conll.py -o conll_data/{}.conll sacr_data/{}'.format(outfile, filename))