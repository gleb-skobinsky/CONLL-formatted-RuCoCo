import os
path = 'sacr_data'
filenames = os.listdir(path)
for filename in filenames:
    print(filename)
    outfile = filename.replace('.json', '')
    outfile = outfile.replace('.sacr', '')
    os.system('python sacr2conll.py -o conll_data/{}.conll sacr_data/{}'.format(outfile, filename))