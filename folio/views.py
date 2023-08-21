from django.shortcuts import render,HttpResponse,redirect
from folioapp.models import contact 
import time

def index(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        my_form=contact(name=name,email=email,subject=subject,message=message)
        my_form.save()
        data={
            'msg':'thank for contacting us'
        }
        
        return render(request,'index.html',data)
        sleep(2)
        return redirect('index')
    
    return render(request,'index.html')
 
def index1(request):
    return render(request,'index1.html')