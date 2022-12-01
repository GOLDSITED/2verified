from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.contrib.auth.models import User
from .models import Userprofile



from .forms import SignUpForm, UserprofileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        userprofileform = UserprofileForm(request.POST)

        if form.is_valid() and userprofileform.is_valid():
            user = form.save()

            userprofile = userprofileform.save(commit=False)
            userprofile.user = user
            userprofile.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
        userprofileform = UserprofileForm()
    
    return render(request, 'signup.html', {'form': form, 'userprofileform': userprofileform})

@login_required
def myaccount(request):
    return render(request, 'myaccount.html')

@login_required
def profile(request):
    return render(request,'profile.html')

def seller_profile(request,id):
    seller = User.objects.get(id=id,)
    context ={
        'seller':seller,
    }
    return render(request, 'seller_profile.html',context)

def create_profile(request):
    if request.method =='POST'and request.FILES.get('upload'):
        phone = request.POST.get('phone')
        image = request.FILES['upload']
        user = request.user
        userprofile = Userprofile(user=user,image=image,phone=phone)
        Userprofile.save()
    return render(request,'createprofile.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)