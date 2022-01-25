from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.http import HttpResponse
# Create your views here.


# def home(request):
    
#     if request.user.is_authenticated:
#         print(1)    
#         return render(request, 'chats/chat.html')        
#     else:
#         print(0) 
#         return render(request, 'chats/chat.html')