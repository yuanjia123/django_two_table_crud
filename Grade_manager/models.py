from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=200)
    #如果当前的表（班级表）和学生表有关联关系、 并且关联对象在另外一个表、可以通过学生表的表名小写_set。all()拿到这个表的所有学生
    def students(self):
        stus = self.student_set.all()
        return stus




class Student(models.Model):
    s_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200,null=True)
    g = models.ForeignKey(Grade, on_delete=models.CASCADE)