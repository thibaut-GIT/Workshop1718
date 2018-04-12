from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import  get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from ApplicationEPSI.models import Etudiant, Equipe, Soutien, Message, Intervenant, Projet


# Create your views here.

@login_required
def homepageetudiant(request, idetudiant):
    etudiant = get_object_or_404(Etudiant, id = idetudiant)
    equipes = etudiant.equipe_set.all()
    return render(request,'ApplicationEPSI/homepageetudiant.html',{'equipes' : equipes, 'etudiant' : etudiant })

@login_required
def equipe(request, idetudiant, idequipe ):
    equipe = get_object_or_404(Equipe, id = idequipe)
    etudiant = get_object_or_404(Equipe, id = idetudiant)
    return render(request, 'ApplicationEPSI/equipe.html', {'equipe' : equipe, 'etudiant' : etudiant})

@login_required
def projet(request, id):
    projet = get_object_or_404(Projet, id = id)
    equipes = projet.equipe_set.all()
    return render(request, 'ApplicationEPSI/projet.html', {'projet' : projet , 'equipes' : equipes} )

@login_required
def message(request, idetudiant, idequipe):
    equipe = get_object_or_404(Equipe, id = idequipe)
    etudiant = get_object_or_404(Etudiant, id = idetudiant)
    return render(request, 'ApplicationEPSI/message.html', {'equipe' : equipe, 'etudiant' : etudiant})

@login_required
def ZoomEquipe(request, id):
    equipe = get_object_or_404(Equipe, id = id)
    Messages =  Messages.objects.get()
    return render(request, 'ApplicationEPSI/ZoomEquipe.html', {'equipe' : equipe})

@login_required
def messagesent(request, id):
    equipe = get_object_or_404(Equipe, id = id)
    if request.method == 'POST':
        Titre = request.POST['titre']
        Contenu = request.POST['contenu']
        Messagetosent = Message(Equipe=equipe, Intervenant=equipe.Projet.Intervenant, Titre=Titre, Contenu=Contenu)
        Messagetosent.save()
    return render(request, 'ApplicationEPSI/messagesent.html', {'equipe' : equipe})


@login_required
def homepageintervant(request):
    return render(request,'ApplicationEPSI/homepageintervenant.html')

def invalid(request):
    return render(request,'ApplicationEPSI/invalid.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'ApplicationEPSI/signup.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST);
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter (name='Etudiant'):
                    usern = user.username
                    etudiant = Etudiant.objects.get(Mail=usern)
                    equipe = etudiant.equipe_set.all()
                    return redirect( '/homepageetudiant/' + str(etudiant.id) )
                elif user.groups.filter (name='Intervenant'):
                    usern = user.username
                    intervenant = Intervenant.objects.get(Mail=usern)
                    projets = intervenant.projet_set.all()
                    return render( request, 'ApplicationEPSI/homepageintervenant.html', {'projets' : projets}, {'intervenant' : intervenant})
                elif user.groups.filter (name='Responsable'):
                    return redirect('/admin/')
                elif user.groups.filter (name='Administrateur'):
                    return redirect('/admin/')
                else:
                    return redirect('/invalid/')
            else:
                return redirect('/')


    else:
        form = AuthenticationForm();
    return render(request, 'ApplicationEPSI/login.html', {'form': form})
