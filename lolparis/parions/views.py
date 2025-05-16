from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Match, Pari
from .forms import PariForm


from rest_framework import generics
from .serializers import PariSerializer

def home(request):
    matchs = Match.objects.all()
    return render(request, 'home.html', {'matchs': matchs})

@login_required
def parier_view(request):
    matchs = Match.objects.all()
    return render(request, 'parions/parier.html', {'matchs': matchs})

@login_required
def parier_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)

    if request.method == 'POST':
        form = PariForm(request.POST, match=match)
        if form.is_valid():
            pari = form.save(commit=False)
            pari.utilisateur = request.user
            pari.match = match
            pari.save()
            return redirect('historique')
    else:
        form = PariForm(match=match)

    return render(request, 'parions/parier_detail.html', {'form': form, 'match': match})

@login_required
def historique_view(request):
    paris = request.user.pari_set.all()
    return render(request, 'parions/historique.html', {'paris': paris})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'parions/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'parions/register.html', {'form': form})

class PariListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pari.objects.all()
    serializer_class = PariSerializer

def regles_view(request):
    return render(request, 'parions/regles.html')
