from django.test import TestCase
from .models import student,other_info,School
# Create your tests here.
student_new = student(graduation_school="1", major="1",gpa_scale=4.0,gpa_score=3.9,language_type="IELTS",language_score=7.0,)