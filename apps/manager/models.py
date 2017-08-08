# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
# Create your models here.
from django.db import models
class Group(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='')
    info=models.CharField(max_length=100,default='')

class Storage(models.Model):
    id=models.AutoField(primary_key=True)#全局ID
    disk_size=models.CharField(max_length=100,default="")
    disk_path=models.CharField(max_length=100,default="")
    info=models.CharField(max_length=100,default="")

class Host(models.Model):
    # SYSTEM_NAMES=(u'',u'Windows Server 2006',u'Windows Server 2008',u'Centos 6.5',u'Centos 7.1')
    # SYSTEM_VALS=(0,1,2,3,4)
    # SYSTEM_CHOICES=tuple(zip(SYSTEM_VALS,SYSTEM_NAMES))
    SYSTEM_CHOICES=(
        (0,u''),
        (1,u'Windows Server 2006'),
        (2,u'Windows Server 2008'),
        (3,u'Centos 6.5'),
        (4,u'Centos 7.1'),
    )
    id=models.AutoField(primary_key=True) #全局ID
    groups = models.ManyToManyField(Group,blank=True,related_name='hosts',verbose_name=_("Group"))#所属应用
    storages = models.ManyToManyField(Storage,blank=True,related_name='hosts',verbose_name=_('Host'))
    systemtype=models.IntegerField(default=0,choices=SYSTEM_CHOICES)#操作系统
    manage_ip = models.CharField(max_length=15, default='',null=True)#管理IP
    service_ip = models.CharField(max_length=15, default='')#服务IP
    outer_ip = models.CharField(max_length=15, default='',null=True)#外网IP
    server_position = models.CharField(max_length=50,default='')#服务器位置
    hostname = models.CharField(max_length=50,default='localhost')#主机名称
    normal_user = models.CharField(max_length=15, default='')#普通用户
    sshpasswd = models.CharField(max_length=100,default='')#用户密码
    sshport = models.CharField(max_length=5,default='52000')#用户端口
    coreness = models.CharField(max_length=5,default='')#CPU数
    memory = models.CharField(max_length=7,default='')#内存
    root_disk=models.CharField(max_length=7,default="")#本地磁盘大小
    info=models.CharField(max_length=200,default="")