from django.shortcuts import render
from StudentApp.models import Student
# Create your views here.
def getRegistration(request):


    return render(request,'registration.html')

def insertToStudent(request):
    print("inside insert metod")
    name=request.POST.get("name")
    addr=request.POST.get("addr")
    total=request.POST.get("total")
    try:
        obj=Student(name=name,address=addr,total=total)
        obj.save()
    except Exception as e:
        print(e.args)
        msg=e.args
        return render(request, 'registration.html',{'msg':msg})

    return getStudentDetails(request)


def getStudentDetails(request):
    print("inside student")
    obj=Student.objects.all()
    return render(request,'studentDetails.html',{"object_list":obj})






