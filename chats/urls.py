from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name = 'home'), 
    
    path('login/', views.loginPage, name = 'login' ),
    path('logout/', views.logoutPage, name = 'logout' ),

    path('courses/', views.courses, name = 'courses' ),
    path('course/<str:pk>', views.course, name = 'course' ),
    path('my_courses/<str:pk>', views.my_courses, name = 'my_courses' ),

    path('food/', views.food, name = 'food' ),
    path('grades/', views.my_grades, name = 'my_grades' ),
    path('exams/', views.my_exams, name = 'my_exams' ),
    path('locations/', views.locations, name = 'locations' ),
    path('teachers/', views.teachers, name = 'teachers' ),
    path('sports/', views.sports, name = 'sports' ),

    #path('chat/<str:pk>', views.chat , name='chat' ),
    path('', views.home, name = 'home')

]