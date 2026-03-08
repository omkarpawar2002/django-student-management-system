from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def add_student(request):
    """
        Here we are creating new student records
    """
    form = StudentForm()
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('view_student')
        else:
            return HttpResponse('Something Wrong While Adding Student Details!!')
    template_name = 'student_app/add_student.html'
    context = {'form':form}
    return render(request,template_name,context)


@login_required(login_url='signin')
def view_student(request):
    """
        Here we are fetching all the student records
    """
    objs = Student.objects.all()
    template_name = 'student_app/view_student.html'
    context = {'records':objs}
    return render(request,template_name,context)


def update_student(request,pk):
    """
        Here we are Updating Student Details 
    """
    obj = Student.objects.get(id=pk)
    form = StudentForm(instance=obj)
    if(request.method == 'POST'):
        form = StudentForm(request.POST,instance=obj)
        if(form.is_valid()):
            form.save()
            return redirect('view_student')
        else:
            return HttpResponse('Something Wrong While Updating Student Details!!')
    template_name = 'student_app/update_student.html'
    context = {'form':form}
    return render(request,template_name,context)


def delete_student(request,pk):
    """
        Here we are Deleting Student Details
    """
    obj = Student.objects.get(id=pk)
    if(request.method == 'POST'):
        obj.delete()
        return redirect('view_student')
    template_name = 'student_app/delete_student.html'
    context = {'obj':obj}
    return render(request,template_name,context)
