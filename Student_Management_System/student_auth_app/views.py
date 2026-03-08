from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    """
        Here we create a view for registering user
    """
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('signin')
        else:
            return HttpResponse("Something Wrong While Creating User!!")
    template_name = 'student_auth_app/signup.html'
    context = {'form':form}
    return render(request,template_name,context)


def signin(request):
    """
        Here we create a view for checking the authenticate user only
    """
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(request,user)
            return redirect('view_student')
        else:
            return HttpResponse("Something Wrong While Log In!!")
    template_name = 'student_auth_app/signin.html'
    context = {}
    return render(request,template_name,context)


def signout(request):
    """
        Here we create a view for Log Out
    """
    logout(request)
    return redirect('signup')