from django.shortcuts import render
from django.http import HttpResponse
from .models import contact
import requests
import json

# url = "https://covid-193.p.rapidapi.com/statistics"


url = "https://api.covid19api.com/summary"




response = requests.request("GET", url).json()


total_country = 190
country = []
country.insert(0, 'Select Country')
for i in range(0, total_country):
    country.append(response['Countries'][i]['Country'])

# for j in country:
#     print(j)


url_india_state = "https://api.covid19india.org/data.json"
response_india_state = requests.request("GET" , url_india_state).json()

india_state_name = []
india_state = 37
for i in range(0, india_state):
    india_state_name.append(response_india_state['statewise'][i]['state'])



def hello(request):
    total_case = response['Global']['TotalConfirmed']
    total_recovered = response['Global']['TotalRecovered']
    total_death = response['Global']['TotalDeaths']
    new_case = response['Global']['NewConfirmed']
    new_recovered = response['Global']['NewRecovered']
    new_death = response['Global']['NewDeaths']

    data = {'case': total_case, 
            'recovered': total_recovered, 
            'death': total_death,
            'new_case': new_case,
            'new_recovered': new_recovered,
            'new_death': new_death,
            'country': country,
            'user_selected_country_name': "Global Case"}
    
    if request.method == "POST":
        user_selected_country = request.POST['selectcountry']
        print(user_selected_country)
        for j in range(0, total_country):
            if user_selected_country == response['Countries'][j]['Country']:
                total_country_case = response['Countries'][j]['TotalConfirmed']
                total_country_recovered = response['Countries'][j]['TotalRecovered']
                total_country_death = response['Countries'][j]['TotalDeaths']
                new_country_case = response['Countries'][j]['NewConfirmed']
                new_recover_case = response['Countries'][j]['NewRecovered']
                new_death_case = response['Countries'][j]['NewDeaths']
            

        data = {
            'case': total_country_case,
            'recovered': total_country_recovered,
            'death': total_country_death,
            'new_case': new_country_case,
            'new_recovered': new_recover_case,
            'new_death': new_death_case,
            'user_selected_country_name': user_selected_country,
        }
        state_flag = 0
        for iterate in country:
            if user_selected_country in country and user_selected_country == 'India':
                state_flag = 1
            else:
                pass
        if(state_flag):
            print(india_state_name)
        else:
            pass
      
    # print(data)
    return render(request, "index.html", context=data)

    


def contactpage(request):
    if request.method == "POST":
        contactus = contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        summary=request.POST.get('summary')
        contactus.name = name
        contactus.email = email
        contactus.summary = summary
        contactus.save()
        return HttpResponse("<h1>We get back to you Soon!<h1>")
    return render(request, "contact.html")