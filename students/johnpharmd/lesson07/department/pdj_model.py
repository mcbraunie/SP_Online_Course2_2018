"""
    pjd_model.py -- person/job/department model
    Modified from personjob_model.py, credit to UW Python 220
    Simple database example with Peewee ORM, sqlite, and Python
    Here we define the schema

"""

from peewee import *
from datetime import *


database = SqliteDatabase('pdj.db')
database.connect()
database.execute_sql('PRAGMA foreign_keys = ON;')


class BaseModel(Model):
    class Meta:
        database = database


class Person(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.
    """
    person_name = CharField(primary_key=True, max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


class Department(BaseModel):
    """
        This class defines Department, which maintains details of
        a given Department.
    """
    department_name = CharField(primary_key=True, max_length=30)
    department_number = CharField(max_length=4)
    department_manager_name = CharField(max_length=30)
    # job_name = ForeignKeyField(Job, related_name='was_held_by', null=False)


class Job(BaseModel):
    """
        This class defines Job, which maintains details of past Jobs
        held by a Person.
    """
    job_name = CharField(primary_key=True, max_length=30)
    department_name = ForeignKeyField(Department, null=False)
    start_date = DateField(formats='YYYY-MM-DD')
    end_date = DateField(formats='YYYY-MM-DD')
    salary = DecimalField(max_digits=7, decimal_places=2)
    person_employed = ForeignKeyField(Person, related_name='was_filled_by', null=False)
    duration_in_days = IntegerField()


class PersonNumKey(BaseModel):
    """
        This class defines Person, which maintains details of someone
        for whom we want to research career to date.

        *** I am implemented with a numeric PK that is generated by the system ***
    """
    person_name = CharField(max_length=30)
    lives_in_town = CharField(max_length=40)
    nickname = CharField(max_length=20, null=True)


database.close()
