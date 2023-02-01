from peewee import *
from db_connection import db


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

d1 = data(2021,2,1)
d2 = data(2021,2,28)
for emloyee in Employees.select().where((Employees.employment_date >= d1)& (Employees.employment_date <= d2):
    print(employee.name,employee.last_name)


class Users(MetaClass):
    name = peewee.CharField(40)
    age = peewee.IntegerField()
    gender = peewee.CharField(40)
    nationality = peewee.CharField(40)


class Posts(MetaClass):
    title = peewee.CharField(40)
    description = peewee.CharField(40)
    user_id = peewee.ForeignKeyField(Users, related_name='posts') #


david = Users.get(id=1)
print(david.name)

for post in artyom.posts.select():
    print(post.title, post.description)

for user in Users.select().order_by(Users.name):
    print(user.name)

