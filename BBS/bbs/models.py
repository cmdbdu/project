#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin


class User(models.Model):
	username = models.CharField(u'用户名',max_length=10)
	password =  models.CharField(u'密码',max_length=10)
	blog = models.BooleanField(u'是否博主',max_length=10,default=False)
	def __unicode__(self):
		return self.username
class Replay(models.Model):
	context = models.CharField(u'回复内容',max_length=200)
	replay = models.ManyToManyField('self',null=True,blank=True,verbose_name='回复内容')
	time = models.DateTimeField(u'时间',auto_now=True)
	author = models.ForeignKey(User,verbose_name='回复人')
	def __unicode__(self):
		return self.context
class Note(models.Model):
	reply=models.ManyToManyField(Replay,verbose_name='回复')
	title = models.CharField(u'标题',max_length=20)
	context = models.CharField(u'内容',max_length=1500)
	author = models.ForeignKey(User,verbose_name='作者人')
	def __unicode__(self):
		return self.title
