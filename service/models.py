from django.db import models

from university.person.models import Student

class Food(models.Model):
    food_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(unique=True, max_length=45)
    meal = models.CharField(max_length=45)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'food'

class FoodReservation(models.Model):
    # The composite primary key (food_id, studentNo) found, that is not supported. The first column is selected.
    food = models.OneToOneField(Food, models.DO_NOTHING, primary_key=True)
    # Field name made lowercase.
    studentno = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentNo', to_field='studentno')
    food_reservation_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'food_reservation'
        unique_together = (('food', 'studentno'),)

class Sport(models.Model):
    s_id = models.IntegerField(primary_key=True)
    price = models.IntegerField()
    capacity = models.CharField(max_length=45)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sport'

class LeisureClass(models.Model):
    leisure_class = models.OneToOneField(Sport, models.DO_NOTHING, primary_key=True)
    l_from = models.DateField(db_column='L_from', blank=True, null=True)  # Field name made lowercase.
    l_to = models.DateField(db_column='L_to', blank=True, null=True)  # Field name made lowercase.
    l_time = models.TimeField(db_column='L_time', blank=True, null=True)  # Field name made lowercase.
    day1 = models.CharField(max_length=45, blank=True, null=True)
    day2 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leisure_class'

class Pool(models.Model):
    pool = models.OneToOneField(Sport, models.DO_NOTHING, primary_key=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pool'

class PoolReservation(models.Model):
    # Field name made lowercase. The composite primary key (studentNo, pool_id) found, that is not supported.
    # The first column is selected.
    studentno = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentNo', primary_key=True)
    pool = models.ForeignKey(Pool, models.DO_NOTHING)
    # Field renamed because it was a Python reserved word.
    from_field = models.TimeField(db_column='from', blank=True, null=True)
    to = models.TimeField(blank=True, null=True)
    date_pool = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pool_reservation'
        unique_together = (('studentno', 'pool'),)

class RegisterLeisureClass(models.Model):
    # Field name made lowercase. The composite primary key (studentNo, leisure_class_id) found, that is not supported.
    # The first column is selected.
    studentno = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentNo', primary_key=True)
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
    # The composite primary key (research_code, studentNo) found, that is not supported. The first column is selected.
    research_code = models.OneToOneField(Research, models.DO_NOTHING, db_column='research_code', primary_key=True)
    # Field name made lowercase.
    studentno = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentNo', to_field='studentno')
    r_from = models.DateField(blank=True, null=True)
    r_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'research_reservation'
        unique_together = (('research_code', 'studentno'),)
