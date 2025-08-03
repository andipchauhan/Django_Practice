from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges={
    "january" : "January : Bath with cold water only",
    "february": "February : Exercise daily for whole month",
    "march": "March : Exercise daily for whole month",
    "april": "April : Exercise daily for whole month",
    "may": "May : Exercise daily for whole month",
    "june": "June : Exercise daily for whole month",
    "july": "July : Exercise daily for whole month",
    "august": "August : Exercise daily for whole month",
    "september": "September : Exercise daily for whole month",
    "october": "October : Exercise daily for whole month",
    "november": "November : Exercise daily for whole month",
    "december": "December : Exercise daily for whole month",
}

# 1
# def january(request):
#     return HttpResponse("January response is being sent")
#     # pass RESPONSE DATA(could be an HTML file) as arguemnt to this function/class instantiation

# def february(request):
#     return HttpResponse("February response is being sent")



# 2
# OBVIOUSLY THE CODE THAT SATISFIES THE URL CONDITION FIRST(i.e. written first in code) WILL SERVE THE REQUEST(i.e. that view will be executed)
# def any_month_challenge(request, month_name):  # month_name as placeholder/variable used in path()
#     challenge_text=None
#     if month_name=="january" or month_name=="1":
#         challenge_text="January : Bath with cold water only"
#     elif month_name=="february":
#         challenge_text="February : Exercise daily for whole month"
#     else:
#         return HttpResponseNotFound("Month couldn't be found")
#     return HttpResponse(challenge_text)

# def any_month_number_challenge(request, month_number):
#     return HttpResponse(month_number)



def index(request):
    months_list=list(monthly_challenges.keys())
    list_items=""
    for month in months_list:
        capitalized=month.capitalize()
        month_url = reverse("month-challenge-url",args=[month])
        list_items+=f"<li><a href=\"{month_url}\">{capitalized}</a></li>" 
        # print(list_items)
        # <li><a href="/challenges/january">January</a></li><li><a href="...">February</a></li>...
        
    response_data=f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)
    
# def func(request, dynamic_segment_or_variable_of_URL)
def any_month_challenge(request,month_name):
    # challenge_text=monthly_challenges[month_name]
    # if challenge_text:
    #     return HttpResponse(challenge_text)
    # else:
    #     HttpResponseNotFound("Month couldn't be found")
    try:
        challenge_text=monthly_challenges[month_name.lower()]
        response_data=f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Month couldn't be found</h1>")
    
def any_month_number_challenge(request,month_number):
    months=list(monthly_challenges.keys())
    if month_number>len(months):
        return HttpResponseNotFound("<h1>Out of months range. MAX 12 MONTHS</h1>")
    redirected_month=months[month_number-1]
    redirected_path= reverse("month-challenge-url", args=[redirected_month]) # /challenge/january (would adjust for changing urls)
    return HttpResponseRedirect(redirected_path)
    # return HttpResponseRedirect("/challenges/"+redirected_month)
    # REDIRECT 302|3XX: URL PART AFTER THE DOMAIN REQUIRED
    # Server tells browser to make a new request at the redirected/returned URL and SUCCESS|200.
    # This keeps browser in sync with URL.

    