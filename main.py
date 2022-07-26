import ui_global
from pony.orm.core import db_session
from pony import orm
from pony.orm import Database, Required, Set, select, commit
import json
# import os
# import sqlite3
# from sqlite3.dbapi2 import Error
# from datetime import datetime
# from PIL import Image


# def main_init_start(hashMap,_files=None,_data=None):
#	ui_global.init()
#	return hashMap

def main_list_of_offers(hashMap, _files=None, _data=None):
	# ---> go in list purchase
	if   hashMap.get('listener') == 'btn__purchase':
		hashMap.put('ShowScreen', 'Список закупок')
	# ---> go in list receipt
	#elif hashMap.get('listener') == 'btn__receipt':
	#	hashMap.put('ShowScreen', 'Список поступлений')
	# ---> reports
	#elif hashMap.get('listener') == 'btn__report':
	#	hashMap.put('ShowScreen', 'Отчёт о поступлениях')
	# ---> go in list goods
	#elif hashMap.get('listener') == 'btn__goods':
	#	hashMap.put('ShowScreen', 'Товары')
	
	return hashMap

# ----- Purchase (Закупка) ------------------------------------------------------------------------------------- #
def goback_from_purch(hashMap, _files=None, _data=None):
	if hashMap.get('listener') == 'btn__back':
		hashMap.put('ShowScreen', 'Главное меню')
	elif hashMap.get('listener') == 'TableClick':
		jrecord = json.loads(hashMap.get('selected_line'))
		hashMap.put('cap__main_menu', '%s %s' % (jrecord['purchase'], jrecord['id']))
		hashMap.put('ShowScreen', 'Закупка')
	
	return hashMap

def goback_from_purchitems(hashMap, _files=None, _data=None):
	if hashMap.get('listener') == 'btn__back':
		hashMap.put('ShowScreen', 'Список закупок')
	
	return hashMap

def table_list_purchase(hashMap, _files=None, _data=None):
	table = {
		'type': 'table',
		'textsize': '20',
		'columns': [
			{
				'name'  : 'purchase',
				'header': 'Закупка',
				'weight': '3'
			},
			{
				'name'  : 'id',
				'header': 'Номер',
				'weight': '2'
			},
		]
	}
	
	# query = select(item for item in ui_global.Ai_Purchase)
	# rows = []
	# count = 7
	# if not query:
	#	rows.append({ 'purchase': 'Тестовая запись', 'id': '0' * count })
	# else:
	#	for item in query:
	#		null = '0' * (count - len(str(item.id)))
	#		rows.append({ 'purchase': item.name, 'id': '%s%s' % (null, item.id) })
	
	rows = []
	count = 7
	range_tb = 5
	if range_tb == 0:
		rows.append({ 'purchase': 'Тестовая запись', 'id': '0' * count })
	else:
		for i in range(range_tb, 0, -1):
			null = '0' * (count - len(str(i)))
			rows.append({ 'purchase': 'Закупка_%s' % (i), 'id': '%s%s' % (null, i) })
	table['rows'] = rows
	hashMap.put('tab__purchase', json.dumps(table))
	
	return hashMap

def table_list_purchase_items(hashMap, _files=None, _data=None):
	table = {
		'type': 'table',
		'textsize': '20',
		'columns': [
			{
				'name'  : 'id',
				'header': 'id',
				'weight': '1'
			},
			{
				'name'  : 'product',
				'header': 'Товар',
				'weight': '3'
			},
			{
				'name'  : 'count',
				'header': 'Кол-во',
				'weight': '1'
			},
		]
	}
	
	rows = []
	jrecord = json.loads(hashMap.get('selected_line'))
	if jrecord['purchase'] == 'Закупка_2':
		items_tb = [['Молоток', '1'], ['Гвоздь 40', '64'], ['Краска', '1']]
		range_tb = len(items_tb)
		if range_tb == 0:
			rows.append({ 'id': '0', 'product': 'товар', 'count': '0' })
		else:
			for i in range(range_tb):
				rows.append({ 'id': str(i), 'product': items_tb[i][0], 'count': items_tb[i][1] })
	table['rows'] = rows
	hashMap.put('tab__purchase_items', json.dumps(table))