from django.db import models


from university.person.models import Student, Professor

class Department(models.Model):
    departmentno = models.IntegerField(db_column='departmentNo', primary_key=True)  # Field name made lowercase.
    field = models.CharField(max_length=45, blank=True, null=True)
    manager = models.ForeignKey(Professor, models.DO_NOTHING, to_field='personnelcode', blank=True, null=True)
    faculty = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'

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

class Course(models.Model):
    course_code = models.IntegerField(primary_key=True)
    course_group = models.IntegerField()
    course_subject = models.CharField(max_length=45)
    credit = models.IntegerField()
    classno = models.CharField(db_column='classNo', max_length=45)  # Field name made lowercase.
    examdate = models.DateField(db_column='examDate')  # Field name made lowercase.
    examtime = models.TimeField(db_column='examTime')  # Field name made lowercase.
    chart_presented_term = models.IntegerField()
    # Field name made lowercase.
    deptno = models.ForeignKey(Department, models.DO_NOTHING, db_column='deptNo', to_field='departmentno')
    # Field name made lowercase.
    profno = models.ForeignKey(Professor, models.DO_NOTHING, db_column='profNo', to_field='personnelcode')
    term = models.ForeignKey(Term, models.DO_NOTHING)
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

class Session(models.Model):
    # The composite primary key (course_code, session_id) found, that is not supported. The first column is selected.
    course_code = models.OneToOneField(Course, models.DO_NOTHING, db_column='course_code', primary_key=True)
    session_id = models.IntegerField()
    s_date = models.DateField(db_column='S_date', blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'
        unique_together = (('course_code', 'session_id'),)

class RollCall(models.Model):
    # Field name made lowercase. The composite primary key (studentNo, session_course_code, session_id) found,
    # that is not supported. The first column is selected.
    studentno = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentNo', primary_key=True)
    session_course_code = models.ForeignKey(Session, models.DO_NOTHING, db_column='session_course_code')
    session = models.ForeignKey(Session, models.DO_NOTHING, to_field='session_id', related_name='rollcall_session_set')
    ispresent = models.IntegerField(db_column='isPresent', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roll_call'
        unique_together = (('studentno', 'session_course_code', 'session'),)

class TakeCourses(models.Model):
    # Field name made lowercase. The composite primary key (studentNo, course_code) found, that is not supported.
    # The first column is selected.
    studentno = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentNo', primary_key=True)
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code')
    student_grade = models.FloatField(blank=True, null=True)
    professor_grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'take_courses'
        unique_together = (('studentno', 'course_code'),)
