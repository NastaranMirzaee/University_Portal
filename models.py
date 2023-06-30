# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    course_code = models.IntegerField(primary_key=True)
    course_group = models.IntegerField()
    course_subject = models.CharField(max_length=45)
    credit = models.IntegerField()
    classno = models.CharField(db_column='classNo', max_length=45)  # Field name made lowercase.
    examdate = models.DateField(db_column='examDate')  # Field name made lowercase.
    examtime = models.TimeField(db_column='examTime')  # Field name made lowercase.
    chart_presented_term = models.IntegerField()
    deptno = models.ForeignKey('Department', models.DO_NOTHING, db_column='deptNo', to_field='departmentno')  # Field name made lowercase.
    profno = models.ForeignKey('Professor', models.DO_NOTHING, db_column='profNo', to_field='personnelcode')  # Field name made lowercase.
    term = models.ForeignKey('Term', models.DO_NOTHING)
    is_digital_signature = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class CourseSchedule(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)
    course_time = models.TimeField(blank=True, null=True)
    course_day = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course-schedule'


class Department(models.Model):
    departmentno = models.IntegerField(db_column='departmentNo', primary_key=True)  # Field name made lowercase.
    field = models.CharField(max_length=45, blank=True, null=True)
    manager = models.ForeignKey('Professor', models.DO_NOTHING, to_field='personnelcode', blank=True, null=True)
    faculty = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Food(models.Model):
    food_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(unique=True, max_length=45)
    meal = models.CharField(max_length=45)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'food'


class FoodReservation(models.Model):
    food = models.OneToOneField(Food, models.DO_NOTHING, primary_key=True)  # The composite primary key (food_id, studentNo) found, that is not supported. The first column is selected.
    studentno = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentNo', to_field='studentno')  # Field name made lowercase.
    food_reservation_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'food_reservation'
        unique_together = (('food', 'studentno'),)


class LeisureClass(models.Model):
    leisure_class = models.OneToOneField('Sport', models.DO_NOTHING, primary_key=True)
    l_from = models.DateField(db_column='L_from', blank=True, null=True)  # Field name made lowercase.
    l_to = models.DateField(db_column='L_to', blank=True, null=True)  # Field name made lowercase.
    l_time = models.TimeField(db_column='L_time', blank=True, null=True)  # Field name made lowercase.
    day1 = models.CharField(max_length=45, blank=True, null=True)
    day2 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leisure_class'


class Pool(models.Model):
    pool = models.OneToOneField('Sport', models.DO_NOTHING, primary_key=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pool'


class PoolReservation(models.Model):
    studentno = models.OneToOneField('Student', models.DO_NOTHING, db_column='studentNo', primary_key=True)  # Field name made lowercase. The composite primary key (studentNo, pool_id) found, that is not supported. The first column is selected.
    pool = models.ForeignKey(Pool, models.DO_NOTHING)
    from_field = models.TimeField(db_column='from', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    to = models.TimeField(blank=True, null=True)
    date_pool = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pool_reservation'
        unique_together = (('studentno', 'pool'),)


class Professor(models.Model):
    personnelcode = models.IntegerField(db_column='personnelCode', primary_key=True)  # Field name made lowercase.
    nationalcode = models.CharField(db_column='nationalCode', unique=True, max_length=10)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=45)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=12)  # Field name made lowercase.
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=100, blank=True, null=True)
    lasteducationcertificate = models.CharField(db_column='lastEducationCertificate', max_length=45)  # Field name made lowercase.
    gender = models.CharField(max_length=6)
    degree = models.CharField(max_length=45)
    supervisor_flag = models.IntegerField()
    department_manager_flag = models.IntegerField(db_column='department_ manager_flag')  # Field renamed to remove unsuitable characters.
    deptno = models.ForeignKey(Department, models.DO_NOTHING, db_column='deptNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor'


class RegisterLeisureClass(models.Model):
    studentno = models.OneToOneField('Student', models.DO_NOTHING, db_column='studentNo', primary_key=True)  # Field name made lowercase. The composite primary key (studentNo, leisure_class_id) found, that is not supported. The first column is selected.
    leisure_class = models.ForeignKey(LeisureClass, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'register_leisure_class'
        unique_together = (('studentno', 'leisure_class'),)


class Research(models.Model):
    research_code = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    book_flag = models.IntegerField(blank=True, null=True)
    paper_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'research'


class ResearchReservation(models.Model):
    research_code = models.OneToOneField(Research, models.DO_NOTHING, db_column='research_code', primary_key=True)  # The composite primary key (research_code, studentNo) found, that is not supported. The first column is selected.
    studentno = models.ForeignKey('Student', models.DO_NOTHING, db_column='studentNo', to_field='studentno')  # Field name made lowercase.
    r_from = models.DateField(blank=True, null=True)
    r_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'research_reservation'
        unique_together = (('research_code', 'studentno'),)


class RollCall(models.Model):
    studentno = models.OneToOneField('Student', models.DO_NOTHING, db_column='studentNo', primary_key=True)  # Field name made lowercase. The composite primary key (studentNo, session_course_code, session_id) found, that is not supported. The first column is selected.
    session_course_code = models.ForeignKey('Session', models.DO_NOTHING, db_column='session_course_code')
    session = models.ForeignKey('Session', models.DO_NOTHING, to_field='session_id', related_name='rollcall_session_set')
    ispresent = models.IntegerField(db_column='isPresent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roll_call'
        unique_together = (('studentno', 'session_course_code', 'session'),)


class Session(models.Model):
    course_code = models.OneToOneField(Course, models.DO_NOTHING, db_column='course_code', primary_key=True)  # The composite primary key (course_code, session_id) found, that is not supported. The first column is selected.
    session_id = models.IntegerField()
    s_date = models.DateField(db_column='S_date', blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'
        unique_together = (('course_code', 'session_id'),)


class Sport(models.Model):
    s_id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    capacity = models.CharField(max_length=45)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sport'


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
    deptno = models.ForeignKey(Department, models.DO_NOTHING, db_column='deptNo', blank=True, null=True)  # Field name made lowercase.
    supervisor = models.ForeignKey(Professor, models.DO_NOTHING, blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)
    passed_credit = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    taken_credit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class TakeCourses(models.Model):
    studentno = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentNo', primary_key=True)  # Field name made lowercase. The composite primary key (studentNo, course_code) found, that is not supported. The first column is selected.
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code')
    student_grade = models.FloatField(blank=True, null=True)
    professor_grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'take_courses'
        unique_together = (('studentno', 'course_code'),)


class Term(models.Model):
    term_id = models.IntegerField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    semesterno = models.IntegerField(db_column='semesterNo', blank=True, null=True)  # Field name made lowercase.
    selection_unit_start_date = models.DateField(blank=True, null=True)
    selection_unit_end_date = models.DateField(blank=True, null=True)
    delete_lesson_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'term'
