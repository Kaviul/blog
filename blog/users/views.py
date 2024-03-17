from django.shortcuts import render
from django.views import View
from .forms import UserRegisterForm
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})
        
 #   @csrf_exempt   
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')
