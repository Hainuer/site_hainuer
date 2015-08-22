# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from duome.models import UserProfile


# activate_menu
# 显示当前激活的菜单
# 说明: 
#  0: index
#  2: category
#  4: mumbler
#  8: archive
# 16: about

def index(request):
	ctx_dict = {
		'title': '首页',
		'activate_menu': '0',
	}
	return render(request, 'duome/index.html', ctx_dict)

def category(request, simple_name):
	return render(request, 'duome/index.html', {})

def mumbler(request):
	return render(request, 'duome/index.html', {})

def archive(request):
	return render(request, 'duome/index.html', {})


def about(request):
	return render(request, 'duome/index.html', {})


# TODO
# 安全性能较低
def register(request):

	tip_type = ''
	tips_msg = ''
	if request.method == 'POST':
		data = request.POST
		username = data.get('username', '')
		# TODO: 密码校验
		password = data.get('password', '')
		if len(password) <= 6:
			tip_type = 'error'
			tips_msg = '密码好像有点短了'
		else:
			if User.objects.filter(username=username):
				tip_type = 'error'
				tips_msg = '这个名称已经被使用了'
			else:
				try:
					new = User.objects.create_user(username=username, password=password, email=data.get('email', ''))
					new.save()

					profile = UserProfile(user=new, nickname=data.get('nickname'), ucode=0)
					profile.save()
					# 登录
					user_login(request)
				except Exception, e:
					tip_type = 'error'
					tips_msg = e
	else:
		pass
	ctx_dict = {
		'title': '注册',
		'tip_type': tip_type,
		'tips_msg': tips_msg,
	}
	return render(request, 'duome/register.html', ctx_dict)

def user_login(request):
	if request.method == 'POST':
		data = request.POST
		username = data.get('username')
		password = data.get('password')
		user = authenticate(username=username, password=password)
		if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/duome/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/login.html', {})











