from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from profiles.models import User
from time import time

def index(request):
    now = time()
    if request.user.is_authenticated:
        friends_list = User.objects.prefetch_related('friends').get(id=request.user.id).friends.all()
        return render(request, 'base/index.html', {'now': now, 'friends_list': friends_list})
    else:
        return render(request, 'base/index.html', {'now': now})


def matches(request):
    return render(request, 'base/matches.html')

def create(request):
    return render(request, 'base/create.html')

def terms_error(request):
    return render(request, 'base/terms_error.html')


def coliseum(request):
    return render(request, 'base/coliseum.html')


def open(request):
    return render(request, 'base/open.html')


def matchmaking(request):
    return render(request, 'base/matchmaking.html')


def matchmaking2(request):
    return render(request, 'base/matchmaking2.html')


def matchmaking3(request):
    return render(request, 'base/matchmaking3.html')


def tournaments(request):
    return render(request, 'base/tournaments.html')


def tournaments_info_active(request):
    return render(request, 'base/tournaments-info-active.html')


def tournaments_info_active2(request):
    return render(request, 'base/tournaments-info-active2.html')


def tournaments_info_active3(request):
    return render(request, 'base/tournaments-info-active3.html')


def tournaments_info(request):
    return render(request, 'base/tournaments-info.html')


def goods(request):
    return render(request, 'base/goods.html')


def skins(request):
    return render(request, 'base/skins.html')


def client(request):
    return render(request, 'base/client.html')


def promo(request):
    return render(request, 'base/promo.html')


def blog(request):
    return render(request, 'base/blog.html')


def terms(request):
    return render(request, 'base/terms.html')


def policy(request):
    return render(request, 'base/policy.html')


def steam(request):
    if request.user.is_authenticated:
        return render(request, 'base/steam.html')
    else:
        return redirect('login')

@csrf_exempt
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect')
        return render(request, 'base/sign_in.html')


def logoutUser(request):
    logout(request)
    return redirect('index')

@csrf_exempt
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:

        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'base/sign_up.html', context)


def profile(request, pk):
    if request.user.is_authenticated:
        user = User.objects.prefetch_related('friends').get(id=pk)
        friends_list = user.friends.all()
        context = {'user': user, 'friends_list': friends_list}
        return render(request, 'base/profile.html', context)
    else:
        return redirect('login')


def profile_skins(request, pk):
    if request.user.is_authenticated:
        user = User.objects.prefetch_related('friends').get(id=pk)
        friends_list = user.friends.all()
        context = {'user': user, 'friends_list': friends_list}
        return render(request, 'base/csskinsprofile.html', context)
    else:
        return redirect('login')


def profile_inv(request, pk):
    if request.user.is_authenticated:
        user = User.objects.prefetch_related('friends').get(id=pk)
        friends_list = user.friends.all()
        context = {'user': user, 'friends_list': friends_list}
        return render(request, 'base/inventoryprofile.html', context)
    else:
        return redirect('login')


def profile_prog(request, pk):
    if request.user.is_authenticated:
        user = User.objects.prefetch_related('friends').get(id=pk)
        friends_list = user.friends.all()
        context = {'user': user, 'friends_list': friends_list}
        return render(request, 'base/programprofile.html', context)
    else:
        return redirect('login')


def profile_settings(request, pk):
    if request.user.is_authenticated:
        user = User.objects.prefetch_related('friends').get(id=pk)
        friends_list = user.friends.all()
        context = {'user': user, 'friends_list': friends_list}
        return render(request, 'base/settingsprofile.html', context)
    else:
        return redirect('login')

def ligi(request):
    return render(request, 'base/league.html')


def ligi_info(request):
    return render(request, 'base/ligi-info.html')


def rules(request):
    return render(request, 'base/rules1.html')


def wallet(request):
    if request.user.is_authenticated:
        return render(request, 'base/wallet.html')
    else:
        return redirect('login')
