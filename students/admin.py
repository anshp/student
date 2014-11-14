from django.contrib import admin
from students.models import Student
from students.models import Group

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'date_of_birth')
    search_fields = ['name']

admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
