from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('resume/',views.resume,name='resume'),
    path('jobSeeker/',views.jobSeeker,name='jobseeker'),
    path('jobSeeker/view-job/<int:id>',views.jobSeeker_view_job,name='jobseeker-view-job'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('user/login/',views.user_login,name='userlogin'),
    path('jobadder/login/',views.jobadder_login,name='jobadderlogin'),
    path('user/home/',views.userhome,name='userhome'),
    path('jobadder/home/',views.jobadderhome,name='jobadderhome'),
    path('user/register/',views.userregister,name='userregister'),
    path('jobadder/register/',views.jobadderregister,name='jobadderregister'),
    path('user/logout/',views.logout_user,name='logout_user'),
    path('jobadder/logout/',views.logout_jobadder,name='logout_jobadder'),
    path('jobadder/add-job/',views.add_job,name='add-job'),
    path('it_job/',views.it_job,name='itjob'),
    path('Aviation/',views.Aviation,name='Aviation'),
    path('Medical/',views. Medical,name='Medical'),
    path('Hotel_Management/',views.Hotel_Management,name='hotelmanagement'),
    path('Engineering/',views.Engineering,name='Engineering'),
    path('Dress_Design/',views.Dress_Design,name='Dress Design'),
    path('add_resume/',views.add_resume,name='add_resume'),
    path('viewresume/',views.viewresume,name='viewresume'),
    path('add-resume/',views.addresume,name='addresume'),
    path('applied-jobs/<int:id>',views.applied_jobs,name='applied-jobs'),
    path('user/apply-job/<int:id>',views.apply_job,name="apply-job"),

]
