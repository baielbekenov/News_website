from django.contrib.auth.views import LoginView
from django.shortcuts import render
from accounts.forms import UserForm

def create_user(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/register.html', locals())



