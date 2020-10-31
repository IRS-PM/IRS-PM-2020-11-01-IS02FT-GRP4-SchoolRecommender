"""
1. 将user输入的现实数据转换成模型需要的字段（GPA/...）
2. 设置每个字段的权重，输出最终的评分（0-100），用于给出超过%多少人
"""
import os
import pickle
import pandas as pd
import numpy as np
from sklearn import tree
from ipdb import set_trace
from results.excel import excel
current_path = os.path.dirname(__file__)

class DecisionTable():
    def __init__(self):
        # self.database = database
        self.inpvalue = [
            "Country", "school", "major", "gpa_scale", "gpa_score",
            "language_type", "language_score", "intern", "work", "paper",
            "competition", "exchange", "scholarship", "entrance",
            "entrance_score"]
        self.outvalue = [
            "evaluation_level", "Exceed Percent", "Graduation School",
            "GPA", "Language", "Entrance_Test", "Other", "lifescore"
        ]
        #### Output Value ####
        self.level_map = {1: "S", 2: "A", 3: "C"}
        self.school_map = {1: "S", 2: "A", 3: "B", 4: "C", 5: "D", 6: "D"}
        self.gpa_map = {1: "S", 2: "A", 3: "B", 4: "C", 5: "D"}
        self.language_map = {1: "S", 2: "A", 3: "B", 4: "C", 5: "D"}
        # self.entrance_map = {}
        
        #### Model Related ####
        self.model_path = current_path + '/NewData/decision_tree.pkl'
        self.lifescore_db = current_path + '/NewData/lifescore_db.pkl'

        model_pkl = open(self.model_path, 'rb')
        self.model = pickle.load(model_pkl)
        print("Loading Model from: ", self.model_path)

        f = open(self.lifescore_db, 'rb')
        self.ls_db = pickle.load(f)
        print("Lifescore Database Identities: ", len(self.ls_db))

    def check_integrity(self, inp):
        inp_key = inp.keys()
        assert all([x in inp_key for x in self.inpvalue]), "missing input keys"

    def _encode(self, inp):
        language_rank = self._language_encode(inp["language_type"], inp["language_score"])
        gpa_rank = self._gpa_encode(inp['gpa_scale'], inp['gpa_score'])
        school_rank = self._school_encode(inp['school'])
        has_intern = 1 if len(inp['intern']) >= 1 else 0
        has_work = 1 if len(inp['work']) >= 1 else 0
        has_paper = 1 if len(inp['paper']) >= 1 else 0
        has_exchange = 1 if len(inp['exchange']) >= 1 else 0
        has_scholarship = 1 if len(inp['scholarship']) >= 1 else 0
        has_competition = 1 if len(inp['competition']) >= 1 else 0

        return [
            school_rank, gpa_rank, language_rank, has_intern, has_work,
            has_paper, has_competition, has_exchange, has_scholarship]

    def _others_pred(self, inp):
        other_sum = 0
        inp = inp[3:]
        for x in inp:
            other_sum = other_sum + x
        
        if x >= 5:
            return "S"
        elif x >= 4 and x < 5:
            return "A"
        elif x >= 3 and x < 4:
            return "B"
        elif x >= 2 and x < 3:
            return "C"
        else:
            return "D"


    def _model_pred(self, inp):
        """
        Only allow one input at a time
        """
        pred = self.model.predict([inp])

        return pred[0]
        

    def _compute_lifescore(self, encode_inp):
        # map into 0~1: x / xarr.max() -> lifescore
        cur_ls = \
            (6-encode_inp[0]) * 10 + \
            (5-encode_inp[1]) * 6 + \
            (5-encode_inp[2]) * 3 + \
            encode_inp[3] * 3 + \
            encode_inp[4] * 3 + \
            encode_inp[5] * 4 + \
            encode_inp[6] * 3 + \
            encode_inp[7] * 3 + \
            encode_inp[8] * 2

        cur_ls = cur_ls / self.ls_db.max()
        self.ls_db = self.ls_db / self.ls_db.max()

        cur_ls = np.clip(cur_ls, 0.25, 0.99) # clip into [0.25, 0.99] 
        exceed_percent = (cur_ls > self.ls_db).sum() / len(self.ls_db)
        return cur_ls, exceed_percent

    def forward(self, inp):
        """
        input:
        - inp: dict
            - school: string
        output:
        - result: dict
            - pred_school
            - pred_others
        """
        self.check_integrity(inp)
        encode_inp = self._encode(inp)
        assert len(encode_inp) == 9
        pred_rank = self._model_pred(encode_inp)
        pred_level = self.level_map[pred_rank]
        print("Pred Level: ", pred_level)

        pred_school = self.school_map[encode_inp[0]] # string
        pred_gpa = self.gpa_map[encode_inp[1]] # string
        pred_language = self.language_map[encode_inp[2]] # string
        pred_entrance_test = "A" # use default
        pred_others = self._others_pred(encode_inp) # string
        int_school = encode_inp[0]
        int_major = inp["major"] # keep as input
        int_gpa = encode_inp[1]
        int_language = encode_inp[2]
        int_intern = encode_inp[3]
        int_work = encode_inp[4]
        int_paper = encode_inp[5]
        int_competition = encode_inp[6]
        int_exchange = encode_inp[7]
        int_scholarship = encode_inp[8]

        float_lifescore, pred_percent = self._compute_lifescore(encode_inp)
        print("Lifescore: {:.0f}%, Exceed {:.0f}% person".format(
            float_lifescore * 100, pred_percent * 100))

        result = {
            "evaluation_level": pred_level,
            "Exceed Percent": pred_percent,
            "Graduation School": pred_school,
            "GPA": pred_gpa,
            "Language": pred_language,
            "Entrance_Test": pred_entrance_test,
            "Other": pred_others,
            "school": int_school,
            "major": int_major,
            "gpa_score": int_gpa,
            "language": int_language,
            "intern": int_intern,
            "work": int_work,
            "paper": int_paper,
            "competition": int_competition,
            "exchange": int_exchange,
            "scholarship": int_scholarship,
            "lifescore": float_lifescore,
        }

        return result

    def _school_encode(self, school):
        # score_map = {
        #     "Tsinghua University/Beijing University": 1, 
        #     "SJTU/FUDAN/NJU/ZJU/USTC": 2,
        #     "HIT/XJTU": 3,
        #     "BUPT/CUFE/SUFE/UIBE": 4,
        #     "Other "985" universities": 4,
        #     "Other "211" universities": 5,
        #     "Overseas univeristy": 2,
        #     "Others": 6}
        score_map = {1:1, 2:2, 3:3, 4:4, 5:4, 6:5, 7:2, 8:6}
        return score_map[school]

    def _language_encode(self, tp, score):
        if tp == "TOEFL":
            if score >= 110:
                return 1
            elif score >= 105 and score < 110:
                return 2
            elif score >= 95 and score < 105:
                return 3
            elif score >= 85 and score < 95:
                return 4
            elif score >= 0 and score < 85:
                return 5
            else:
                raise Exception("Invalid score(TOEFL): ", score)
        elif tp == "IELTS":
            if score >= 8.0:
                return 1
            elif score >= 7.5 and score < 8.0:
                return 2
            elif score >= 7 and score < 7.5:
                return 3
            elif score >= 6 and score < 7:
                return 4
            elif score >= 0 and score < 6:
                return 5
            else:
                raise Exception("Invalid score(IELTS): ", score)
        else:
            raise Exception("Unsupported Language Type: ", tp)

    def _gpa_encode(self, tp, score):
        if tp == 100.0:
            if score >= 95 and score <= 100:
                return 1
            elif score >= 90 and score < 95:
                return 2
            elif score >= 85 and score < 90:
                return 3
            elif score >= 80 and score < 85:
                return 4
            elif score >= 0 and score < 80:
                return 5
            else:
                raise Exception("Invalid score(GPA): ", score)
        elif tp == 4.0:
            if score >= 3.95 and score <= 4.0:
                return 1
            elif score >= 3.81 and score < 3.95:
                return 2
            elif score >= 3.58 and score < 3.81:
                return 3
            elif score >= 3.25 and score < 3.58:
                return 4
            elif score >= 0. and score < 3.25:
                return 5
            else:
                raise Exception("Invalid score(GPA): ", score)
        elif tp == 5.0:
            if score >= 4.5 and score <= 5.0:
                return 1
            elif score >= 4.0 and score < 4.5:
                return 2
            elif score >= 3.5 and score < 4.0:
                return 3
            elif score >= 3.0 and score < 3.5:
                return 4
            elif score >= 0 and score < 3.0:
                return 5
            else:
                raise Exception("Invalid score(GPA): ", score)
        else:
            raise Exception("Unsupported GPA Type: ", tp)

