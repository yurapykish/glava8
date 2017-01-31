# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
#Student model

class Student (models.Model):

	class Meta(object):
	    verbose_name=u'Студенти',
	    verbose_name_plural= u'Студенти'


	first_name = models.CharField(
	    max_length=256,
	    blank=False,
	    verbose_name=u'Ім*я')

	last_name = models.CharField(
	    max_length=256,
	    blank=False,
	    verbose_name=u'Прізвище')

	middle_name = models.CharField(
	    max_length = 256, 
	    blank=True,
	    verbose_name= u'По-батькові',
	    default='')

	student_group = models.ForeignKey('Group',
	   verbose_name = u'Група',
	   blank = False, 
	   null = True,
 	   on_delete=models.PROTECT)
	
	birthday = models.DateField(
	    blank=True,
	    verbose_name=u'Дата народження',
	    null=True)
	
	photo = models.ImageField(
	    blank=True,
	    verbose_name=u'Фото',
	    null=True)
	
	ticket = models.CharField(
	    max_length=256,	
   	    blank=False,
	    verbose_name=u'Білет')
 
        notes = models.TextField(
	    blank=True,
	    verbose_name=u'Додаткові нотатки')
	
	def __unicode__(self):
	    return u'%s %s' % (self.first_name, self.last_name)


class Ekzamyn(models.Model):
	class Meta(object):
	    verbose_name=u'екзамени',
	    verbose_name_plural= u'екзамени'

	ekzamyn = models.CharField(
	    max_length=256,
	    blank=True,
	    null=True,
	    verbose_name=u'Предмет')
	
	ekzamyn_date = models.DateTimeField(
	    blank=True,
	    verbose_name=u'Дата і час проведення',
	    null=True)
	
	teacher = models.CharField(
	    max_length=256,
	    blank=True,
	    null=True,
	    verbose_name=u'Викладач')

 	ekz_group = models.ForeignKey('Group',
          verbose_name = u"Екзаменаційна група",
          blank=True,
          null=True,
          on_delete=models.SET_NULL)

	#inspector = models.OneToOneField('Student', verbose_name=u'Інспектор',
         #   max_length = 256,
          #  blank=True,
	   # null=True,
	    #on_delete=models.SET_NULL)

	
	    #if self.inspector and 
	   
	#      return u'%s %s' % (self.inspector.first_name, self.inspector.last_name)
	    
	def __unicode__(self):
            return u'%s' % (self.ekzamyn)
	      
	    
class Group (models.Model):
        
	class Meta(object):
  	    verbose_name=u'Групи'
      	    verbose_name_plural=u'Групи'

	title = models.CharField(
	    max_length = 256,
	    blank = False,
            verbose_name = u'Назва ГРУПИ')
	leader = models.OneToOneField('Student', verbose_name=u'Староста',
            max_length = 256,
            blank=True,
	    null=True,
	    on_delete=models.SET_NULL)
	notes = models.TextField(
	    blank=True,
	    verbose_name=u'Додаткові нотатки')
	
	def __unicode__(self):
	    if self.leader:

	      return u'%s(%s %s)' % (self.title, self.leader.first_name, self.leader.last_name)
	    else:
	      return u"%s" % (self.title,)

