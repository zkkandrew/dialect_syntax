# from collections import Counter

# from collections import defaultdict 
# rows_by_date = defaultdict(list) 
# for row in saep_dict:
#     rows_by_date[row['emitter']].append(row)
# print(rows_by_date)

# from operator import itemgetter
# from itertools import groupby
# # 一个非常重要的准备步骤是要根据指定的字段将数据排序。
# # 因为 groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。
# saep_dict.sort(key = itemgetter('syl'))
# for syl, items in groupby(saep_dict, key = itemgetter('syl')):
# 	print(syl)
# 	syl_dict = []
# 	for i in items:
# 		# print(' ', i)
# 		# print(i['syl'])
# 		syl_dict.append({i['syl'], i['emitter'], i['population']})
# 	print(syl_dict)
# 	# print(Counter(syl_dict))

import pandas as pd
df = pd.read_csv('../new_analysis/syl_all_emitter_population.csv', header=0, names=['syl', 'emitter','population'])
# print(df.head())
df_grouped = df.groupby(['syl', 'emitter'])['population'].count().reset_index(name='count')
# print(df_grouped['syl'].count())
# get types in one column
emitter_list = list(df_grouped['emitter'].unique())
emitter_list = [(x).strip() for x in emitter_list]
# print(emitter_list)
# df_g_count = df_grouped
# print(df_g_count)
# for (syl, emitter), group in df_grouped:
# 	print(syl, emitter, group)

syl_common_list = ['SFM-UFM', 'SFM-NB', 'N-S-N', 'NB-SFM-UFM', 'BNBs', 'UFM', 'AFM', 'NB-UFM', 'N-S-N-S', 'BNBl', 'S-N-S', 'N-S-N-D', 'SFM', 'NB-DFM', 'NB-SFM']

df_new = pd.DataFrame(columns=syl_common_list)
df_new['emitter'] = emitter_list

# print(df_new.loc[df_new['emitter']=='a', 'N-S-N'])
# # print(df_new)
# # # # print(df_new.columns)
for syl in syl_common_list:
	# print(syl)
	for emitter in emitter_list:
		# print(emitter)
		for row in df_grouped.iterrows():
			# print(row[1]['syl'], syl, row[1]['emitter'], emitter)
			if row[1]['syl'] == syl and (row[1]['emitter']).strip() == emitter:
				# df_new.loc[syl,emitter] = 
				df_new.loc[df_new['emitter']==emitter, syl] = row[1]['count']
				# print(syl, emitter, row[1]['count'])

df_new.to_csv('../new_analysis/syl_all_emitter_population_new.csv')
print(df_new)
	

