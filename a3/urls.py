from django.conf.urls import patterns, include, url
from assignment3 import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'a3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^addteacher/$', views.add_teacher, name='add_teacher'),
    url(r'^addstudent/$', views.add_student, name='add_student'),
    url(r'^addcourse/$', views.add_course, name='add_course'),
    url(r'^listteachers/$', views.teacher_list, name='teacher_list'),
    url(r'^liststudents/$', views.student_list, name='student_list'),
    url(r'^listcourses/$', views.course_list, name='course_list'),
    url(r'^enrollstudents/$', views.enroll_student, name='enroll_student'),



)
