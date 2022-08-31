from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def todo_index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            a = request.POST.get('title')
            b = request.POST.get('sana')
            c = request.POST.get('desc')
            d = request.POST.get('status')
            e = request.POST.get('student')

            talaba = Student.objects.get(id=e)
            Todo.objects.create(title=a, sana=b, description = c, status=d, student=talaba)
            return redirect('/')
        st = Student.objects.get(user=request.user)
        data = {
            'todo': Todo.objects.filter(student=st),
            'students': Student.objects.all()
        }
        return render(request, 'index.html', data)
    return redirect('/login/')

def delete_todo(request, a):
    Todo.objects.filter(id=a).delete()
    return redirect('/')

