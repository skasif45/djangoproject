from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

import string
import random

def hello1(request):
    return HttpResponse("<center>Welcome to TTM HomePage</center>")
def hello2(request):
    return render(request,'hello.html')

def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')
def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        your_name = request.POST['your_name']
        print(f'your name:{your_name}')
   # return HttpResponse('Form Submitted Successfully')
    a1={'your_name':your_name}
    return render(request,'print_to_console.html',a1)


def random123(request):
    ran1 = ''.join(random.sample(string.digits, k=6))
    print(ran1)
    a2={'ran1':ran1}
    return render(request,'random123.html',a2)

def randomotp(request):
    return ()

def getdate1(request):
    return render(request,'datetime123.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'datetime123.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'datetime123.html',{'form':form})

def tzfunctioncall(request):
    return render(request,'pytzexample.html')
def pagecall(request):
    return render(request,'myregisterpage.html')

from .models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        #check if the email already exists
        if Register.objects.filter(email=email).exists():
            message1 = "Email already registered. Choose a different email"
            #return HttpResponse("Email Already exists,choose another email")
            return render(request,'myregisterpage.html',{'message':message1})
        #create a new register instance and save it
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'myregisterpage.html')
import matplotlib.pyplot as plt
import numpy as np



def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'graph.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'graph.html', {'form': form})
def destinations(request):
    return render(request,'imageGeneration.html')


def weather(request):
    return render(request,'presentWeather.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'b2fcf262318aa11f896772b82fe941e5'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'presentWeather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'presentWeather.html', {'error_message': error_message})

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    return render (request,'login.html')
def signup(request):
    return render (request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render (request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render (request,'login.html')
    else:
        return render(request,'login.html')

def signup1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        pass2 = request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username alresdy taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass2)
                user.save()
                messages.info(request,'Account created successfully!')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render (request,'newhomepage.html')

def feedback(request):
    return render(request,'feed.html')
def contactmail(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comments = request.POST['comment']
        # tosend = comment + '-------------This is just a feedback form'
        data = contactus(firstname=firstname,lastname=lastname,email=email,comments=comments)
        data.save()

        return HttpResponse("<h1><center>THank you for giving the feedback</center></h1>")



