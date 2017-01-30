# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..model import Student
from ..group import Group
from ..ekz import Ekzamyn
def students_list(request):
    students = Student.objects.all()
     
   
# paginator        
    students = students.order_by('last_name', 'ticket', 'last_name', 'id', 'student_group')
  
    if request.GET.get ('reverse', '') == '1':
        students = students.reverse()
    paginator = Paginator(students, 3) 
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)
	
    return render(request, 'students_list.html', {'students': students})
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
