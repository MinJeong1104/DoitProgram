from django.db import models

# Create your models here.
#강의에 대한 class 를 정의합니다. 기본적으로 charField로 선언하였습니다
#number = 학수번호, subnum = 분반, title=강의명, professor=교수명, downloadPath= 가상환경 내 위치, filename=위치 내 파일명, crawled_time=크롤링된 시간

class Class(models.Model):
    idnum=models.CharField(max_length=200,null=True,default='',primary_key=True)
    number = models.CharField(max_length=200,null=True,default='')
    title = models.CharField(max_length=200, null=True, default='')
    subnum= models.CharField(max_length=50,null=True,default='')
    professor = models.CharField(max_length=200, null=True, default='')
    downloadPath = models.CharField(max_length=200, null=True, default='')
    filename = models.CharField(max_length=200, null=True, default='')
    crawled_time = models.DateTimeField(auto_now=True,null=True)

class Todo(models.Model):
    days = models.CharField(max_length=50,null=True,default='')
    activities = models.CharField(max_length=50,null=True,default='')
    idnum = models.ForeignKey(Class, on_delete=models.CASCADE)
    weeks = models.CharField(max_length=50, null=True, default='')
    Ranges = models.CharField(max_length=50,null=True,default='')
    Materials = models.CharField(max_length=50,null=True,default='')
    Assignments = models.CharField(max_length=50,null=True,default='')
