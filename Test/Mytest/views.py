from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {'name':'Lagan'})
def add(request):
	val1 = int(request.POST["num1"])
	val2 = int(request.POST["num2"])
	Res = val1 + val2
	return render(request, 'result.html', {'Result':Res})
