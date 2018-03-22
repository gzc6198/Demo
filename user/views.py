from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import RegisterForm
from .models import User


# Create your views here.
def register(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST, request.FILES)
        print('============================')
        if forms.is_valid():
            user = forms.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            request.session['uid'] = user.id
            return redirect('/user/info/')
        else:
            return render(request, 'register.html',{'error': forms.errors})
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        try:
            user = User.objects.get(nickname=nickname)
            if check_password(password, user.password):
                request.session['uid'] = user.id
                request.session['nickname'] = user.nickname
                request.session['nickname'] = user.nickname
                return redirect('/user/info/')
            else:
                return render(request, 'login.html', {'error': '用户名或密码不正确'})
        except User.DoesNotExist as e:
            return render(request, 'login.html', {'error': '用户名或密码不正确'})
    return render(request, 'login.html')
def info(request):
    uid = request.session.get('uid')

    if uid:
        user = User.objects.get(id = uid)
        return render(request,'user_info.html',{"user":user})
    else:
        return render(request,'login.html')
def logout(request):
    request.session.flush()
    return redirect('/user/login')
