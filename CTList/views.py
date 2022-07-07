from django.shortcuts import render, redirect
from django.http import HttpResponse
from CTList.models import User

def MainPage(request):
	if request.method == 'POST':
		User.objects.create(name=request.POST['for1Form'],
			number=request.POST['for2Form'],
			comment=request.POST['for3Form'])
		return redirect('/')
	brandx = User.objects.all()
	return render(request, 'mainpage.html', {'warehouse': brandx})

def SecondPage(request):
	return render(request, 'page2.html')

def ThirdPage(request):
	if request.method == 'POST':
		Feedback.objects.create(name=request.POST['nameres'],
			game=request.POST['gameres'],
			response=request.POST['comres'])
		return redirect('/')
		items = Feedback.objects.all()
	return render(request, 'page3.html', {'responses': items})
