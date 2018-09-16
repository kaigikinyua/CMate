from django.shortcuts import render,redirect
from .models import UserDetails,Profile
from .forms import RegistrationForm,LoginForm,MyProfile
# Create your views here.
def home(request):
    return render(request,'chat/index.html')
def user(request):
    if request.method=="POST":
        profile=MyProfile(request.POST,request.FILES)
        if profile.is_valid():
            image=request.FILES['profile']
            i=Profile(profile=image,useremail="k@gmail.com")
            i.save()
            pUrl=Profile.objects.get(useremail='k@gmail.com')
            return render(request,'chat/navbar.html',{'Picture':pUrl})
        else:
            error=profile.errors
            return render(request,'chat/navbar.html',{'error_message':error})
    return render(request,'chat/user.html',{'email':Email})
def login(request):
    if request.method=="POST":
        user=LoginForm(request.POST)
        if user.is_valid():
            e=user.cleaned_data["email"]
            p=user.cleaned_data["password"]
            db=UserDetails.objects.filter(email=e,password=p)
            if len(db)!=1:
                return render(request,'chat/login.html',{'error_message':"Incorrect Credentials"})
            else:
                context={'greetings':"Hae "+user.cleaned_data['username'],'email':e}
                return render(request,'chat/navbar.html',context)
                return redirect('user')#,Email=e)
        else:
            message=user.errors
            return render(request,'chat/login.html',{'error_message':message})
    else:
         return render(request,'chat/login.html',{})
def signup(request):
    if request.method=="POST":
        #check if form is valid
        user=RegistrationForm(request.POST)
        if user.is_valid():
            e=user.cleaned_data["email"]
            db=UserDetails.objects.filter(email=e)
            if len(db)!=0:
                return render(request,'chat/signup.html',{"error_message":"The email has a registered account"})
            else:
                pass1=user.cleaned_data["password"]
                pass2=user.cleaned_data["cpassword"]
                if pass1==pass2:
                    uname=user.cleaned_data["username"]
                    newuser=UserDetails(username=uname,email=e,password=pass1)
                    newuser.save()
                    return render(request,'chat/login.html')
                else:
                    return render(request,'chat/index.html',{'error_message':"Passwords do not match"})
        else:
            message=user.errors
            return render(request,'chat/signup.html',{'error_message':message})
    else:
        return render(request,'chat/signup.html',{})
def subject(request):
    return render(request,'chat/subject.html')
