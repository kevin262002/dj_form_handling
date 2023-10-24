from django.shortcuts import render
from .forms import InputForm
from .models import Member
 
# Create your views here.
def members(request):
    context ={}
    context['form']= InputForm()
    return render(request, "kevin.html", context)

def abc(request):
        if request.method == 'POST':
            if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('roll_number') and request.POST.get('password'):
                post=Member()
                post.first_name= request.POST.get('first_name')
                post.last_name= request.POST.get('last_name')
                post.roll_number= request.POST.get('roll_number')
                post.password= request.POST.get('password')
                post.save()
                
                return render(request, 'print.html')  

        else:
                return render(request,'kevin.html')
