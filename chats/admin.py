from django.contrib import admin

# Register your models here.

from .models import Chat, Message, Food, LocationType, Location, Course, Exam, Grade, UserCourse, Teacher, Sport

admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Food)
admin.site.register(LocationType)
admin.site.register(Location)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Grade)
admin.site.register(Sport)
admin.site.register(Teacher)
admin.site.register(UserCourse)


