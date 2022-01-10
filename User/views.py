from django.shortcuts import render,redirect
from .forms import LoginForm,SignupForm,PostForm
from django.contrib.auth import  authenticate,login ,logout
from  .models import Post


def login_view(request):
    if request.user.is_authenticated:
        return redirect(profile_view)
    else:
        login_form = LoginForm(request.POST)
        if request.method == "POST":

            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    Posts = Post.objects.all()
                    return render(request,"profile.html",{"form":PostForm,"posts":Posts,"user":request.user})
                return render(request, "Login.html", {"form": LoginForm, "error": "not authentic"})

            else:
                err = "provide valid details"
                return render(request, "Login.html", {"form": LoginForm, "error": err})

        return render(request, "Login.html",{"form":LoginForm})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect(profile_view)
    
    if request.method == "POST":
        sign_form = SignupForm(request.POST)
        if sign_form.is_valid():
            password = sign_form.clean_password2()
            check_pass = sign_form.cleaned_data.get('password2')

            if password == check_pass:
                username = sign_form.username_clean()
                check_user = sign_form.cleaned_data.get('username')

                if username == check_user:
                    email = sign_form.email_clean()
                    check_email = sign_form.cleaned_data.get('email')

                    if email == check_email:
                        user = sign_form.save()
                        msg = "Registered successfully,please login"

                        return render(request,"Login.html",{"form":LoginForm,"msg":msg})

                    return render(request,"Signup.html",{"form":SignupForm,"error":email})
                    
                return render(request,"Signup.html",{"form":SignupForm,"error":username})
    
            return render(request,"Signup.html",{"form":SignupForm,"error":password})

    return render(request, "Signup.html",{"form":SignupForm})


def profile_view(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        post = post_form.save(request)
        Posts = Post.objects.all()
        user = request.user
        return render(request,"profile.html",{"form":PostForm,"posts":Posts,"user":user})

    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('http://127.0.0.1:8000/admin')
        else:
            Posts = Post.objects.all()
            return render(request, "profile.html", {"form":PostForm,"posts":Posts,"user":request.user})
    else:
        return redirect(login_view)


def logout_view(request):
    logout(request)
    return redirect(login_view)


