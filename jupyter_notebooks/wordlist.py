import re
import pandas as pd
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199

full_list = []
with open('Resources/Frequency_index.txt', 'r', encoding='utf8') as infile:
    for line in infile:
        components = re.split(r'\t+', line.rstrip('\t').rstrip('\n'))
        if len(components) == 1:
            continue
        word, POS, ENG, freq = components[1],components[2],components[3],components[-1]
        sent = ' '.join(map(lambda x: x, components[4:-1]))
        dict = {'freq':freq, 'word':word, 'POS':POS, 'ENG':ENG, 'sent':sent}
        full_list.append(dict)

full_df = pd.DataFrame.from_dict(full_list).sort_values(by=['freq'],ascending=False).drop_duplicates(subset=['word','freq','ENG'])

def print_by_POS(pos, df=full_df, sort='freq'):
    pos_df = conj = full_df[full_df['POS'].str.contains(pos)]
    if sort == 'freq':
        return pos_df[['word','ENG','sent']].reset_index(drop=True).style.set_properties(**{'text-align': 'left'})
    if sort == 'alpha':
        return pos_df[['word','ENG','sent']].reset_index(drop=True).sort_values(by=['word']).style.set_properties(**{'text-align': 'left'})