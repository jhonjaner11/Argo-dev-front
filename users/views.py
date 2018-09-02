from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Person, Dependence, ArgoUser
from .forms import PersonForm, ArgoUserForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def profile(request):
    return render(request, 'users/profile.html')
@login_required()
def home(request):
    argo_user=ArgoUser.objects.filter(user__username__contains=request.user.get_username())
    context={'argo_user': argo_user[0]}
    print(argo_user[0].person)
    return render(request, 'users/index.html', context)    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

def new_person(request):
    if request.method=='POST':
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('users:home')
    else:
        form = PersonForm()
    return render(request,'users/person_form.html',{'form':form})

def list_persons(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'users/person_list.html',context)

def search_persons(request):
    try:
        persons = Person.objects.filter(first_name__icontains=request.POST['key_word'],last_name__icontains=request.POST['key_word'])
        context = {'persons': persons}
        print(persons)
    except Person.DoesNotExist: 
        raise Http404("Question does not exist")
    return render(request, 'users/person_list.html',context)

def delete_person(request, id_person):
    person = Person.objects.get(id=id_person)
    if request.method == 'POST':
        person.delete()
        return redirect('users:list_person')
    return render(request, 'users/person_delete.html',{'person':person})
def edit_person(request, id_person):
    person = Person.objects.get(pk=id_person)
    if request.method == 'GET':
        form = PersonForm(instance=person)
    else:
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
        return redirect('users:list_person')
    return render(request, 'users/person_form.html',{'form':form})
def new_argouser(request):
    if request.method=='POST':
        form=ArgoUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('users:home')
    else:
        form = ArgoUserForm()
    return render(request,'users/argouser_form.html',{'form':form})

def list_argousers(request):
    argousers = ArgoUser.objects.all()
    context = {'argousers': argousers }
    return render(request, 'users/argouser_list.html',context)

def search_argouser(request):
    try:
        argouser = ArgoUser.objects.filter(user__username__icontains=request.POST['key_word'])
        context = {'argouser': argouser}
        print(argouser)
    except ArgoUser.DoesNotExist: 
        raise Http404("Question does not exist")
    return render(request, 'users/argouser_list.html',context)

def delete_argouser(request, id_argouser):
    argouser = ArgoUser.objects.get(id=id_argouser)
    if request.method == 'POST':
        argouser.delete()
        return redirect('users:argouser_list')
    return render(request, 'users/argouser_delete.html',{'argouser':argouser})
def edit_argouser(request, id_argouser):
    argouser = ArgoUser.objects.get(pk=id_argouser)
    if request.method == 'GET':
        form = ArgoUserForm(instance=argouser)
    else:
        form = ArgoUserForm(request.POST, instance=argouser)
        if form.is_valid():
            form.save()
        return redirect('users:argouser_list')
    return render(request, 'users/argouser_form.html',{'form':form})
