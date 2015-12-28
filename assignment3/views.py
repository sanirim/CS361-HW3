from django.shortcuts import render,redirect

from forms import TeacherForm,StudentForm,CourseForm,EnrollForm
from models import Teacher,Student,Course


def add_teacher(request):
    if request.method =='POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save
            return redirect('teacher_list', pk)
    else:
        form = TeacherForm
    return render(request, 'add_teacher.html', {'form': form})

def add_student(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save
            return redirect('student_list')
    else:
        form = StudentForm
    return render(request, 'add_student.html', {'form': form})

def add_course(request):
    if request.method =='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save
            return redirect('course_list')
    else:
        form = CourseForm
    return render(request, 'add_course.html', {'form': form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def enroll_student(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save
    return render(request, 'enroll_student.html', {'form': form})
