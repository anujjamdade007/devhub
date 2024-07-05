from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from projects.forms import projectform
from .models import Project , Review
from django.forms import ModelForm 
from .utils import searchproject
from .forms import reviewform

from django.contrib.auth.decorators import login_required
# Create your views here.




def projects(request):

    project , search_projects = searchproject(request)
    context = {
        'project':project,
        'search_projects':search_projects
    }
    return render(request , 'projects/projects.html' , context)




def project_details(request , pk):
    projectObj = Project.objects.get(pk=pk)
    tags = projectObj.tags.all()
    form = reviewform()


    if request.method == 'POST':
        form= reviewform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user.profile
            form.project = projectObj
            form.save()
            messages.success(request, ('Your comment was successfully Added!'))
            return redirect('project_details' , projectObj.id )    

    context = {
        'projectObj':projectObj,
        'tags':tags,
        'form':form,
    }
    return render(request, 'projects/project_details.html', context)





@login_required(login_url="login")
def addproject(request):
    profile = request.user.profile
    form = projectform()

    if request.method == 'POST':
        form = projectform(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
        return redirect('user_account')

    context = {
        'form':form
    }
    return render(request ,'projects/add-project.html', context)





@login_required(login_url="login")
def editproject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    form = projectform(instance=project)
    
    if request.method == 'POST':
        form = projectform(request.POST, request.FILES ,instance=project )
        if form.is_valid():
            form.save()
        return redirect('user_account')

    context = {
        'form':form
    }
    return render(request ,'projects/add-project.html', context)






@login_required(login_url="login")
def deleteproject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('user_account')

    context = {
        'project':project
    }
    return render(request , 'projects/delete-template.html', context)


