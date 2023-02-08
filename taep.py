


# INSERT INTO `taep_new`(`NB__SFM_S__N__S`,`NB__SFM_SFM`) VALUES (
# (SELECT count(*) from taep where transition like 'NB-SFM/S-N-S' and emitter LIKE '%13%'),
# (SELECT count(*) from taep where transition like 'NB-SFM/SFM' and emitter LIKE '%13%'),
# '13',
# 'LT')


import pymysql

connection = pymysql.connect(host='localhost', port=8889, user='root', password='root', db='yu', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

with connection.cursor() as cursor:
	sql_select = "SELECT * FROM taep_new"
	cursor.execute(sql_select)
	sql_list = cursor.fetchall()
	for seq in sql_list:
		emitter = seq['emitter']
		print("%"+emitter+"%")
		update_sql = "UPDATE taep_new SET `NB__SFM_S__N__S` = (SELECT count(*) from taep where transition like 'NB-SFM/S-N-S' and taep.emitter LIKE %s), `NB__SFM_SFM` = (SELECT count(*) from taep where transition like 'NB-SFM/SFM' and taep.emitter LIKE %s) WHERE taep_new.emitter = %s"
		cursor.execute(update_sql, ("%"+emitter+"%", "%"+emitter+"%", emitter))