# frequency of transition for nested discrete choice model.
import syntax_function as sf
import pymysql

connection = pymysql.connect(host='localhost', port=8889, user='root', password='root', db='yu', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

table_list = ['baoji_del', 'jian', 'lantian_del']

syl_common_list = ['SFM-UFM', 'SFM-NB', 'N-S-N', 'NB-SFM-UFM', 'BNBs', 'UFM', 'AFM', 'NB-UFM', 'N-S-N-S', 'BNBl', 'S-N-S', 'N-S-N-D', 'SFM', 'NB-DFM', 'NB-SFM']

tran_common_list = ['BNBl/NB-DFM', 'NB-SFM/NB-SFM', 'NB-DFM/NB-SFM', 'NB-SFM/NB-DFM', 'NB-DFM/NB-UFM', 'NB-SFM/S-N-S', 'SFM/SFM', 'NB-SFM/SFM', 'NB-DFM/NB-DFM', 'SFM/NB-SFM', 'BNBl/NB-SFM', 'BNBl/BNBl']

emitter_list = ['1', '10', '100', '12', '4', '5', '7', '8', '9', 'L2', 'LR', 'LR2', 'N', 'R', 'a', 'c', 'd', 'f', 'g', 'h', 'k', '13', 'b', 'e', 'i', '3', 'j', '2', '11', 'LR3', 'LR4', 'L']

save_csv = ''
syl_all_list = []
for table in table_list:
		
	with connection.cursor() as cursor:
		sql_select = "SELECT * FROM " + table
		cursor.execute(sql_select)
		sql_list = cursor.fetchall()
		# print(sql_list)
		for seq in sql_list:
			if 'emitter2' in seq:
				emitter = seq['emitter2']
			else:
				emitter = seq['emitter']
			# *****************************************(print syl,seqID, emitter, population)
			syl_list = sf.seq2syl(seq['sequence'])
			# print(syl_list)
			# if len(syl_list) > 1:
			# print(syl_list)
			for syl in syl_list:
				if syl in syl_common_list:
					save_csv += syl +', '+ str(emitter) + ', '+ table +'\n'
					syl_all_list.append({'syl': syl, 'emitter': emitter, 'population': table})
		
		# with open('../new_analysis/syllable_call_animal_LT.csv', mode='w', encoding='utf-8') as save_file:
		# 	save_file.write(save_csv)		

			# *****************************************(print common_transition, emitter, population)
			# tran_list = sf.seq2tran(seq['sequence'])
			# if tran_list != None:
			# 	for tran in tran_list:
			# 		if tran in tran_common_list:
			# 			save_csv += tran + ', ' + str(emitter) +', ' + table + '\n'

with open('../new_analysis/syl_all_emitter_population.csv', mode='w', encoding='utf-8') as save_file:
	save_file.write(save_csv)



