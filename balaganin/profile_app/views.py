from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render (request, "registration/register.html", {'form': form})


def profile(request,username='Default Username'):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile', request.user.id)
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'profile_app/profile.html', context)


def home(request):
    count = User.objects.count()
    return render(request,'profile_app/home.html',{
        'count':count
    })
