from django.shortcuts import render,HttpResponse,redirect
from home.models import REGISTER
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from home.models import Contactus

# Create your views here.
def indexx(request):
    context={
        "variable":"shaurya"
    }

    return render(request,'indexx.html',context)

def about(request):
      return render(request,'about.html')
    # return HttpResponse("this is about page")
def services(request):
       if request.method=="POST":
             Hotel=request.POST.get('Hotel')
             city=request.POST.get('city')
             checkindate=request.POST.get('checkindate',default="shaurya singh")
             checkoutdate=request.POST.get('checkoutdate',default="shaurya singha")
             budget=request.POST.get('budget',default="shaurya singhaa")
             username=request.POST.get('username',default='shaurya')
             messsage=request.POST.get('messsage',default='shauryas')
             num=request.POST.get('num',default="shaurya singh")
             phone=request.POST.get('phone',default='shauryass')
             country=request.POST.get('country')
             if Hotel=='':
                  return render(request,'services.html')
             if city=='':
                  return render(request,'services.html')
             if checkindate=='':
                  return render(request,'services.html')
             if checkoutdate=='':
                  return render(request,'services.html')
             if budget=='':
                  return render(request,'services.html')
             if phone=='':
                  return render(request,'services.html')
             if num=='':
                  return render(request,'services.html')
             if Hotel=='':
                  return render(request,'services.html')
             if country=='':
                  return render(request,'services.html')
             else:
              services=REGISTER(Hotel=Hotel,city=city,checkindate=checkindate,checkoutdate=checkoutdate,budget=budget,username=username,country=country,num=num,messsage=messsage,phone=phone)
            
             services.save()
             messages.success(request,"Submitted ")
            
       return render(request,'services.html')
    # return HttpResponse("this is contact page")
def search(request):
    
      querycity=request.GET['city']
      querycheckin=request.GET['checkindate']
      querycheckout=request.GET['checkoutdate']
      querybudget=request.GET['budgets']
      querypeople=request.GET['num']
      querybudgetss=request.GET['budgetss']
      if querycity=='' :
           return render(request,'indexx.html')
      
      else:
       allPosts=REGISTER.objects.filter(city__icontains=querycity,checkindate__icontains=querycheckin,checkoutdate__icontains=querycheckout,num__gte=querypeople,budget__gte=querybudgetss,budget__lte=querybudget)
       param={'allPosts': allPosts}
       return render(request,'search.html',param)

def handleSignup(request):
     if request.method=='POST':
          emails=request.POST['emails']
          nameofuse=request.POST['nameofuser']
          password=request.POST['password']
          cpassword=request.POST['cpassword']
          if len(nameofuse) > 10:
               messages.error(request,"Username must be under 10 charcaters")
               return redirect('home')
          if not nameofuse.isalnum():
               messages.error(request,"Username should only contain alphabets and numbers")
               return redirect('home')
          if password!=cpassword:
               messages.error(request," ReEnter the correct password")
               return redirect('home')
          if User.objects.filter(email=emails).exists():
               messages.warning(request,"Email taken")
               return redirect ('home')
          if User.objects.filter(username=nameofuse).exists():
               messages.warning(request,"username taken")
               return redirect ('home')
          
          myuser=User.objects.create_user(nameofuse,emails,password)
          myuser.save()
          messages.success(request,"You have successfully created your account")
          return redirect('home')
     else:
          return HttpResponse('404 not found')
def handlelogin(request):
     if request.method=='POST':
          signinname=request.POST['nameofuser2']
          signinpassword=request.POST['passwordsign']
          user=authenticate(username=signinname,password=signinpassword)
          if user is not None:
               login(request,user)
               messages.success(request,"Successfully Logged In")
               return redirect('home')
          else:
               messages.warning("Invalid credentials  ,Please try again")
               return redirect('home')
     return HttpResponse('Error 404 not found')
    
def handlelogout(request):
     logout(request)
     messages.success(request,"Successfully Logged out")
     return redirect('home')
    
def contact(request):
     if request.method=='POST':
          name= request.POST.get('nameq')
          messagess=request.POST.get('messsage')
          phone=request.POST.get('phone')
     contact=Contactus(name=name,messagess=messagess,phone=phone)
     contact.save()
     messages.success(request,'Successfully submitted')
     return render (request,'about.html')
