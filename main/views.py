from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import student
from .forms import RegisterForm

# Create your views here.
def homepage(request):
    return render(request,
    template_name='main/home.html',
    context={'students':student.objects.all})

def registerstu(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            stu_name = form.cleaned_data.get('student_name')
            messages.success(request, f"New Student Registered: {stu_name}")
#            args={'form': form,'text': stu_name}
            return redirect("main:homepage")
        else:
            return render(request,
            template_name='main/register.html',
            context={'form':form})

 #       else:
 #           for msg in form.errors:
 #               messages.error(request, f"{msg}: {form.errors[msg]}")

    form=RegisterForm()
    return render(request,
    template_name='main/register.html',
    context={'form':form})

