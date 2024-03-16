from django.shortcuts import render
from django.views import View
from .forms import UserCreationForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
        
        
    def post(self, request):
        pass
