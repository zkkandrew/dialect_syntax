from scipy import stats
####################
# stats.chisquare() : the observed and expected frequencies should be at least 5.and
####################
import random
import sys
sys.path.append("..")
import syntax_function as sf

def get_seq_by_indi_num(batID, seqNum, table):
	seq_list = sf.get_colums_where(['sequence'], table, 'emitter', batID)
	seq_list = [x['sequence'] for x in seq_list]
	random.shuffle(seq_list)
	seq_list_random = random.sample(seq_list, seqNum)
	return seq_list_random

def chi_stats(stats_dict):
	num_list = [y for x, y in stats_dict.items()]
	chi = stats.chisquare(num_list)
	return [chi[0], chi[1]]












