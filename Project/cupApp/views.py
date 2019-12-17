from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account, Game, Category, Statistic, Comment, Score, Suggestion, Badge
from django.utils import timezone
from .forms import RegisterForm


# Create your views here.
def index(request):
    games = Game.objects.filter(added_date__lte=timezone.now()).order_by('-added_date')
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    games2 = Game.objects.filter(play_count__gte=0).order_by('-play_count')
    games3 = Game.objects.filter(game_name__contains="").order_by('game_name')
    categorys = Category.objects.filter(category_name__contains="").order_by('category_name')
    return render(request, 'cupApp/index.html',
                  {'games': games, 'scores': scores, 'games2': games2, 'games3': games3, 'categorys': categorys})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("someone tried to login and failed")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'cupApp/login.html', {})


def register(request):
    return render(request, 'cupApp/register.html')


def leaderboards(request):
    return render(request, 'cupApp/leaderboards.html')


def becomepremium(request):
    return render(request, 'cupApp/becomepremium.html')


def gamepage(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'cupApp/gamepage.html', {'game': game})


def categorypage(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'cupApp/categorypage.html', {'category': category})


def account_new(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('account_detail', pk=account.pk)
    else:
        form = RegisterForm()
    return render(request, 'cupApp/account_edit.html', {'form': form})
