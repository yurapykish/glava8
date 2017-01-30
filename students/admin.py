from django.contrib import admin
from model import Student
from group import Group
from ekz import Ekzamyn 
# Register your models here.
admin.site.register(Ekzamyn)
admin.site.register(Group)
admin.site.register(Student)
