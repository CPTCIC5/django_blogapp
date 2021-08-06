from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return HttpResponseRedirect('users/login.html',{'username':username})
    else:
        form=RegisterForm()
        return render(request,'users/register.html',{'form':form})
    return render(request,'users/register.html')

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form=UserUpdateForm()
        p_form=ProfileUpdateForm()
    context={"u_form":u_form ,"p_form":p_form}
    return render(request,'users/profile.html',context)
