import syntax_function
from collections import Counter

# seq_list
baoji_all_seq_list = syntax_function.get_seq_list('baoji_del')
lantian_all_seq_list = syntax_function.get_seq_list('lantian_del')
jian_all_seq_list = syntax_function.get_seq_list('jian')


# syl_type_list
baoji_all_seq_str = '/'.join(baoji_all_seq_list)
baoji_all_syl = syntax_function.seq2syl(baoji_all_seq_str)
baoji_syl_type_list = Counter(baoji_all_syl)
# print(baoji_syl_type_list)
 
lantian_all_seq_str = '/'.join(lantian_all_seq_list)
lantian_all_syl = syntax_function.seq2syl(lantian_all_seq_str)
lantian_syl_type_list = Counter(lantian_all_syl)
# print(lantian_syl_type_list)

jian_all_seq_str = '/'.join(jian_all_seq_list)
jian_all_syl = syntax_function.seq2syl(jian_all_seq_str)
jian_syl_type_list = Counter(jian_all_syl)
# print(jian_syl_type_list)


# all_syl_type_list = list(baoji_syl_type_list.keys()) + list(lantian_syl_type_list.keys()) + list(jian_syl_type_list.keys())
# # print(set(all_syl_type_list))
# all_syl_type_list = sorted(set(all_syl_type_list))
# # print(all_syl_type_list)
# # for syl in all_syl_type_list:
# #   print(syl)

# nt_syl_list = ['T', 'T', 'NT', 'T', 'T', 'T', 'N', 'N', 'N', 'T', 'NT', 'T', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'NT', 'T', 'T', 'NT', 'NT', 'NT', 'T', 'T', 'NT', 'T', 'NT', 'NT', 'N', 'T', 'T']

# insert_str = ''
# for indx, syl in enumerate(all_syl_type_list):
#   insert_str += '("'+syl+'", "'+nt_syl_list[indx]+'"), '
# print(insert_str)

# connection = syntax_function.connect_db()
# with connection.cursor() as cursor:
#   nt_insert = "INSERT INTO nt (syllable, nt3) VALUES " + insert_str[:-2]
#   cursor.execute(nt_insert)

# baoji_all_tran_list = []
# for seq in baoji_all_seq_list:
#   nt_seq = syntax_function.seq2nt(seq)
#   nt_tran_list = syntax_function.seq2tran(nt_seq)
#   if nt_tran_list != None:
#     baoji_all_tran_list += nt_tran_list

# # print(baoji_all_tran_list)
# baoji_all_tran_type_dict = Counter(baoji_all_tran_list)
# # print(baoji_all_tran_type_dict)
# # for tran, num in baoji_all_tran_type_dict.items():
# #   print(tran, num)


# lantian_all_tran_list = []
# for seq in lantian_all_seq_list:
#   nt_seq = syntax_function.seq2nt(seq)
#   nt_tran_list = syntax_function.seq2tran(nt_seq)
#   if nt_tran_list != None:
#     lantian_all_tran_list += nt_tran_list

# # print(lantian_all_tran_list)
# lantian_all_tran_type_dict = Counter(lantian_all_tran_list)
# # print(lantian_all_tran_type_dict)
# for tran, num in lantian_all_tran_type_dict.items():
#   print(tran, num)

# print('\n')
# jian_all_tran_list = []
# for seq in jian_all_seq_list:
#   nt_seq = syntax_function.seq2nt(seq)
#   nt_tran_list = syntax_function.seq2tran(nt_seq)
#   if nt_tran_list != None:
#     jian_all_tran_list += nt_tran_list

# # print(jian_all_tran_list)
# jian_all_tran_type_dict = Counter(jian_all_tran_list)
# # print(jian_all_tran_type_dict)
# for tran, num in jian_all_tran_type_dict.items():
#   print(tran, num)

### seuquence types
# baoji_seq_type_list = []
# for seq in baoji_all_seq_list:
#   seq_nt = syntax_function.seq2nt(seq)
#   seq_type = syntax_function.unique_two_adjacent(seq_nt)
#   baoji_seq_type_list.append(seq_type)

# baoji_seq_type_dict = Counter(baoji_seq_type_list)
# # print(baoji_seq_type_dict)
# # for seq, num in baoji_seq_type_dict.items():
# #   print(seq, num)

# lantian_seq_type_list = []
# for seq in lantian_all_seq_list:
#   seq_nt = syntax_function.seq2nt(seq)
#   seq_type = syntax_function.unique_two_adjacent(seq_nt)
#   lantian_seq_type_list.append(seq_type)

# lantian_seq_type_dict = Counter(lantian_seq_type_list)
# # print(lantian_seq_type_dict)
# for seq, num in lantian_seq_type_dict.items():
#   print(seq, num)

jian_seq_type_list = []
for seq in jian_all_seq_list:
  seq_nt = syntax_function.seq2nt(seq)
  seq_type = syntax_function.unique_two_adjacent(seq_nt)
  jian_seq_type_list.append(seq_type)

jian_seq_type_dict = Counter(jian_seq_type_list)
# print(jian_seq_type_dict)
# for seq, num in jian_seq_type_dict.items():
#   print(seq, num)