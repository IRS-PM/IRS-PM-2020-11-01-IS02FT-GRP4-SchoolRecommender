from django.db import models

# Create your models here.
class student(models.Model):
    student_id = models.AutoField(db_column='Student_ID', primary_key=True)
    graduation_school = models.CharField(db_column='Graduation_School',max_length=100)
    major = models.CharField(db_column='Major',max_length=100)
    gpa_scale = models.FloatField(db_column='GPA_Scale',blank=False,null=True)
    gpa_score = models.FloatField(db_column='GPA_score',blank=False,null=True)
    language_type = models.CharField(db_column='TOEFL/IELTS',max_length=10)
    language_score = models.FloatField(db_column='Language_Score',blank=False,null=True)

# class work_intern(models.Model):
#     student_id = models.IntegerField(db_column='Student_ID', primary_key=True)
#     type = models.IntegerField(db_column='Type',blank=False,null=False)
#     company = models.CharField(db_column='Major',max_length=100)
#     # job = models.CharField(db_column='Job',max_length=100)
#     duration = models.IntegerField(db_column='Duration',blank=False,null=False)


class other_info (models.Model):
    student_id = models.IntegerField(db_column='Student_ID', primary_key=True)
    type = models.IntegerField(db_column='Type',blank=False,null=False)
    level = models.CharField(db_column='Level',max_length=100)
    quantity = models.IntegerField(db_column='Quantity',blank=False,null=False)

class School(models.Model):
    school_id = models.IntegerField(db_column='School_ID', primary_key=True)
    school_name = models.CharField(db_column='School_Name',max_length=100)
    location =  models.CharField(db_column='Location',max_length=100,null=True)
    icon =  models.CharField(db_column='Icon',max_length=1000,blank=True,null=True)
    homepage =  models.CharField(db_column='Homepage',max_length=1000,blank=True)
    qsrank = models.CharField(db_column='QSRank',max_length=10,default="0")
    timesrank = models.CharField(db_column='TIMESRank',max_length=10,default="0")
    usnewsrank = models.CharField(db_column='USNewsRank',max_length=10,default="0")














