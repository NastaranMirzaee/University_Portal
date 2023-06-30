from django.db import models

from university.service.models import Department

class Professor(models.Model):
    personnelcode = models.IntegerField(db_column='personnelCode', primary_key=True)  # Field name made lowercase.
    nationalcode = models.CharField(db_column='nationalCode', unique=True, max_length=10)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=12)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=100, blank=True, null=True)
    # Field name made lowercase.
    lasteducationcertificate = models.CharField(db_column='lastEducationCertificate', max_length=45)
    gender = models.CharField(max_length=6)
    degree = models.CharField(max_length=45)
    supervisor_flag = models.IntegerField()
    # Field renamed to remove unsuitable characters.
    department_manager_flag = models.IntegerField(db_column='department_ manager_flag')
    # Field name made lowercase.
    deptno = models.ForeignKey(Department, models.DO_NOTHING, db_column='deptNo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'

class Student(models.Model):
    studentno = models.IntegerField(db_column='studentNo', primary_key=True)  # Field name made lowercase.
    nationalcode = models.CharField(db_column='nationalCode', unique=True, max_length=10)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=12)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=100, blank=True, null=True)
    entranceyear = models.IntegerField(db_column='entranceYear')  # Field name made lowercase.
    gender = models.CharField(max_length=6)
    birthdate = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    deptno = models.ForeignKey(Department, models.DO_NOTHING, db_column='deptNo', blank=True, null=True)
    supervisor = models.ForeignKey(Professor, models.DO_NOTHING, blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)
    passed_credit = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    taken_credit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
