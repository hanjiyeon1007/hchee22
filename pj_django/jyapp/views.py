from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import ADDress
from .models import Board
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from .models import Member

def index(request):
    #return HttpResponse("<center><h/3>안녕 장고</h3><center>")
    template = loader.get_template('index.html')
    #return HttpResponse(template.render()) #나중에 session 변수값을 가져오지 못한다.
    return HttpResponse(template.render({},request)) # request 객체를 받아야 확장성이 좋아진다.

def list(request):
    template = loader.get_template('list.html')
    #addresses = ADDress.objects.all().values()
    #addresses = ADDress.objects.filter(Q(name='홍길동') | Q(addr='부산시')).values()
    #addresses = ADDress.objects.filter(name__startswith='이').values()
    addresses = ADDress.objects.all().order_by('-name').values()
    context = {
        'addresses': addresses,  
    }
    return HttpResponse(template.render(context, request))

def write(request):
    template = loader.get_template('write.html')
    return HttpResponse(template.render({},request))

def write_ok(request):
    x = request.POST['name']
    y = request.POST['addr']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    address = ADDress(name=x, addr =y, rdate =nowDatetime)
    address.save()
    return HttpResponseRedirect(reverse('list'))

def delete(request, id):
    address = ADDress.objects.get(id=id)
    address.delete()
    return HttpResponseRedirect(reverse('list'))

def update(request,id):
    template = loader.get_template('update.html')
    address = ADDress.objects.get(id=id)
    context = {
        'address': address,  
    }
    return HttpResponse(template.render(context, request))

def update_ok(request,id):
    x = request.POST['name']
    y = request.POST['addr']
    address = ADDress.objects.get(id=id)
    address.name = x
    address.addr = y
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S') #수정된 날짜를 보여주는 옵션
    address.rdate = nowDatetime
    address.save()
    return HttpResponseRedirect(reverse('list'))







#로그인
def login(request):
    #template = loader.get_template('login.html')
    #return HttpResponse(template.render({},request))
    return render(request,'login.html')

def login_ok(request):
    email = request.POST['email']
    email = email.strip()
    pwd = request.POST['pwd']
    pwd = pwd.strip()
    print("email:", email, "pwd:", pwd)
    
    #해야 할 일: DB table의 정보와 비교해서 그 결과를 template으로 넘겨줌
    try:
        member = Member.objects.get(email=email)
    except Member.DoesNotExist:
        member = None
    #print("member:", member)
    
    result = 0
    if member != None:
        print("해당 이메일 계정이 존재함")
        if member.pwd.strip() == pwd:
            print("비밀번호까지 일치")
            result = 2
        
            request.session['login_ok_user'] = member.email
        else:
            print("비밀번호 틀림")
            result = 1
    else:
        print("해당 이메일 계정이 없습니다.")
        result = 0

    template = loader.get_template('login_ok.html')
    context = {
        'result': result, #2: 성공, 1: 비번 틀림, 0: email 존재 X  
    }
    return HttpResponse(template.render(context,request))

def logout(request):
    if request.session.get('login_ok_user'):
        del request.session['login_ok_user']
    return redirect("../")

# 게시판
    
def board_list(request):
    template = loader.get_template('board/list.html')
    boards = Board.objects.all().values()
    context = {
		'boards' : boards,
	}
    return HttpResponse(template.render(context, request))

    
def board_write(request):
    template = loader.get_template('board/write.html')
    return HttpResponse(template.render({},request))
    #boards = board.objects.all().values()
    
# 템플릿
def test1(request):
    addresses = ADDress.objects.all().values()
    template = loader.get_template("template1.html")
    context = {
        'yourname':'길동',
        'addresses': addresses
    }
    return HttpResponse(template.render(context, request))

def test2(request):
    template = loader.get_template("template2.html")
    context = {
        'x': 2,
        'y': 'tiger',
        'fruits': ['apple', 'orange'],
        'fruits2': ['apple', 'orange'],
    }
    return HttpResponse(template.render(context, request))

def test3(request):
    addresses = ADDress.objects.all().values()
    temlate = loader.get_template("template3.html")
    context = {
        'fruits': ['apple', 'orange', 'melon'],
        'cars': [{'brand':'현대', 'model':'소나타', 'year':'2022'}, {'brand':'테슬라', 'model':'모델X', 'year':'2020'}],
        #'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))

def test4(request):
    temlate = loader.get_template("template4.html")
    context = {
        'name': '홍길동',
    }
    return HttpResponse(temlate.render(context, request))

def test5(request):
    addresses = ADDress.objects.all().values()
    temlate = loader.get_template("template5.html")
    context = {
        'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))

def test6(request):
    addresses = ADDress.objects.all().values()
    temlate = loader.get_template("template6.html")
    context = {
        'addresses': addresses,
    }
    return HttpResponse(temlate.render(context, request))

def test7(request):
    temlate = loader.get_template("template7.html")
    context = {}
    return HttpResponse(temlate.render(context, request))

def test8(request):
    temlate = loader.get_template("template8.html")
    context = {}
    return HttpResponse(temlate.render(context, request))