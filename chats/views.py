from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message, Chat, Course, Exam, Grade, UserCourse, Location, LocationType, Food, Teacher, Sport
from .forms import MessageForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from py_code import chat as c

# Create your views here.


def loginPage(request):
    
    page = 'login'
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exists in the system')
        
        user = authenticate(request, username =username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username and/or password incorrect')


    content = {'page':page}
    
    return render(request, 'chats/login_register.html', content)
    

def logoutPage(request):
    
    logout(request)
    
    return redirect('home')


def home(request):

    if request.user.is_authenticated:
           chat = Chat.objects.get(host = request.user)

    else:
        chat = Chat.objects.create()
    print(chat)    
    chat_messages = chat.message_set.all().order_by('-created')[:6]
    
    body_var = request.POST.get('body')
    
    if request.method == "POST":
        message = Message.objects.create(
            chat_id = chat,
            body = body_var,
            user = 'me'
        )
        #print (f.func(message.body))
        idp, body_var, idc = c.get_response(body_var) 
        print('idp', idp, 'body', body_var, 'idc', idc)
        if idp == 'food':
            return render(request, 'chats/food.html')    
        elif idp == 'courses':
            courses = Course.objects.all()
            context = {'courses': courses}
            return render(request,'chats/courses.html', context )
               
        elif idp == 'address':
            locations = Location.objects.all()
            context = { 'locations' : locations }
            return render(request,'chats/locations.html', context )
        elif idp == 'grades':
            return render(request, 'chats/courses.html') 
        
                       
        message = Message.objects.create(
            chat_id = chat,
            body = body_var,
            user = 'BotCamp'
        )
        if idp is not None:
            print(idp)

        
    content = {'chat_messages': chat_messages, 'chat': chat}
    return render(request, 'chats/home.html', content)        


##########################################)###

def chat(request):
        
    return render(request, 'chats/chat.html')

def execute(request, command):
    if command == 1:
        print(1)
        res = 1
    elif command == 2:
        print(2)
        res = 2
    else:
        print(3)
        res = 3
    
    return res


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request,'chats/courses.html', context )


def course(request, pk):
    course = Course.objects.get(id = pk)
    print(course)
    context = {'course': course}
    return render(request,'chats/course.html', context )

def my_courses(request, pk):
    
    # users = User.objects.all()
    user = User.objects.get(id = pk)
    print(user)
#    courses = Course.objects.filter(mycourses. = Course)
    context = {'user':user}#, 'courses':courses, 'users':users, }
    return render(request,'chats/my_courses.html', context )  

def my_grades(request):
    
    return render(request,'chats/my_grades.html')    

def my_exams(request):
    return render(request,'chats/my_exams.html' )  

def teachers(request):
    teachers = Teacher.objects.all()
    context = { 'teachers' : sports }
    return render(request,'chats/teachers.html', context )    

def food(request):
    sports = Sport.objects.all()
    context = { 'sports' : sports }
    return render(request,'chats/food.html', context )    

def sports(request):
    sports = Sport.objects.all()
    context = { 'sports' : sports }

    return render(request,'chats/sports.html', context )    


def locations(request):
    locations = Location.objects.all()
    context = { 'locations' : locations }
    return render(request,'chats/locations.html', context )




