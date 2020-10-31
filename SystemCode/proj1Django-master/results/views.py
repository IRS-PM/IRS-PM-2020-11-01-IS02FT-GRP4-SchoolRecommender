import math
import os

import demjson
from django.shortcuts import render

# Create your views here.
from .models import student,other_info,School
from rest_framework.mixins import Response
from rest_framework.views import APIView
from .MapTabel import DecisionTable
from results.excel import excel
from results.FM.getRecommendation import forwad

current_path = os.path.dirname(__file__)


def response_success_200(res={}):
    """
    返回请求成功
    :param data_dict:
    :return: response(dict)
    """
    response = dict()
    response['msg'] = 'Request Success'
    response['result'] = res
    response['code'] = 200
    return Response(response, status=200)


def response_failed_400():
    """
    返回请求失败
    :return: response(dict)
    """
    response = dict()
    response['msg'] = 'Request Parameter Error'
    response['result'] = dict()
    response['code'] = 400
    return Response(response, status=400)

def WriteResult(result):
    #将decision table的返回值写入文件，方便后续取出
    file_path = current_path + "/result_dt.xlsx"
    print(current_path)
    result_excel = excel(file_path)
    j=1
    row, column = result_excel.getRowsClosNum()
    for key, value in result.items():
        result_excel.setCellValue(row+1, j, value)
        j = j+1


def GetLastResult():
    #取出 DT 返回的result
    file_path = current_path + "/result_dt.xlsx"
    result_excel = excel(file_path)
    row, column = result_excel.getRowsClosNum()
    result_from_excel = result_excel.getRowValues(row)
    return result_from_excel


class GetSchoolDetail(APIView):
    def post(self, request):
        school = School.objects.get(school_name = request.data.get('school_name'))
        location = school.location
        if location in ["US","USA"]:
            location = "United States"
        if location in ["Britain","UK","England"]:
            location = "United Kingdom"
        res = {"school_name":school.school_name,"location":location,"homepage":school.homepage,
               "icon":school.icon,"qsrank":school.qsrank,"timesrank":school.timesrank,
               "usnewsrank":school.usnewsrank}

        return response_success_200(res)

class GetEvaluationLevel(APIView):
    # 获取总评分等级
    def __init__(self):

        # self.evaluation_level = result["evaluation_level"]
        # self.exceed_percent = float(result["Exceed Percent"])
        # self.exceed_percent = math.floor(self.exceed_percent*100)

        last_result = GetLastResult()
        self.evaluation_level = last_result[0]
        self.exceed_percent = float(last_result[1])
        self.exceed_percent = math.floor(self.exceed_percent*100)

    def post(self,request):
        res={"evaluation_level":self.evaluation_level,"exceed_percent":self.exceed_percent}
        return response_success_200(res)

class GetLevelDetail(APIView):
    #获取各项的详情评级信息

    def __init__(self):
        last_result = GetLastResult()
        # self.graduate_school = result["Graduation School"]
        # self.GPA = result["GPA"]
        # self.language = result['Language']
        # self.entrance_test = result['Entrance_Test']
        # self.other = result["Other"]
        self.graduate_school = last_result[2]
        self.GPA = last_result[3]
        self.language = last_result[4]
        self.entrance_test = last_result[5]
        self.other = last_result[6]

    def post(self,request):
        res = {"graduate_school":self.graduate_school,"GPA":self.GPA,"language":self.language,
               "entrance_test":self.entrance_test,"other":self.other}
        print('[DEBUG]res in get LevelDetail:',res)
        return response_success_200(res)


class GetExceedInfo(APIView):
    pass

class GetRecommendSchool(APIView):
    #返回推荐的学校
    def post(self,request):
        locations = request.data["locations"]
        last_result = GetLastResult()
        level_map = {"S": 1, "A": 2, "C": 3}
        recom_school = forwad(last_result[7:17],level_map[last_result[0]])
        recom_school2 = self.getNewSchool(locations,recom_school)[:10]
        print('[DEBUG]recom_school2:',recom_school2)
        key = ["school","major","score","location"]
        res = []
        for i in range(len(recom_school2)):
            res.append(dict(zip(key, recom_school2[i])))


        return response_success_200(res)

    def getNewSchool(self,locations,recom_school):
        #根据选择的国家限制，筛选一遍推荐的学校
        school_result = []
        print("[DEBUG]locations:",locations)
        sorted(recom_school, key=lambda x: x[2], reverse=True)

        for i in range(len(recom_school)):
            name = recom_school[i][0]
            try:
                school = School.objects.get(school_name=name)
            except:
                continue
            if school.location == "HongKong": school.location = "Hong Kong"
            if school.location in locations:
                recom_school[i].append(school.location)
                school_result.append(recom_school[i])
        # print('[DEBUG]school_result:',school_result)
        return school_result







class PutUsersInfo(APIView):
    def post(self,request):
        response = {}
        try:

            data = request.data
            print("[DEBUG]request_data:",data)

            student_new = student(graduation_school=str(data["school"]),major=str(data["major"]),
                                  language_type=data["language_type"],language_score=data["language_score"],
                                  gpa_scale=data["gpa_scale"],gpa_score=data["gpa_score"])

            student_new.save()
            logic_table = DecisionTable()
            result_temp = logic_table.forward(data)
            print("[DEBUG]result_temp:",result_temp)

            WriteResult(result_temp)
            response['msg'] = 'success'
            response['error_num'] = 0

        except  Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
            print("[DEBUG]putuserinfo:",str(e))
        return response_success_200(response)


