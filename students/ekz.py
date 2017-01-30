# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#ekzamen model
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
	      
	    

