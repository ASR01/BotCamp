from django.db import models
import uuid

from django.db.models.fields import UUIDField
from django.db.models.deletion import CASCADE 
from django.contrib.auth.models import User


# Create your models here.

class Chat(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key = True)
    host = models.ForeignKey(User, on_delete = models.CASCADE, null =True)
    updated = models.DateTimeField(auto_now = True)  # it will add the actual datetime
    
  
    
class Message(models.Model):
 
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key = True)
    chat_id = models.ForeignKey(Chat, on_delete = models.CASCADE) 
    body = models.TextField()
    user = models.CharField(max_length = 200, default = 'None')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)     
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self): # what is diplayed in admin panel
        return self
    
    
class Food(models.Model):
     
    id = models.AutoField(primary_key = True)
    chat_id = models.ForeignKey(Chat, on_delete = models.CASCADE) 
    body = models.TextField()
    user = models.CharField(max_length = 200, default = 'None')
    img_link = models.TextField(null = True, default = '#')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)   
    
    class Meta:
        ordering = ['-updated', '-created']
    
    # def __str__(self): # what is diplayed in admin panel
    #     return self

class LocationType(models.Model):
     
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200, default = 'None')
    tags = models.TextField(null = True)
    description = models.TextField(null = True)

#    updated = models.DateTimeField(auto_now=True)
#    created = models.DateTimeField(auto_now_add=True)     
    
    #class Meta:
    #    ordering = ['-updated', '-created']
    
    def __str__(self): # what is diplayed in admin panel
        return self.name

class Location(models.Model):
     
    id = models.AutoField(primary_key = True)
    type = models.ForeignKey(LocationType, on_delete = models.CASCADE) 
    name = models.CharField(max_length = 200, default = 'None')
    tags = models.TextField(null = True, default = 'location')
    lat = models.FloatField(null = True)
    long = models.FloatField(null = True)
    img_link = models.TextField(null = True, default = '#')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)     
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self): # what is diplayed in admin panel
        return self.name

class Course(models.Model):
     
    id = models.AutoField(primary_key = True)
    body = models.CharField(max_length = 200)
    description = models.TextField(null = True)
    brief_desc = models.TextField(null = True)
    teacher = models.CharField(max_length = 200, default = 'None')
    tags = models.TextField(null = True, default = 'course')
    img_link = models.TextField(null = True, default = '#')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)     
        
    def __str__(self): # what is diplayed in admin panel
        return self.body


class Exam(models.Model):
     
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200, default = 'exam')
    course = models.ForeignKey(Course, on_delete = models.CASCADE) 
    tags = models.TextField(default = 'exams')
    date = models.DateTimeField()
    img_link = models.TextField(null = True, default = '#')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)     
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self): # what is diplayed in admin panel
        return self.name

class Grade(models.Model):
     
    id = models.AutoField(primary_key = True)
    name = models.TextField(max_length = 2) # A, b, or whatever
    tags = models.TextField(null = True, default = '#')
    course = models.ForeignKey(Course, on_delete = models.CASCADE) 
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE) 
    img_link = models.TextField(null = True, default = '#')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)     
    
    
    def __str__(self): # what is diplayed in admin panel
        return self.id
    
    
class UserCourse(models.Model):
    id      = models.AutoField(primary_key = True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    course  = models.ForeignKey(Course, on_delete = models.CASCADE) 
    academic_year = models.IntegerField(default = 2021)
    img_link = models.TextField(null = True, default = '#')

    def __str__(self): # what is diplayed in admin panel
        return self
    
class Teacher(models.Model):
         
    id      = models.AutoField(primary_key = True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    tags    = models.TextField(null = True, default = '#')
    img_link = models.TextField(null = True, default = '#')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # what is diplayed in admin panel
        return self
    
    
class Sport(models.Model):
         
    id      = models.AutoField(primary_key = True)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    tags    = models.TextField(null = True, default = '#')
    img_link = models.TextField(null = True, default = '#')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # what is diplayed in admin panel
        return self