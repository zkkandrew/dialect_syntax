import pymysql.cursors
from collections import Counter

def connect_db():
  return pymysql.connect(host='localhost', port=8889, user='root', password='root', db='yu', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

def seq2syl(seq): # str
  syl_list = seq.split('/')
  return syl_list


def get_colum(colum, table): # str str
  connection = connect_db()
  with connection.cursor() as cursor:
    seq_select = "SELECT `" + colum + "` FROM " + table
    cursor.execute(seq_select)
    seq_list = cursor.fetchall()
    return seq_list

def get_colums(colums, table): # list str
  connection = connect_db()
  colums_str = ''
  for col in colums:
    colums_str += col+', '
    
  with connection.cursor() as cursor:
    seq_select = "SELECT " + colums_str[0:-2] + " FROM " + table# + " LIMIT 20"
    cursor.execute(seq_select)
    seq_list = cursor.fetchall()
    return seq_list

def get_colums_where(colums, table, col_where, col_value):
  connection = connect_db()
  colums_str = ''
  for col in colums:
    colums_str += col+', '
    
  with connection.cursor() as cursor:
    seq_select = "SELECT " + colums_str[0:-2] + " FROM " + table + " WHERE " + col_where + "='" + col_value+"'"
    cursor.execute(seq_select)
    seq_list = cursor.fetchall()
    return seq_list

def seq2tran(seq): # str
  syl_list = seq2syl(seq)
  if len(syl_list) > 1:
    tran_list = []
    for indx in range(1, len(syl_list)):
      tran_list.append(syl_list[indx-1] + '/' + syl_list[indx])

    return tran_list

def get_syl_of_position(sequence, position): #str int
  # get the syllable on the requested position of a sequence
  if type(sequence) != str:
    sequence = sequence['sequence']
  syl_list = sequence.split('/')
  if len(syl_list) >= position+1:
    return syl_list[position]

def get_nt_syl(syl): # str
  connection = connect_db()
  with connection.cursor() as cursor:
    sql = 'SELECT nt3 FROM nt WHERE syllable="' + syl +'"'
    cursor.execute(sql)
    nt_syl = cursor.fetchall()
  
    return nt_syl[0]['nt3']

def seq2nt(seq): # str
  if type(seq) != str:
    seq = seq['sequence']
  syl_list = seq.split('/')
  nt_syl_list = []
  for syl in syl_list:
    nt_syl = get_nt_syl(syl)
    nt_syl_list.append(nt_syl)

  nt_seq = '/'.join(nt_syl_list)
  return nt_seq

def unique_two_adjacent(seq): # str
  if seq.find('/') != -1:
    syl_list = seq.split('/')
    indx_del = []
    syl_list_new = []
    for indx in range(0, len(syl_list)-1):
      if syl_list[indx] == syl_list[indx+1]:
        indx_del.append(indx)
    for indx, syl in enumerate(syl_list):
      if indx not in indx_del:
        syl_list_new.append(syl_list[indx])
    seq_new = '/'.join(syl_list_new)
    return seq_new
  else:
    return seq



def get_seq_list(table_name): #str
  all_seq_dict = get_colum('sequence', table_name)
  all_seq_list = []
  for seq in all_seq_dict:
    all_seq_list.append(seq['sequence'])
  return all_seq_list

def syl_count(seq_list):
  all_syl_list = []
  for seq in seq_list:
    syl_list = seq.split('/')
    all_syl_list += syl_list
  syl_type_list = Counter(all_syl_list)
  return syl_type_list

def tran_count(seq_list):
  all_tran_list = []
  for seq in seq_list:
    if seq.find('/') != -1:
      tran_list = seq2tran(seq)
      all_tran_list += tran_list
  tran_type_list = Counter(all_tran_list)
  return tran_type_list

def position_count(seq_list):
  # only count the first four position
  position_dict = {
    "position0": '',
    "position1": '',
    "position2": '',
    "position3": ''
  }
  for seq in seq_list:
    syl_list = seq2syl(seq)
    for idx, syl in enumerate(syl_list):
      if idx <= 3:
        position_dict['position'+str(idx)] += syl+'/'
  position_result = []
  for po, syl_str in position_dict.items():
    po_syl_list = syl_str[0:-1].split('/')
    po_syl_count = Counter(po_syl_list)
    position_result.append(po_syl_count)
  return position_result

def seq_type_count(seq_list):
  seq_type_list = []
  for seq in seq_list:
    nt_seq = seq2nt(seq)
    nt_seq_type = unique_two_adjacent(nt_seq)
    seq_type_list.append(nt_seq_type)

  seq_type_list_count = Counter(seq_type_list)
  return seq_type_list_count





