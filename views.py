from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import View
from .forms import UserForm
# Create your views here.

def home(requests):
    context = locals()
    template = 'home.html'
    return render(requests, template, context)

def about(requests):
    context = locals()
    template = 'about.html'
    return render(requests, template, context)

class userformv(View):
    form_class = UserForm
    template = 'register.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template , {'form': form})
    
    
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                if user.is_active:
                    
                    login(request, user)
                    return redirect('home')
                
                
        return render(request, template , {'form': form})
                
    
    
    
    