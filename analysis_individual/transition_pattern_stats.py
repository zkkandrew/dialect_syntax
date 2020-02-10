from scipy import stats
import indi_seq_function as isf
import constant

import sys
sys.path.append("..")
import syntax_function as sf


# within populations
all_syl_num_dict_list = []
all_tran_num_dict_list = []
all_po_num_dict_list = []
all_seq_num_dict_list = []
for pop in constant.threeQuartersIndividuals:
	# if pop['population'] == 'baoji_del':
	# print(pop['population'])
	all_seq_list = []
	for bat in pop['seqPerBat']:
		# print(bat['batID'], bat['numOfSeq'])
		seq_result = isf.get_seq_by_indi_num(bat['batID'], bat['numOfSeq'], pop['population'])
		all_seq_list += seq_result
	
	# transition
	# print('transition')
	all_tran_list = sf.tran_count(all_seq_list)
	tran_type_list_5 = {key: value for key, value in all_tran_list.items() if value >= 5}
	print(pop['population'])
	nt_tran_type_dict = {'N/N': 0, 'NT/NT': 0, 'T/T': 0, 'N/NT': 0, 'N/T': 0, 'NT/T': 0, 'NT/N': 0, 'T/N': 0, 'T/NT': 0}
	for tran in tran_type_list_5.keys():
		# print(tran)
		tran2nt = sf.seq2nt(tran)
		for nt_tran in nt_tran_type_dict.keys():
			if tran2nt == nt_tran:
				nt_tran_type_dict[nt_tran] += tran_type_list_5[tran]

	print(nt_tran_type_dict)
