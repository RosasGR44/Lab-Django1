#  hello/views.py

from django.shortcuts import render

def primeiro(request):
	return render(request, 'website/primeiro.html')

def segundo(request):
	return render(request, 'website/segundo.html')

def terceiro(request):
	return render(request, 'website/terceiro.html')