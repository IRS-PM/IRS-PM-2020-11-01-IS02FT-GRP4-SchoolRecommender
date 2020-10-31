import xlwt
import xlrd
import random
from xlutils.copy import copy
import os
current_path = os.path.dirname(__file__)
def getSchoolMajor(info,dT_level):
	rbook = xlrd.open_workbook(current_path+'/PM_DATA_JITUO_Processed.xlsx')
	rbook.sheets()
	#school_level
	#school_dict = {level:[school_name]}
	school_sheet = rbook.sheet_by_index(3) 

	school_dic = {1:[],2:[],3:[],4:[],5:[]}
	cols = [4,5,6,7,8]

	#school_level map
	for col in cols:
		for row in school_sheet.get_rows():
			name_column = row[col]
			if type(name_column.value)  == type(1.0):
				#print('aaa')
				continue 
			#print(name_column.value) 
			school_name = name_column.value.rstrip()
			if school_name != "":
				school_dic[col-3].append(school_name)

	rbook = xlrd.open_workbook(current_path+'/PM_DATA_JITUO_Processed.xlsx')
	rbook.sheets()

	random_id = random.sample(range(1,8), 3)

	#school_major map
	#major_dic = {'school_name':{'major_category':[major_name]}}
	major_sheet = rbook.sheet_by_index(2) 
	major_dic = {}
	ncol = major_sheet.ncols

	for row in major_sheet.get_rows():
		school_name = row[0].value.rstrip()
		if school_name not in set(major_dic.keys()):
				major_dic[school_name] = {}
		major_dic[school_name] = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
		for i in range(1, ncol):
			major_name = row[i].value.rstrip()
			if major_name == "":
				continue
			major_level = int(major_name[-1])
			major_name = major_name[:-2]
			#if major_level not in set(major_dic[school_name]):
			
			
			if major_name != "":
				major_dic[school_name][major_level].append(major_name)
	#print(major_dic)
	'''

	#school_major map
	#major_dic = {'school_name':{'major_category':[major_name]}}
	major_sheet = rbook.sheet_by_index(2) 
	major_dic = {}
	ncol = major_sheet.ncols

	for row in major_sheet.get_rows():
		school_name = row[0].value.rstrip()
		if school_name not in set(major_dic.keys()):
				major_dic[school_name] = []
		for i in range(1, ncol):
			major_name = row[i].value.rstrip()
			if major_name == "":
				continue
			major_level = int(major_name[-1])
			major_name = major_name[:-2]
			#if major_level not in set(major_dic[school_name]):
			
			if major_name != "":
				major_dic[school_name].append(major_name)
	'''
	res = []
	for school in school_dic[dT_level]:
		#print(school)
		
		for majorr in major_dic[school][info[1]]:
			temp = [i for i in info]
			temp.append(school)
			temp.append(majorr)
			#print(temp)
			res.append(temp)

	filefullpath = current_path+'/new_info.xls'
	if os.path.exists(filefullpath):
	    os.remove(filefullpath)

	rbook = xlrd.open_workbook(current_path+'/onehot_new.xls')       #读取excel文件，只能读取内容无法读取excel格式信息
	wbook = copy(rbook)                    #复制excel
	wsheet = wbook.get_sheet(0)
	nnrow = 410

	for i in range(len(res)):
		for j in range(len(res[i])):
			wsheet.write(nnrow+1+i, j, res[i][j]) 
	wbook.save(filefullpath) 

#info = [1,2,2,3,1,0,0,0,0,0]
#dT_level = 1
#getSchoolMajor(info,dT_level)


