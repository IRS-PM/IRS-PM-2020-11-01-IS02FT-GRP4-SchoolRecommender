from .create_info import getSchoolMajor
from .predict_new import returnSchoolMajor


def forwad(info,dT_level):
    getSchoolMajor(info,dT_level)
    top3 = returnSchoolMajor()
    return top3
