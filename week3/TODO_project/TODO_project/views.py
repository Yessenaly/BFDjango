from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
	html = "<html><body>Hello gyus!!</body></html>"
	return HttpResponse(html)