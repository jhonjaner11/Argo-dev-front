from django.shortcuts import render, redirect
from dependences.forms import DependenceForm
from dependences.models import Dependence

# Create your views here.
def new_dependence(request):
    if request.method=='POST':
        form=DependenceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dependences:list')
    else:
        form = DependenceForm()
    return render(request,'dependences/dependence_form.html',{'form':form})

def list_dependences(request):
    
    dependences = Dependence.objects.all()
    context = {'dependences': dependences}
    form = DependenceForm()



    return render(request, 'dependences/dependence_list2.html',context)



def search_dependences(request):
    try:
        dependences = Dependence.objects.filter(name__icontains=request.POST['key_word'])
        context = {'dependences': dependences}
        print(dependences)
    except Dependence.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'dependences/dependence_list2.html',context)


def delete_dependence(request, id_dependence):
    dependence = Dependence.objects.get(id=id_dependence)
    if request.method == 'POST':
        dependence.delete()
        return redirect('dependences:list')
    return render(request, 'dependences/dependence_delete.html',{'dependence':dependence})

def edit_dependence(request, id_dependence):
    dependence = Dependence.objects.get(pk=id_dependence)
    if request.method == 'GET':
        form = DependenceForm(instance=dependence)
    else:
        form = DependenceForm(request.POST, instance=dependence)
        if form.is_valid():
            form.save()
        return redirect('dependences:list')
    return render(request, 'dependences/dependence_form.html',{'form':form})
