# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def journal(request):
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
	{'id': 2,
	 'first_name': u'Юрій',
	 'last_name': u'Пукіш',
	 'ticket': 2322,
	 'image': "img/V1nvvYJCUtU.jpg"},
	)
    return render(request, 'journal.html', {'students':students})
