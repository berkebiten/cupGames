from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
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
        username = request.POST['username']
        password = request.POST['password']
        user_check = Account.objects.filter(username=username, password=password)

        if user_check:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("index")
        else:
            return render(request, 'cupApp/index.html', {})
    return render(request, 'cupApp/login.html', {})


def register(request):
    return render(request, 'cupApp/register.html')


def logoutpage(request):
    del request.session['username']
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def profile(request):
    return render(request, 'cupApp/profile.html')


def leaderboards(request):
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    return render(request, 'cupApp/leaderboards.html', {'scores': scores})


def becomepremium(request):
    return render(request, 'cupApp/becomepremium.html')


def gamepage(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'cupApp/gamepage.html', {'game': game})


def categorypage(request, pk):
    games = Game.objects.filter(added_date__lte=timezone.now()).order_by('-added_date')
    games2 = Game.objects.filter(play_count__gte=0).order_by('-play_count')
    games3 = Game.objects.filter(game_name__contains="").order_by('game_name')
    categorys = Category.objects.filter(category_name__contains="").order_by('category_name')
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'cupApp/categorypage.html',
                  {'category': category, 'games': games, 'games2': games2, 'games3': games3, 'categorys': categorys})


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
