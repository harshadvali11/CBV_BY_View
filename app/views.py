from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

#FBV for returning string as Response

def fbv_string(request):
    return HttpResponse('<h1>This FBV string</h1>')

#FBV for returning string as Response

class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1> This Is CbvString</h1>')


#FBV for returning string as HTML page

def fbv_html(request):
    return render(request,'fbv_html.html')


#CBV for returning HTML as Response

class CbvHtml(View):
    def get(self,request):
        return render(request,'CbvHtml.html')



#insert_student_fbv 



def insert_student_fbv(request):
    ESFO=StudentMF()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('DOne')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_student_fbv.html',d)


#Insert Data into Student By using CBV

class CbvCreateStudent(View):
    def get(self,request):
        ESFO=StudentMF()
        d={'ESFO':ESFO}
        return render(request,'CbvCreateStudent.html',d)
    
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('DOne')
        else:
            return HttpResponse('Invalid')



