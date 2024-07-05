from django.shortcuts import render , get_object_or_404 , redirect
from .models import Profile , Skills
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm , update_profile_form , skillform
from django.db.models import Q
from .utils import searchuser


# Create your views here.


def users(request):
    search_user , profile = searchuser(request)
    context = {
        'profile':profile,
        'search_user':search_user
    }
    return render(request , 'users/users.html' , context)


def user_profile(request , pk):
    profile = get_object_or_404(Profile , pk=pk)
    topskills = profile.skills_set.exclude(description__exact="")
    otherskills = profile.skills_set.filter(description="")
    context = {
        'profile':profile,
        'topskills':topskills,
        'otherskills':otherskills,
    }
    return render(request , 'users/user_profile.html' , context)


@login_required(login_url="login")
def user_account(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    skills = profile.skills_set.all()
    context = {
        'profile':profile,
        'projects':projects,
        'skills':skills
    }
    return render(request , 'users/user_account.html', context)

@login_required(login_url="login")
def update_profile(request):
    profile = request.user.profile
    form = update_profile_form(instance=profile)
    if request.method == 'POST':
            form = update_profile_form(request.POST , request.FILES , instance=profile)
            if form.is_valid():
                form.save()
            messages.success(request, ('Your Profile was successfully Updated!'))
            return redirect('user_account')
    context= {
        'form':form,
        'profile':profile
    }
    return render(request , 'users/update_profile.html' , context)


# Add-Update-Delete sl\kill

@login_required(login_url="login")
def addskill(request):
    profile = request.user.profile
    form = skillform()

    if request.method == "POST":
        form = skillform(request.POST)
        if form.is_valid():
            skill = form.save(commit = False)
            skill.owner = profile
            skill.save()
            messages.success(request, ('Your Skill was successfully Added!'))
            return redirect('user_account')

    context={
        'form':form
    }
    return render(request , 'users/addskill.html', context)

@login_required(login_url="login")
def editskill(request , pk):
    profile = request.user.profile
    skill = profile.skills_set.get(id=pk)
    form = skillform(instance = skill)

    if request.method == "POST":
        form = skillform(request.POST , instance=skill )
        if form.is_valid():
            skill.save()
            messages.success(request, ('Your Skill was successfully Updated!'))
            return redirect('user_account')

    context={
        'form':form
    }
    return render(request , 'users/addskill.html', context)

@login_required(login_url="login")
def deleteskill(request , pk):
    profile = request.user.profile
    skill = profile.skills_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, ('Your Skill was successfully Deleted!'))
        return redirect('user_account')
    context ={
        'skill':skill
    }
    return render(request , 'projects/delete-template.html' , context)


#Login/ Logout/ Register


def userlogin(request):
    page= 'login'
    #hide the login page for alredy logged users
    if request.user.is_authenticated:
        return redirect('users')

    if request.method == 'POST':
        username = request.POST["username"].lower()
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , 'username not found')

        user = authenticate(request , username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request ,"User Successfully Logged In")

            return redirect('users')
        else:
            messages.error(request ,"Username or Password not found")
        
    
    context={'page':page}
        
    return render(request ,'users/loginpage.html' , context)

def logoutuser(request):
    logout(request)
    messages.success(request , 'User Is succesfully logged out')
    return redirect('login')

def registeruser(request):
    page= 'register'
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST )
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request , 'user is succesfully created')
            login(request, user)
            return redirect('users')
        else:
            messages.error(request , 'something went wrong')


    context={
        'page':page,
        'form':form,
        }
    return render(request , 'users/loginpage.html' , context )



      