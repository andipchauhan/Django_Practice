from django.urls import path
from . import views

urlpatterns = [
    
    # 1
    # http://localhost:8000/challenges/january
    # january in path() is case sensetive
    
    # path("january", views.january),
    # path("february", views.february),
    # WE CAN ALSO OMIT PATHS AT END, JUST AN EXPERIMENT NOT PRACTICAL (done on "localhost:8000/challenges" url)
    
    
    path("",views.index,name="index"), # /challenges/
    # placeholder for dynamic/random/unhardcoded/any urls
    # checked int first because int can be converted to string ALWAYS, but not vice-versa
    # so convert into int if possible because into string is obviously possible, it already is string BTW
    path("<int:month_number>",views.any_month_number_challenge),
    path("<str:month_name>",views.any_month_challenge, name="month-challenge-url"),
    # reverse will need an arguement for month_name part as it is a variable
    # NO ARG NEEDED INCASE OF STATIC URL : path ("january",views.january) OR NO URL : path("", views.index)
       
]
