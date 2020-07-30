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
            return redirect("main:homepage")
        else:
            return render(request,
            template_name='main/register.html',
            context={'form':form})

    form=RegisterForm()
    return render(request,
    template_name='main/register.html',
    context={'form':form})

def merit_list(request):
    students=student.objects.all()
    merit_dict={}
    marka_dict={}
    markb_dict={}
    markc_dict={}
    for stu in students:
        stu_mark=stu.student_marks_A + stu.student_marks_B + stu.student_marks_C
        student_name=stu.student_First_Name +" "+ stu.student_Last_Name
        merit_dict[student_name]=stu_mark
        marka_dict[student_name]=stu.student_marks_A
        markb_dict[student_name]=stu.student_marks_B
        markc_dict[student_name]=stu.student_marks_C
 #   merit_list=sorted(merit_dict.items(), key=lambda x: x[1],reverse=True)
    merit_list=[(x,y,marka_dict[x],markb_dict[x],markc_dict[x]) for (x,y) in sorted(merit_dict.items(), key=lambda x: x[1],reverse=True)]

    return render(request,
    template_name='main/merit_list.html',
    context={'meritlist':merit_list})
