from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import student
from .forms import RegisterForm, CheckDetails

# Create your views here.


def homepage(request):
    return render(request,
                  template_name='main/home.html',
                  context={'students': student.objects.all().order_by('-student_timeofreg')})


def registerstu(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            stu_name = form.cleaned_data.get('student_First_Name')
            messages.success(request, f"New Student Registered: {stu_name}")
            return redirect("main:homepage")
        else:
            return render(request,
                          template_name='main/register.html',
                          context={'form': form})

    form = RegisterForm()
    return render(request,
                  template_name='main/register.html',
                  context={'form': form})


def merit_list(request):
    students = student.objects.all()
    merit_dict = {}
    marka_dict = {}
    markb_dict = {}
    markc_dict = {}
    for stu in students:
        stu_mark = stu.student_marks_A + stu.student_marks_B + stu.student_marks_C
        student_name = stu.student_First_Name + " " + stu.student_Last_Name
        merit_dict[student_name] = stu_mark
        marka_dict[student_name] = stu.student_marks_A
        markb_dict[student_name] = stu.student_marks_B
        markc_dict[student_name] = stu.student_marks_C
 #   merit_list=sorted(merit_dict.items(), key=lambda x: x[1],reverse=True)
    merit_list = [(x, y, marka_dict[x], markb_dict[x], markc_dict[x]) for (
        x, y) in sorted(merit_dict.items(), key=lambda x: x[1], reverse=True)]

    return render(request,
                  template_name='main/merit_list.html',
                  context={'meritlist': merit_list})


def check_details(request):
    if request.method == "POST":
        form = CheckDetails(request.POST)
        if form.is_valid():
            Fname = request.POST['First_Name']
            Lname = request.POST['Last_Name']
            Mobileno = request.POST['Mobile_number']
            result = student.objects.filter(student_First_Name__iexact=Fname)\
                .filter(student_Last_Name__iexact=Lname)\
                .filter(guardian_mobile_number__iexact=Mobileno)
            if result:
                return render(request,
                              template_name='main/check_details.html',
                              context={'form': form, 'student': result[0]})
            else:
                messages.error(request, "No student with those details found")
                return render(request,
                              template_name='main/check_details.html',
                              context={'form': form})
            return redirect("main:homepage")
        else:
            return render(request,
                          template_name='main/check_details.html',
                          context={'form': form})

    form = CheckDetails()
    return render(request,
                  template_name='main/check_details.html',
                  context={'form': form})
