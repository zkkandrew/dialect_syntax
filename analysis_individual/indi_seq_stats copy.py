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
for pop in constant.halfIndividuals:
	# if pop['population'] == 'baoji_del':
	print(pop['population'])
	all_seq_list = []
	for bat in pop['seqPerBat']:
		# print(bat['batID'], bat['numOfSeq'])
		seq_result = isf.get_seq_by_indi_num(bat['batID'], bat['numOfSeq'], pop['population'])
		all_seq_list += seq_result

	# syllable
	print('syllable')
	all_syl_list = sf.syl_count(all_seq_list)
	syl_type_list_5 = {key: value for key, value in all_syl_list.items() if value >= 5}
	all_syl_num_dict_list.append(syl_type_list_5)
	# print(syl_type_list_5)
	syl_stats_result = isf.chi_stats(syl_type_list_5)
	print(syl_stats_result)

	# transition
	print('transition')
	all_tran_list = sf.tran_count(all_seq_list)
	tran_type_list_5 = {key: value for key, value in all_tran_list.items() if value >= 5}
	all_tran_num_dict_list.append(tran_type_list_5)
	# print(tran_type_list_5)
	tran_stats_result = isf.chi_stats(tran_type_list_5)
	print(tran_stats_result)

	# position
	print('position')
	all_each_po_num_dict_list = []
	po_result = sf.position_count(all_seq_list)
	for idx, po in enumerate(po_result):
		po_num_list = {x: y for x, y in po.items() if y > 1} # only count more than one as written in the paper
		all_each_po_num_dict_list.append(po_num_list)
		print('position'+str(idx))
		po_stats_result = isf.chi_stats(po_num_list)
		print(po_stats_result)

	all_po_num_dict_list.append(all_each_po_num_dict_list)

	# sequence
	print('sequence')
	seq_result = sf.seq_type_count(all_seq_list)
	seq_num_list_5 = {x:y for x, y in seq_result.items() if y >= 5}
	all_seq_num_dict_list.append(seq_num_list_5)
	seq_stats_result = isf.chi_stats(seq_num_list_5)
	print(seq_stats_result)


# among three populations

# syllable
syl_comm_three_list_5 = all_syl_num_dict_list[0].keys() & all_syl_num_dict_list[0].keys() & all_syl_num_dict_list[0].keys()
print(syl_comm_three_list_5)
