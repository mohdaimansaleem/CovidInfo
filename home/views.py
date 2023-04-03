from django.shortcuts import render , HttpResponse
import requests,json

def index(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
	"X-RapidAPI-Key": "527121b5aemsh6d9831ed570cc36p16a136jsnad034a8b777b",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
     }

    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
       
       f = open("static/app.json", "w")
       f.write(response.text)
       f.close()

       dict={
           "ans":response.text
       }
       return render(request,"index.html")
    return HttpResponse("sorry")

def preventions(request):
      return render(request,"../template/prevention.html")

def symptoms(request):
       return render(request,"../template/symptoms.html")

