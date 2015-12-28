from django import forms
from models import Teacher,Student,Course

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollForm(forms.ModelForm):
    class Meta:
        model = Course
    student = forms.ModelMultipleChoiceField(queryset=Student.objects)
