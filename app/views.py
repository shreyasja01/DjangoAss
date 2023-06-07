from django.shortcuts import render,HttpResponse
from .models import Student

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST['name']
      
        email=request.POST['email']
        dob = request.POST['dob']
        gen = request.POST['gender']
        cls=request.POST['classname']
        reg = request.POST['reg']

        print("name is:", name,email,dob,gen,cls,reg)
        stud = Student()
        stud.name=name
        stud.email=email
        stud.dob=dob
        stud.gen=gen
        stud.stuClass=cls
        stud.reg=reg
       
        stud.save()
        return HttpResponse("<h1>Information saved succesfully</h1>")
    return render(request,'index.html')
            


       


   







    
