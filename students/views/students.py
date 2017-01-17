# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# FOR STUDEntS_List
def students_list(request):
    students = (
        {'id': 1,
	 'first_name': u'Віталій',
	 'last_name': u'Подоба',
	 'ticket': 2123,
	 'image': 'img/k4DBbnUiaW8.jpg'},
	{'id': 2,
	 'first_name': u'Андрій',
	 'last_name': u'Пукіш',
	 'ticket': 212,
	 'image': "img/k4DBbnUiaW8.jpg"},
	{'id': 3,
	 'first_name': u'Юрій',
	 'last_name': u'Пукіш',
	 'ticket': 2322,
	 'image': "img/V1nvvYJCUtU.jpg"},
	)
    return render(request, 'students_list.html', {'students': students})
def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
