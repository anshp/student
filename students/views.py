from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse 
from django.views import generic

from students.models import Student, Group

def index(request):
    if request.method == 'POST':
        student_list = Student.objects.filter(name__startswith=request.POST['search']).order_by('id')[:50]
        context = {'student_list': student_list, 'search' :request.POST['search']}
    else:
        student_list = Student.objects.all().order_by('id')[:50]
        context = {'student_list': student_list}
    return render(request, 'students/index.html', context)


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


def groups(request):
    if request.method == 'POST':
        group_list = Group.objects.filter(name__startswith=request.POST['search']).order_by('id')[:50]
        context = {'group_list': group_list, 'search' :request.POST['search']}
        return render(request, 'students/groups.html', context)
    
    group_list = Group.objects.all().order_by('id')[:50]
    context = {'group_list': group_list}
    return render(request, 'students/groups.html', context)

def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'students/group_detail.html', {'group': group})
