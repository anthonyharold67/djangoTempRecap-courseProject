from django.urls import path
from .views import enroll_the_course, release_the_course, user_dashboard, user_login, user_logout,user_register


urlpatterns = [
    path('login/', user_login, name="login"),
    path('register/', user_register, name="register"),
    path('dashboard/', user_dashboard, name="dashboard"),
    path('logout/', user_logout, name="logout"),
    path('enroll_the_course/', enroll_the_course, name="enroll_the_course"),
    path('release_the_course/', release_the_course, name="release_the_course"),

]