if __name__ == '__main__':
    logic_table = DecisionTable()
    
    data = {
        "Country": "USA", 
        "school": 2, 
        "major": 4,
        "gpa_scale": 100.,
        "gpa_score": 90,
        "language_type": "IELTS",
        "language_score": 7.0,
        "intern": [{'industry':'bytedance','field': 'China', 'duration':"1"}], 
        "work": [{'industry':'bytedance','field': 'China', 'duration':"1"}], 
        "paper": [{'paper_level':'journal','quantity':1}],
        "competition": ['awad1','award2'], 
        "exchange": [{'school':'nus','duration':"1"}], 
        "scholarship": [{'level':'school','times':'4'}], 
        "entrance": "GRE",
        "entrance_score": 325.}

    data2 = {'Country': 'USA', 'school': 2, 'major': 4, 'language_type': 'TOEFL', 'language_score': 100, 'gpa_scale': 5, 'gpa_score': 5, 'entrance': 'GMAT', 'entrance_score': 325, 'work': '[{"industry":"","duration":""}]', 'paper': '[{"paper_level":"","quantity":""}]', 'intern': '[{"industry":"","duration":""}]', 'scholarship': '[{"level":"","times":""}]', 'exchange': '[{"school":"","duration":""}]', 'competition': '[{"award":"","times":""}]'}

    result = logic_table.forward(data)
    print(result)
    result_excel = excel("result_dt.xlsx")
    j=1
    row, column = result_excel.getRowsClosNum()
    for key, value in result.items():
        result_excel.setCellValue(row+1, j, value)
        j = j+1

    result_from_excel = result_excel.getRowValues(row)
    print(result_from_excel)


    print("Happy Ending...")