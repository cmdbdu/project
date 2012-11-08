# Create your views here.
# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import models


def index(request):
    notes = models.Note.objects.all()
    return render_to_response('index.html',{'request':request,'notes':notes})

def register(request):
    if request.method=='POST':
        if request.POST.get('password','')==request.POST.get('repassword',''):
                username = request.POST.get('user','')
                password = request.POST.get('password','')    
                newuser=models.User(username=username,password=password)
                newuser.save()
            	request.session['username']=username
            	user = models.User.objects.get(username = username)
            	request.session['user']=user
            	return HttpResponseRedirect('/bbs') 
    return render_to_response('register.html',{'request':request})

def write(request):
    if request.method=='POST':
            title=request.POST.get('title','')
            context=request.POST.get('context','')
            author=models.User.objects.get(username=request.session['username'])
            newnote=models.Note(title=title,context=context,author=author)
            newnote.save()
            return HttpResponseRedirect('/bbs') 
    return render_to_response('write.html',{'request':request})

def read(request,parm):
    note = models.Note.objects.get(id=parm)
    replys = note.reply.all()
    return render_to_response('read.html',locals())

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/bbs')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username','')
        if username == 'root':
            return HttpResponse("不能以root用户登录<a href='http://127.0.0.1:8000/register'>注册新用户</a>,<a href='http://127.0.0.1:8000/bbs'>返回主页</a>")
        password=models.User.objects.get(username=username).password
        if password==request.POST.get('password',''):
            request.session['username']=username
            user = models.User.objects.get(username = username)
            request.session['user']=user
            return HttpResponseRedirect('/bbs')
        else:
            return render_to_response('index.html',{'request':request})
    else:
        return render_to_response('index.html',{'request':request})

def replay(request,parm1):
    note=models.Note.objects.get(id=parm1)
    replys = note.reply.all()
    if request.method=='POST':
        author = models.User.objects.get(username=request.session['username'])
        reply = request.POST.get('replay','')
        notereply = models.Replay(author=author,context=reply)
        notereply.save()
        note.reply.add(notereply)
        note.save()
        return HttpResponseRedirect('/read/'+parm1)
    else:
        return render_to_response('read.html',{'replys':replys,'parm1':parm1,'note':note,'request':request})


def reply(request,parm3,parm2):
    note=models.Note.objects.get(id=parm3)
    if request.method=='POST':
    	author = models.User.objects.get(username=request.session['username'])
    	reply = request.POST.get('replay','')
    	replayreply = models.Replay(author=author,context=reply)
    	replayreply.save()
    	replay =models.Replay.objects.get(id=parm2)
    	replay.replay.add(replayreply)
    	replay.save()
        replys = note.reply.all()
    	return render_to_response('read.html',locals())
    else:
        return render_to_response('readreplay.html',{'parm2':parm2,'note':note,'request':request})


