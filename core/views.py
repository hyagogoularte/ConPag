from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/")
def HomeView(request):
	return render(request, 'home/index.html')

