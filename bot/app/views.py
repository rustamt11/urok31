from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import ChatForm
from app.models import Message


class RegisterUser(CreateView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')





class UserLoginView(LoginView):
    template_name = 'app/login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')



def chat(request):
    form = ChatForm()
    messages = Message.objects.all()

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            new_message = Message(content=message)
            new_message.save()
            return redirect('home')

    return render(request, 'app/home.html', {'form': form, 'messages': messages})