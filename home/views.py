from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.db.models import Q
from .models import Profile
from django.contrib.auth.decorators import login_required


from highscores.models import Leaderboard, Score

def index(response):
    return render(response, "home/home.html", {})

def about(response):
    return render(response, "home/about.html", {})

def mrc(response):
    return render(response, "home/mrc.html", {})

def rules(response):
    return render(response, "home/rules.html", {})

def staff(response):
    return render(response, "home/staff.html", {})

def src_rules(response):
    return redirect('https://bit.ly/SRCrules')

def stc_rules(response):
    return redirect('https://bit.ly/STC-rules')

def mrc_rules(response):
    return redirect('https://bit.ly/MRC-rules')

def discord(response):
    return redirect('https://www.discord.gg/Zq3HXRc')

def sixmans(response):
    return redirect('https://bit.ly/EloRanks')

def merch(response):
    return redirect('https://streamlabs.com/secondrobotics/merch')

def hall_of_fame(response):
    return render(response, "home/hall_of_fame.html", {})

def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                Profile.objects.create(
                    user=user
                )
                messages.success(request, f"Account was created for {username}")
                return redirect('/login')

        context = {"form": form}
        return render(request, "home/register.html", context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username or Password is Incorrect")
        context = {}
        return render(request, "home/login.html", context)

def logout_user(request):
    logout(request)
    return redirect('/login')

def user_profile(request, username):
    if not User.objects.filter(username=username).exists():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    profile = Profile.objects.filter(user__username=username)
    scoresdata = Score.objects.filter(~Q(leaderboard__name="Pushbot2"), player_name=username, approved=True)
    scores = {"overall": 0}
    sources = {}
    for score in scoresdata:
        sources.update({score.leaderboard.name: score.source})
        scores.update({score.leaderboard.name: score.score})
        scores.update({"overall": score.score + scores['overall']})
    context={"scores": scores, "username": username, "sources": sources, "profile": profile}
    return render(request, "home/user_profile.html", context)

@login_required(login_url='/login')
def user_settings(request):
    try:
        profile = request.user.profile
    except:
        profile = Profile.objects.create(user=request.user)
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
    
    return render(request, "home/user_settings.html", {"form": form, "profile": profile})