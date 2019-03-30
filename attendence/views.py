from django.http import HttpResponse as hr 
from django.http import JsonResponse as jr 
from django.http import HttpResponseRedirect as hrr

from django.shortcuts import render

import datetime
now = datetime.datetime.now()

a1=[]

def home(request):
	return render(request,"main.html",{"main":a1,"date":now.strftime("%d/%m/%Y")})

def process(request):
	temp=request.GET["Name"].split(",")
	for i in temp:
		a1.append(i)
	return hrr("/home")

def completed(request):
	print(a1)
	f=open("attendence.txt","w")
	n=1
	f.write("Date: " + now.strftime("%d/%m/%Y\n\n"))
	for i in a1:
		f.write(str(n)+". "+i+"\n")
		n=n+1
	f.close()
	return hrr("/home")